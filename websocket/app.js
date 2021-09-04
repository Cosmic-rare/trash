var connection = new WebSocket('wss://echo.websocket.org');

var btn = document.getElementById('btn');


connection.onopen = function(e) {
  console.log("connect");
};


btn.addEventListener('click', function(e) {
  var text = document.getElementById('text');
 
  connection.send(text.value);
})

connection.onmessage = function(e) {
 
    console.log(e.data);
 
};



connection.onclose = function() {
  console.log("disconnect");
};