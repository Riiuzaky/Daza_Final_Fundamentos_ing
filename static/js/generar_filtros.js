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
                var datosg = JSON.parse(dicc.grafica);
                var lienzo =document.getElementById('lienzo').getContext('2d');
                var myChart = new Chart(lienzo, {
                    type: 'bar',
                    data: {
                        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
                        datasets: [{
                            label: '# of Votes',
                            data: [12, 19, 3, 5, 2, 3],
                            backgroundColor: [
                                'rgba(255, 99, 132, 0.2)',
                                'rgba(54, 162, 235, 0.2)',
                                'rgba(255, 206, 86, 0.2)',
                                'rgba(75, 192, 192, 0.2)',
                                'rgba(153, 102, 255, 0.2)',
                                'rgba(255, 159, 64, 0.2)'
                            ],
                            borderColor: [
                                'rgba(255, 99, 132, 1)',
                                'rgba(54, 162, 235, 1)',
                                'rgba(255, 206, 86, 1)',
                                'rgba(75, 192, 192, 1)',
                                'rgba(153, 102, 255, 1)',
                                'rgba(255, 159, 64, 1)'
                            ],
                            borderWidth: 1
                        }]
                    },
                    options: {
                        maintainAspectRatio: false,
                        responsive:true,
                        scales: {
                            yAxes: [{
                                ticks: {
                                    beginAtZero: true
                                }
                            }]
                        }
                    }
                });
                console.log(datosg)
                $('#datos').append(dicc.tabla);
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

