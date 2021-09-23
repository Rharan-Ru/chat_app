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