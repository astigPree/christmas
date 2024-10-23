
var socket = new WebSocket('ws://' + window.location.host + '/ws/some_path/');

socket.onmessage = function(e) {
    var data = JSON.parse(e.data);
    console.log(data.message);
};

socket.onclose = function(e) {
    console.error('WebSocket closed unexpectedly');
};

function sendMessage(message) {
    socket.send(JSON.stringify({
        'message': message
    }));
}

