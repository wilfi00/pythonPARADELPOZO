$(document).ready(function()
{

  $("#commune").autocomplete({

    source : function(request, response){

      $.ajax({
        url:'http://infoweb/~E145628R/codePostalComplete.php',
        //url:'http://infoweb-ens/~jacquin-c/codePostal/codePostalComplete.php',
        type:'GET',
        dataType:'json',
        data:'commune='+$("#commune").val()+"&maxRows=10",

        success:function(data){
          response($.map(data, function(valeur){
                return {
                  label:valeur.Ville+" ("+valeur.CodePostal +")",
                  valeur:valeur.Ville,
                  CodePostal:valeur.CodePostal
                }
          }));
        }
      })
    },



  });



});
