document.querySelector('#room-name-input').focus();

document.querySelector('#room-name-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#room-name-submit').click();
    }
};

document.querySelector('#room-name-submit').onclick = function(e) {
    var roomName = document.querySelector('#room-name-input').value.replaceAll(' ','_');
    window.location.pathname = '/chat/' + roomName + '/';
};

var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
var chatSocket = new WebSocket(ws_scheme + '://' + window.location.host + "/ws/chat/");
chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    $('#lista_salas').empty();
    for (let x in data.salas) {
        document.getElementById('lista_salas').innerHTML += '<div class="col-lg-4" style="background-image: "> <a href="/chat/'+data.salas[x]['name']+'/"> <div class="card bg-dark"> <img src="/static/steven_bg08.gif" class="card-img embed-responsive" alt="..." style="height:20vh;object-fit:cover"> <div class="card-img-overlay" style="justify-content: center;align-items: center;display: flex"> <h3 class="card-text text-uppercase text-body">'+data.salas[x]['name']+'</h3> </div><p class="text-center text-white" id="'+data.salas[x]['name']+'">'+data.salas[x]['users']+' pessoas no chat</p></div></a> </div>'
        var name = data.salas[x]['name']
        document.getElementById(name).innerHTML = data.salas[x]['users'] + ' pessoas no chat'

    }
}