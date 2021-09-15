const roomName = JSON.parse(document.getElementById('room-name').textContent);
var scroll = document.getElementById('position')
scroll.scrollTop = scroll.scrollHeight;

var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
var chat_socket = new WebSocket(ws_scheme + '://' + window.location.host + "/ws/chat/" + roomName + '/');

console.log(window.location.host)
console.log(WebSocket)

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    const user_Id = data.user_id
    const loggedUser = JSON.parse(document.getElementById('user_id').textContent)
    console.log(data.user_profile)
    if (data.entrou){
        $('#chat-log').append("<p class='text-center m-0 text-white border bg-secondary' style='opacity:80%;' ><small>"+ data.entrou +"</small></p>")
        document.getElementById('num_users').innerHTML = roomName + ' - ' +data.num_users+ ' members'
    }

    if (data.message) {
        if (user_Id === loggedUser) {
          $('#chat-log').append("<div class='m-0 mt-1 p-4 text-white' style='background:rgba(0,0,0,.9)'> <div class='row'> <div class='m-0 p-0 col-1 perfil1 row'> <img class='img-fluid ml-1 mr-1 rounded-circle' src='"+ data.user_profile +"' style='width:30px;height:30px;background:rgba(0,0,0,.9)'> <p class='m-0 text-left' style='opacity:none'> <strong>" + data.user_name + "</strong> </div> <div class='m-0 p-0 col-11 mensagem1'> <p class='m-0 p-0 ml-2 pl-2 text-left'>" + data.message + "</div></div></div>")
        }
        else {
            $('#chat-log').append("<div class='m-0 mt-1 p-4 text-white' style='background:rgba(255,255,255,.9)'> <div class='row'> <div class='m-0 p-0 col-11 mensagem1'> <p class='m-0 p-0 mr-2 pr-2 text-body text-right'>" +data.message+ "</div> <div class='m-0 p-0 col-1 perfil1 row'> <img class='img-fluid ml-1 mr-1 rounded-circle' src='" + data.user_profile + "' style='width:30px;height:30px;background:rgba(0,0,0,.9)'> <p class='m-0 text-body text-right' style='opacity:none'> <strong>"+ data.user_name +"</strong></div></div></div>")
        }
    }

    var scroll = document.getElementById('position')
    scroll.scrollTop = scroll.scrollHeight;

};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function(e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message,
    }));
    messageInputDom.value = '';
};