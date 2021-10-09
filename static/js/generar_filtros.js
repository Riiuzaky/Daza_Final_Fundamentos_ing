$(document).ready(function(){
    var contador=0;
    var  lista = [];
    $('#pruebab').hide(3);
    $('#limpiar').hide(3);
    $('#limpiar').click(function(){
        lista.length=0;
        contador=0;
        $('#contenedor select').val('');
        $('#contenedor select').prop('disabled',false);
        $('#pruebab').hide(3);
        $('#limpiar').hide(3);         
    });
    $('#contenedor select').change(function(e){ 
        function diferente(valor){
            return valor != e.target;   
        }
        if(lista.every(diferente)){
            lista.push(e.target);
            contador+=1;
        }
        if(contador>=2){
            $('#pruebab').show(100);
            console.log(contador)
        }
        
    });
    function ajax_login(){
         var data =$('#datos').serialize();
        $('#contenedor select').prop('disabled',true);
        $('#limpiar').show(100);
        console.log(data)
        $.ajax({
            url:'/peticion',
            data:data,
            type : 'POST',
            success: function(response){
                $('#datos').append("<h1>prueba</h1>");
            },
            error: function(error){
                console.log(error);
            }
        });
    }
    $('#datos').submit(function(e){
        e.preventDefault();             
        ajax_login();
    });
});

