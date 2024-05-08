//Marcar el boton de la talla


const botonesTalla = document.querySelectorAll('.Boton-Talla');
botonesTalla.forEach(boton => {
    boton.addEventListener('change', function() {
        if (this.checked) {
            botonesTalla.forEach(otroBoton => {
                if (otroBoton !== this) {
                    otroBoton.checked = false;
                    otroBoton.nextElementSibling.classList.remove('checked');
                }
            });
            this.nextElementSibling.classList.add('checked');
        } else {
            this.nextElementSibling.classList.remove('checked');
        }
    });
});

//Marcar el color
const botonesColor = document.querySelectorAll('.Boton-Color');
botonesColor.forEach(boton => {
    boton.addEventListener('change', function() {
        if (this.checked) {
            botonesColor.forEach(otroBoton => {
                if (otroBoton !== this) {
                    otroBoton.checked = false;
                    otroBoton.nextElementSibling.classList.remove('Seleccionado'); 
               }
            });
            this.nextElementSibling.classList.add('Seleccionado');
        } else {
            this.nextElementSibling.classList.remove('Seleccionado');
        }
    });
});

//cargar la imagen
document.getElementById('inputImagen').addEventListener('change', function(event) {
    const input = event.target;
    if (input.files && input.files[0]) {
        const reader = new FileReader();
        reader.onload = function(e) {
            
            const img = document.createElement('img');
            img.src = e.target.result;
            img.onload = function() {
                
                const container = document.getElementById('fotoFondo');
                const posX = (container.clientWidth - img.width) / 2;
                const posY = (container.clientHeight - img.height) / 2;
                img.style.left = posX + 'px';
                img.style.top = posY + 'px';
                
                container.appendChild(img);
                
                makeDraggable(img);
            }
        }
        reader.readAsDataURL(input.files[0]); 
    }
});
//mover imagen
function makeDraggable(element) {
    var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
    var scaleFactor = 1; 

    element.onmousedown = dragMouseDown;
    element.onwheel = scaleImage;

    function dragMouseDown(e) {
        e = e || window.event;
        e.preventDefault();
        pos3 = e.clientX;
        pos4 = e.clientY;
        document.onmouseup = closeDragElement;
        document.onmousemove = elementDrag;
    }
    //Aumentar imagen
    function scaleImage(e) {
        e.preventDefault();
        var delta = Math.max(-1, Math.min(1, (e.wheelDelta || -e.detail)));
        scaleFactor += delta * 0.1;
    
        scaleFactor = Math.min(3.5, scaleFactor);
        scaleFactor = Math.max(0.25, scaleFactor);
    
        element.style.transform = "scale(" + scaleFactor + ")";
    }

    function elementDrag(e) {
        e = e || window.event;
        e.preventDefault();
        pos1 = pos3 - e.clientX;
        pos2 = pos4 - e.clientY;
        pos3 = e.clientX;
        pos4 = e.clientY;
        element.style.top = (element.offsetTop - pos2) + "px";
        element.style.left = (element.offsetLeft - pos1) + "px";

        var contenedor = document.getElementById('fotoFondo');
        var contenedorRect = contenedor.getBoundingClientRect();
        var elementoRect = element.getBoundingClientRect();

        if (elementoRect.left < contenedorRect.left) {
            element.style.left = contenedorRect.left - elementoRect.left + 'px';
        }
        if (elementoRect.top < contenedorRect.top) {
            element.style.top = contenedorRect.top - elementoRect.top + 'px';
        }
        if (elementoRect.right > contenedorRect.right) {
            element.style.left = contenedorRect.right - elementoRect.width - elementoRect.left + 'px';
        }
        if (elementoRect.bottom > contenedorRect.bottom) {
            element.style.top = contenedorRect.bottom - elementoRect.height - elementoRect.top + 'px';
        }
    }

    function closeDragElement() {
        document.onmouseup = null;
        document.onmousemove = null;
    }
}