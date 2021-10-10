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
        $.ajax({
            url:'/peticion',
            data:data,
            type : 'POST',
            success: function(response){
                var dicc = JSON.parse(response);
                console.log(dicc)
                $('#datos').append(dicc.tabla);
                $('#imagen').attr('src','data:image/png;base64, '+dicc.grafica);
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

