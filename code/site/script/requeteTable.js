function myOwnApi(data) {
  if (data.length == 0) {
    alert("Nothing was found :/");
  }
  else {
    var t = $('#activ').DataTable();
    t.clear();
    for (var i = 0; i < data.length; i++) {
      t.row.add( [data[i].comLib,data[i].actLib,data[i].id] ).draw( false );
    }
  }
}

$(document).ready(function()
{
    $('#listeCommune').DataTable();

    $("#recherche").click(function(){
    var comm = $("#commune").val();
    $.ajax({
      url : 'http://localhost:8080/actByCom/'+comm,
      type : 'GET',
      dataType : 'jsonp',
      jsonpCallback : 'myOwnApi',
      success : function(res){console.log("test1")},
      error : function(res, statut, erreur){
        console.log(erreur)},
      complete : function(res, statut){console.log("test3")}
    });

    $("#maps").click(function(){
    var comm = $("#commune").val();
    var win = window.open('https://www.google.com/maps/place/'+comm,'_blank');
    win.focus();
    });
  });
});
