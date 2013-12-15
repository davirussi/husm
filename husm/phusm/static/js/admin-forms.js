(function($){
  $(function(){
    $("#id_tipo").change(function(){
      tipo=document.getElementById('id_tipo').value;
      if (tipo=="Sodio"){
        //  alert(document.getElementById('id_tipo').value);
        var meqsodio = document.getElementById("id_meqsodio");
        meqsodio.value="0.0"
        meqsodio.disabled=true;
      }
      else{
         var meqsodio = document.getElementById("id_meqsodio");
         meqsodio.disabled=false;
      }
    });
  })
})(django.jQuery);
