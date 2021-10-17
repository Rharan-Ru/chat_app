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
