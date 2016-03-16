$(document).ready(function()
{
  $("#commune").autocomplete({

    source : function(request, response){

      $.ajax({
        url:'http://infoweb/~E145628R/listeCommune.php',
        type:'GET',
        dataType:'json',
        data:'commune='+$("#commune").val()+"&maxRows=10",

        success:function(data){
          response($.map(data, function(valeur){
                return {
                  label:valeur.Ville+" "+valeur.CodePostal,
                  valeur:valeur.Ville,
                  CodePostal:valeur.CodePostal
                }
          }));
        }
      })
    },

    select : function(event, ui){
      $("div").text(ui.item.value);
    },


  });

});
