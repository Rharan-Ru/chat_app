const postPK = JSON.parse(document.getElementById('post-pk').textContent);

var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
var chatSocket = new WebSocket(ws_scheme + '://' + window.location.host + "/ws/comments/" + postPK + '/');

console.log('deu certo')
console.log(postPK)

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);

    const user_Id = data.user_id
    const loggedUser = JSON.parse(document.getElementById('user_id').textContent)

    if (data.comment) {
        $('#commentSection').append('<div class="m-0 p-0"> <div class="m-0 p-0 row" id="comment1"> <div class="m-0 p-0 col-1 "> <img class="mx-auto d-block mt-1 img-fluid rounded embed-responsive-item img-teste" src="'+data.user_profile+'" alt="" style="width:50px;height:40px;object-fit:cover"> </div><div class="col-11 bg-dark text-white p-1 mt-1 card"> <p class="m-0 p-0"><strong>'+data.username+'</strong></p><p class="m-0 p-0">'+data.comment+'</p></div><span class="col-1"></span> <div class="col-11 m-0 p-0" id="accordion"> <a class="reply col-11 m-0 p-0" data-toggle="collapse" data-target="#collapseOne1"><i class="bi bi-reply-fill"></i><small>Reply</small></a> <div class="row p-0 m-0 collapse" aria-labelledby="headingOne" data-parent="#accordion" id="collapseOne1"> <input type="text" class="col-10 form-control mb-3 required-field com_pk2" id="chat-message-input-reply" maxlength="5000" placeholder="..." required> <button class="col-2 btn btn-dark msg" style="height:10%" id="chat-message-submit-reply" type="submit" value="Send"> > </button> </div></div></div><div class="col-12 m-0 p-0" id="accordion2"></div>')
    }
    else {
        console.log('teste')
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
    console.log(comment)
    chatSocket.send(JSON.stringify({
        'comment': comment,
    }));
    messageInputDom.value = '';
};


document.querySelector('#chat-message-input-reply').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit-reply').click();
    }
};


document.querySelector('#chat-message-submit-reply').onclick = function(e) {
    const messageInputDom = document.querySelector('#chat-message-input-reply');
    console.log(messageInputDom.className.slice(46,))
    const reply = messageInputDom.value;
    console.log(reply + ' comment-reply')
    chatSocket.send(JSON.stringify({
        'reply': reply,
    }));
    messageInputDom.value = '';
};
