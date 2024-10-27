
let WebSocketHasError = false;
let ResponseHasError = false;


addEventListener('DOMContentLoaded', function() {
    var socket = new WebSocket('ws://' + window.location.host + '/ws/check/location/');

    const sendWithApi = async () => {
        // TODO:  USE API TO FETCH A DATA AS A SECOND OPTIONS
        try{
            let response = await fetch('/ws/check/location/');
            
            if (!response.ok){
                let data = await response.json();
                ResponseHasError = true;
                return null;
            }

            return await response.json();

        } catch (error) {
            return null;
        
        }
    }


    socket.onmessage = function(e) {
        // Use to receive a data
        try{
            var data = JSON.parse(e.data);
        } catch (error) {
            WebSocketHasError = true;
            // TODO:  USE API TO FETCH A DATA AS A SECOND OPTIONS
            let response = sendWithApi();
            if (response){

            }
        }
        
        
    };

    socket.onclose = function(e) {
        console.error('WebSocket closed unexpectedly');
    };

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

})


