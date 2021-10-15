console.log('teste')

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
        document.getElementById('lista_salas').innerHTML += '<div class="col-md-4 mt-3"> <a href="'+data.salas[x]['name']+'/" class="room-link" style="text-decoration:none"> <div class="card" style="background-color:#343a406e"> <div class="card-horizontal p-2"> <div class="img-square-wrapper embed-responsive img-fluid" style="width:150px; height:64px;"> <img class="embed-responsive-item img-fluid rounded" src="/media/'+data.salas[x]['image']+'" alt="Card image cap" style="width:200px;object-fit: cover"> </div><div class="card-body text-white p-0 m-0 ml-1"> <h5 class="card-title p-0 m-0">'+ data.salas[x]['name'] +'</h4> <p class="m-0 p-0" id="'+data.salas[x]['name']+'">'+ data.salas[x]['users'] +' users online</p></div></div></div> </a> </div>'
        var name = data.salas[x]['name']
        console.log(data.salas[x]['image'])
        document.getElementById(name).innerHTML = data.salas[x]['users'] + ' users online'

    }
}