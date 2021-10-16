$('.formulario-likes').click(function(e){
    e.preventDefault();
    id = e.target.id.slice(5, );
        $.ajax({
        type        : 'POST', // define the type of HTTP verb we want to use (POST for our form)
        url         : '/likes/add/'+id, // the url where we want to POST
        data        : $('#form_like'+id).serialize(), // our form data
        dataType    : 'json', // what type of data do we expect back from the serveidr
        success: function (data){
            document.getElementById('likes'+id).innerHTML = data['likes'] + " votes";
            document.getElementById('likes'+id).className = data['color'] + " bi bi-arrow-up-circle-fill m-0 p-0 ml-2 mr-2";
            if (data['color_c']) {
                document.getElementById('deslikes'+id).className = data['color_c'] + " bi bi-arrow-down-circle-fill m-0 p-0 ml-2 mr-2";
            }
        }
    });
});

$('.formulario-deslikes').click(function(e){
    e.preventDefault();
    id = e.target.id.slice(8, );
        $.ajax({
        type        : 'POST', // define the type of HTTP verb we want to use (POST for our form)
        url         : '/deslikes/add/'+id, // the url where we want to POST
        data        : $('#form_deslike'+id).serialize(), // our form data
        dataType    : 'json', // what type of data do we expect back from the server
        success: function (data){
            document.getElementById('deslikes'+id).className = data['color'] + " bi bi-arrow-down-circle-fill m-0 p-0 ml-2 mr-2";
            if (data['color_c']) {
                document.getElementById('likes'+id).className = data['color_c'] + " bi bi-arrow-up-circle-fill m-0 p-0 ml-2 mr-2";
                document.getElementById('likes'+id).innerHTML = data['likes'] + " votes";
            }
        }
    });
});

jQuery(document).ready(function($) {
  var alterClass = function() {
    var ww = document.body.clientWidth;
    if (ww < 985) {
      $('.cont').css({'width':''});
      $('#side-bar').css({'display':'none'});
      $('.img-teste').css({'width':'40px', 'height':'30px'})

    } else if (ww >= 986) {
      $('.cont').css({'width':'90%'});
      $('#side-bar').css({'display':'block'});
      $('.img-teste').css({'width':'50px', 'height':'40px'})

    };
  };
  $(window).resize(function(){
    alterClass();
  });
  alterClass();
});

jQuery(document).ready(function($) {
  var alterClass = function() {
    var ww = document.body.clientWidth;
    if (ww < 985) {
      $('#side-bar2').css({'display':'none'});
      $('#side-bar2-button').css({'display':'block'});

    } else if (ww >= 986) {
      $('#side-bar2').css({'display':'block'});
      $('#side-bar2-button').css({'display':'none'});

    };
  };
  $(window).resize(function(){
    alterClass();
  });
  alterClass();
});
