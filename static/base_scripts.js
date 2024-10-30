
let WebSocketHasError = false;
let ResponseHasError = false;


addEventListener('DOMContentLoaded', function() {
    let connecting_times = 0;
    let socket;

    function connectWebSocket() {
        if (connecting_times > 5) {
            WebSocketHasError = true;
            return;
        }

        socket = new WebSocket('ws://' + window.location.host + '/ws/check/location/');
        connecting_times++;

        socket.onopen = function(e) {
            console.log("[open] Connection established");
        };

        socket.onmessage = function(event) {
            const data = JSON.parse(event.data);
            console.log(`[message] ${data.message}`);
        };

        socket.onclose = function(e) {
            console.log('WebSocket closed unexpectedly, trying to reconnect...');
            setTimeout(connectWebSocket, 3000); // Attempt reconnection after 3 seconds
        };

        socket.onerror = function(error) {
            console.error(`[error] ${error.message}`);
        };
    }

    connectWebSocket();
    function sendMessage(message) {
        /* 
            message = {
                'action' : 'location',
                ...
            }
        */
       try {
            socket.send(JSON.stringify(message));
        } catch (error) {
            WebSocketHasError = true;
            // TODO:  USE API TO FETCH A DATA AS A SECOND OPTIONS
            
        }

    }


    const loading = document.querySelector('.loading-screen');
    loading.classList.add('hide-loading');

})


