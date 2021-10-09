(function(){
    var opcionCambiada =function() {
        console.log("Cambio");
        console.log(localStorage.getItem('informacion'));        
        contador = contador+1;
        console.log(contador);
        if(localStorage.getItem('informacion')=="General"){
            if(contador==2){
                document.getElementsByTagName('select')[1].disabled = true;
                document.getElementsByTagName('select')[2].disabled = true;
                document.getElementsByTagName('select')[3].disabled = true;
                document.getElementsByTagName('select')[4].disabled = true;
                contador=0;
            }
        }    
    }

    var contador= 0;
    var opcion = document.getElementsByTagName('select');

    for (var index = 1; index <opcion.length; index++) {
        opcion[index].addEventListener('change',opcionCambiada);
    }
      
}());


  



