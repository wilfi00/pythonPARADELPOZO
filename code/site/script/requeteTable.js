$(document).ready(function()
{
    $('#listeCommune').DataTable();

    $("#recherche").click(function(){
    var comm = $("#commune").val();
    $.ajax({
      url : 'http://localhost:8080/actByCom/'+comm,
      type : 'GET',
      dataType : 'json',
      crossDomain: true,
      success : function(res){
        if (res.length == 0) {
          alert("Nothing was found :/");
        }
        else {
          photoList = res
          console.log(photoList)
          urlTab = [];
          // for (var i = 0; i < photoList.length; i++) {
          //   farm = photoList.attribute[4];
          //   serv = photoList.attribute[4];
          //   id = photoList.attribute[4];
          //   secret = photoList.attribute[4];
          //   urlTab.push("https://farm"+farm+".staticflickr.com/"+serv+"/"+id+"_"+secret+".jpg");
          // }
          // ajout(urlTab);
        }
      },
      error : function(res, statut, erreur){
        console.log(res)
        alert("Fatal error :/");
      },
      complete : function(res, statut){}
    });
  });
});
