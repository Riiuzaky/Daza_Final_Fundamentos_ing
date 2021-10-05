(function(){
    var opcion = document.getElementById('opcion');
    opcion.addEventListener('change',Seleccion)
}());
function Seleccion(){
    var cod = document.getElementById("opcion").value;
    console.log(cod)
    if(cod=="General"){
        location.href='/prueba'
        window.localStorage.setItem('informacion',document.getElementById("opcion").value)
    }
    if(cod=="Comparacion"){
        location.href='/prueba'
        window.localStorage.setItem('informacion',document.getElementById("opcion").value)
    }
}