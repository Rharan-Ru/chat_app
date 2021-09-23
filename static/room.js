const roomName = JSON.parse(document.getElementById('room-name').textContent);

var scroll = document.getElementById('position')
scroll.scrollTop = scroll.scrollHeight;

var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
var chatSocket = new WebSocket(ws_scheme + '://' + window.location.host + "/ws/chat/" + roomName + '/');


chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    const user_Id = data.user_id
    const loggedUser = JSON.parse(document.getElementById('user_id').textContent)

    if (data.entrou){
        $('#chat-log').append("<p class='text-center m-0 text-white border bg-secondary' style='opacity:80%;' ><small>"+ data.entrou +"</small></p>")
        document.getElementById('num_users').innerHTML = roomName + ' - ' + data.num_users.length+ ' members'
        $('#lista_users').empty();
        $('#lista_users2').empty();
        for (let x in data.num_users) {
            document.getElementById('lista_users').innerHTML += '<div class="bg-warning row p-0 m-0 mt-1 rounded"> <div class="col-1 p-1 m-0"> <img class="rounded" src="'+data.num_users[x]['image']+'" style="width:30px;height:30px;object-fit:cover" alt=""> </div><p class="col-8 text-white p-1 ms-2 m-0 text-body"><strong>'+data.num_users[x]['username']+'</strong></p></div>'
            document.getElementById('lista_users2').innerHTML += '<div class="bg-warning row p-0 m-0 mt-1 rounded"> <div class="col-1 p-1 m-0"> <img class="rounded" src="'+data.num_users[x]['image']+'" style="width:30px;height:30px;object-fit:cover" alt=""> </div><p class="col-8 text-white p-1 ms-2 m-0 text-body"><strong>'+data.num_users[x]['username']+'</strong></p></div>'
        }
    }

    if (data.message) {
        if (user_Id === loggedUser) {
          $('#chat-log').append("<div class='m-0 mt-1 p-0'> <div class='row m-0 p-0'> <div class='col-12 m-0 p-0'> <img class='float-left rounded-circle' src='"+ data.user_profile +"' style='width:30px;height:30px' alt=''> <p class='float-left ml-2'> <strong>"+ data.user_name +"</strong></p></div><div class='container rounded ml-0 pl-0 perfil1' style=''> <p class='bg-dark float-left rounded text-card p-2' style='max-width:100%; min-width:15%'>"+ data.message +"</p></div></div></div>")
        }
        else {
            $('#chat-log').append("<div class='m-0 mt-1 p-0 '> <div class='row m-0 p-0 text-body'> <div class='col-12 m-0 p-0'> <img class='float-right rounded-circle' src='"+ data.user_profile +"' style='width:30px;height:30px' alt=''> <p class='float-right mr-2'> <strong>"+ data.user_name +"</strong></p></div><div class='container rounded mr-0 pr-0 perfil1' style=''> <p class='bg-primary float-right rounded text-card p-2' style='max-width:100%;min-width:15%;'>"+ data.message +"</p></div></div></div>")
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
    if (message.length > 0) {
        chatSocket.send(JSON.stringify({
            'message': message,
        }));
        messageInputDom.value = '';
        document.getElementById('input-req').innerHTML = ''
    }
    else {
        document.getElementById('input-req').innerHTML = 'O campo acima precisa ser preenchido'
    }
};

function sair() {
    chatSocket.send(JSON.stringify({
            'sair': 'sair',
        }));
}