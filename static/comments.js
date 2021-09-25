const postPK = JSON.parse(document.getElementById('post-pk').textContent);

var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
var chatSocket = new WebSocket(ws_scheme + '://' + window.location.host + "/ws/comments/" + postPK + '/');


chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);

    const user_Id = data.user_id
    const loggedUser = JSON.parse(document.getElementById('user_id').textContent)

    if (data.comment) {
        $('#commentSection').prepend('<div class="m-0 p-0"> <div class="m-0 p-0 row" id="comment'+data.com_pk+'"> <div class="m-0 p-0 col-1 "> <img class="mx-auto d-block mt-1 img-fluid rounded embed-responsive-item img-teste" src="'+data.user_profile+'" alt="" style="width:50px;height:40px;object-fit:cover"> </div><div class="col-11 bg-dark text-white p-1 mt-1 card"> <p class="m-0 p-0"><strong>'+data.author+'</strong></p><p class="m-0 p-0">'+data.comment+'</p></div><span class="col-1 m-0 p-0"></span> <div class="col-11 m-0 p-0" id="accordion"> <a class="reply m-0 p-0" data-toggle="collapse" data-target="#collapseOne'+data.com_pk+'"><i class="bi bi-reply-fill"></i><small>Reply</small></a> <div class="p-0 m-0 collapse" aria-labelledby="headingOne" data-parent="#accordion" id="collapseOne'+data.com_pk+'"> <form action="" class="form-group m-0 p-0 row"> <input type="text" class="chat-message-input-reply col-10 form-control mb-3 required-field '+data.author+'" id="'+data.com_pk+'" maxlength="5000" placeholder="..." required> <button class="chat-message-submit-reply col-2 btn btn-dark msg" style="height:10%" type="submit" value="Send"> > </button> </form> </div></div></div><div class="col-12 m-0 p-0" id="accordion'+data.com_pk+'"><a class="btn btn-link text-white" id="count'+data.com_pk+'" data-toggle="collapse" data-target="#collapseTwo'+data.com_pk+'" aria-controls="collapseTwo">See all comments ('+data.num_comments+')</a></div>')
        $('#count'+data.com_pk+'').css({'display':'none'});
    }
    else {
        if ($('.texte'+data.parent_pk+'')[0]){
            var span_teste = $('.texte'+data.parent_pk+'')[0].className
            if (span_teste.includes('show')) {
                $('#accordion'+data.parent_pk+'').append('<span class="collapseTwo'+data.parent_pk+' show texte'+data.parent_pk+'" id="collapseTwo'+data.parent_pk+'" aria-labelledby="headingOne" data-parent="#accordion'+data.parent_pk+'"><div class="m-0 ml-3 p-0 row" id="replies"> <div class="m-0 p-0 col-1 "> <img class="mx-auto d-block mt-1 img-fluid rounded embed-responsive-item img-teste2" src="'+data.user_profile+'" alt="" style="width:30px;height:30px;object-fit:cover"> </div><div class="col-11 text-white p-1 mt-1 card" style="background-color:#bd2130e6"> <p class="m-0 p-0"><strong>'+data.author+'</strong></p><p class="m-0 p-0"><a class="mr-2">'+data.reply_author+'</a>'+data.reply+'</p></div><span class="col-1 m-0 p-0"></span> <div class="col-11 m-0 p-0" id="accordion'+data.reply_pk+'"> <a class="reply m-0 p-0" data-toggle="collapse" data-target="#collapseOne'+data.reply_pk+'"><i class="bi bi-reply-fill"></i><small>Reply</small></a> <div class="p-0 m-0 collapse" aria-labelledby="headingOne" data-parent="#accordion" id="collapseOne'+data.reply_pk+'"> <form action="" class="form-group m-0 p-0 row"> <input type="text" class="chat-message-input-reply col-10 form-control mb-3 required-field '+data.author+'" id="'+data.parent_pk+'" maxlength="5000" placeholder="..." required> <button class="chat-message-submit-reply col-2 btn btn-dark msg" style="height:10%" id="" type="submit" value="Send"> > </button> </form> </div></div></div></span>')
                document.getElementById('count'+data.parent_pk+'').innerHTML = 'See all comments ('+data.num_comments+')'
            }
            else {
                $('#accordion'+data.parent_pk+'').append('<span class="collapseTwo'+data.parent_pk+' collapse texte'+data.parent_pk+'" id="collapseTwo'+data.parent_pk+'" aria-labelledby="headingOne" data-parent="#accordion'+data.parent_pk+'"><div class="m-0 ml-3 p-0 row" id="replies"> <div class="m-0 p-0 col-1 "> <img class="mx-auto d-block mt-1 img-fluid rounded embed-responsive-item img-teste2" src="'+data.user_profile+'" alt="" style="width:30px;height:30px;object-fit:cover"> </div><div class="col-11 text-white p-1 mt-1 card" style="background-color:#bd2130e6"> <p class="m-0 p-0"><strong>'+data.author+'</strong></p><p class="m-0 p-0"><a class="mr-2">'+data.reply_author+'</a>'+data.reply+'</p></div><span class="col-1 m-0 p-0"></span> <div class="col-11 m-0 p-0" id="accordion'+data.reply_pk+'"> <a class="reply m-0 p-0" data-toggle="collapse" data-target="#collapseOne'+data.reply_pk+'"><i class="bi bi-reply-fill"></i><small>Reply</small></a> <div class="p-0 m-0 collapse" aria-labelledby="headingOne" data-parent="#accordion" id="collapseOne'+data.reply_pk+'"> <form action="" class="form-group m-0 p-0 row"> <input type="text" class="chat-message-input-reply col-10 form-control mb-3 required-field '+data.author+'" id="'+data.parent_pk+'" maxlength="5000" placeholder="..." required> <button class="chat-message-submit-reply col-2 btn btn-dark msg" style="height:10%" id="" type="submit" value="Send"> > </button> </form> </div></div></div></span>')
                document.getElementById('count'+data.parent_pk+'').innerHTML = 'See all comments ('+data.num_comments+')'
            }
        }
        else {
            $('#accordion'+data.parent_pk+'').append('<span class="collapseTwo'+data.parent_pk+' show texte'+data.parent_pk+'" id="collapseTwo'+data.parent_pk+'" aria-labelledby="headingOne" data-parent="#accordion'+data.parent_pk+'"><div class="m-0 ml-3 p-0 row" id="replies"> <div class="m-0 p-0 col-1 "> <img class="mx-auto d-block mt-1 img-fluid rounded embed-responsive-item img-teste2" src="'+data.user_profile+'" alt="" style="width:30px;height:30px;object-fit:cover"> </div><div class="col-11 text-white p-1 mt-1 card" style="background-color:#bd2130e6"> <p class="m-0 p-0"><strong>'+data.author+'</strong></p><p class="m-0 p-0"><a class="mr-2">'+data.reply_author+'</a>'+data.reply+'</p></div><span class="col-1 m-0 p-0"></span> <div class="col-11 m-0 p-0" id="accordion'+data.reply_pk+'"> <a class="reply m-0 p-0" data-toggle="collapse" data-target="#collapseOne'+data.reply_pk+'"><i class="bi bi-reply-fill"></i><small>Reply</small></a> <div class="p-0 m-0 collapse" aria-labelledby="headingOne" data-parent="#accordion" id="collapseOne'+data.reply_pk+'"> <form action="" class="form-group m-0 p-0 row"> <input type="text" class="chat-message-input-reply col-10 form-control mb-3 required-field '+data.author+'" id="'+data.parent_pk+'" maxlength="5000" placeholder="..." required> <button class="chat-message-submit-reply col-2 btn btn-dark msg" style="height:10%" id="" type="submit" value="Send"> > </button> </form> </div></div></div></span>')
            document.getElementById('count'+data.parent_pk+'').innerHTML = 'See all comments ('+data.num_comments+')'
        }

        if (data.num_comments > 2){
            $('#count'+data.parent_pk+'').css({'display':'inline-block'});
        }
    }
}


document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};


document.querySelector('#chat-message-submit').onclick = function(e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const comment = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'comment': comment,
    }));
    messageInputDom.value = '';
};


$(document).submit(function(e) {
    e.preventDefault()
    var reply = e.target.children[0]
    span_teste = ''
    if ($('.texte'+reply.id+'')[0]){
        var span_teste = $('.texte'+reply.id+'')[0].className
        if (span_teste.includes('show')) {
            span_teste = 'show'
        }
        else {
            span_teste = 'collapse'
        }
    }
    else {
        span_teste = 'show'
    }

    reply_author = reply.className.slice(65,)
    chatSocket.send(JSON.stringify({
        'reply': reply.value,
        'parent_id': reply.id,
        'reply_author': reply_author,
        'span_comment': span_teste,
    }));
    e.target.children[0].value = '';
});


function removeComment(e) {
    console.log(e);
    console.log('removido');
    $('#all-comment' + e).remove();
}
