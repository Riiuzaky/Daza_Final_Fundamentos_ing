(function(){

    const opcionCambiada = () => {
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
        }
    }
    if(localStorage.getItem('informacion')=="Comparacion"){
        if(contador==3){
            document.getElementsByTagName('select')[1].disabled = true;
            document.getElementsByTagName('select')[2].disabled = true;
            document.getElementsByTagName('select')[3].disabled = true;
            document.getElementsByTagName('select')[4].disabled = true;
            }
    
    }
      };
      

    var contador= 0;
    var opcion = document.getElementsByTagName('select');
    opcion[1].addEventListener('change', opcionCambiada);
    opcion[2].addEventListener('change', opcionCambiada);
    opcion[3].addEventListener('change', opcionCambiada);
    opcion[4].addEventListener('change', opcionCambiada);
  
}());


  



