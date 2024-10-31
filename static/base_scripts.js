
let WebSocketHasError = false;
let ResponseHasError = false; 
let isSearching = false;
let searchScreen = undefined;
let sendMessage = undefined;

function openSearchScreen() {
    if (searchScreen) {
        searchScreen.classList.remove('close-pop-up');
    }
}

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, showError);
    } else {
        alert("Geolocation is not supported by this browser.");
    }
}

function showPosition(position) {
    var lat = position.coords.latitude;
    var lon = position.coords.longitude;
    if (sendMessage){
        sendMessage({
            'action' : 'location',
            'latitude' : lat,
            'longitude' : lon
        });
    }
    
    // document.getElementById("location").innerHTML = "Latitude: " + lat + "<br>Longitude: " + lon;
}

function showError(error) {
    switch(error.code) {
        case error.PERMISSION_DENIED:
            alert("User denied the request for Geolocation.");
            break;
        case error.POSITION_UNAVAILABLE:
            alert("Location information is unavailable.");
            break;
        case error.TIMEOUT:
            alert("The request to get user location timed out.");
            break;
        case error.UNKNOWN_ERROR:
            alert("An unknown error occurred.");
            break;
    }
}

 


addEventListener('DOMContentLoaded', function() {

    searchScreen = document.getElementById('pop-up-screen');    
    this.document.getElementById('stop-searching').addEventListener('click', function() {
        if (searchScreen) {
            searchScreen.classList.add('close-pop-up');
            isSearching = false;
        }
    });

    
 

    let connecting_times = 0;
    let socket;

    function connectWebSocket() {
        if (connecting_times > 1) {
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
    
    
    sendMessage = async(message)=> {
        /* 
            message = {
                'action' : 'location',
                ...
            }
        */
        console.log("Sending message:", message);
       try {
            socket.send(JSON.stringify(message));
            
        } catch (error) {
            WebSocketHasError = true;
            // TODO:  USE API TO FETCH A DATA AS A SECOND OPTIONS 
            console.log("There was an error sending the message:", error);
            try {
                // http://127.0.0.1:8000/api/nearby_trees?latitude=12.375339279210461&longitude=123.63268216492332
                const response = await fetch(`http://127.0.0.1:8000/api/nearby_trees?latitude=${message.latitude}&longitude=${message.longitude}`);
                const data = await response.json();
                
                if (response.ok){
                    console.log(data);
                } else {
                    ResponseHasError = true;
                    console.error('HTTP error!', response);
                }
 
            } catch (error) {
                console.log(error);
            }


            
        }

    }



    


    const loading = document.querySelector('.loading-screen');
    loading.classList.add('hide-loading');

})



