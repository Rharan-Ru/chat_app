jQuery(document).ready(function($) {
  var alterClass = function() {
    var ww = document.body.clientWidth;
    if (ww < 750) {
      $('.cont').css({'width':''});
      $('#side-bar').css({'display':'none'});
      $('.img-teste').css({'width':'40px', 'height':'30px'})

    } else if (ww >= 751) {
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