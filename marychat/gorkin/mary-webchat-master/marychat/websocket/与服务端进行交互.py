var updater = {
     socket: null,

     start: function() {
         var url = "ws://" + location.host + "/chatsocket";
         updater.socket = new WebSocket(url);
         
         updater.socket.onopen = function(event) {
         }
         
         updater.socket.onclose = function(event) {
             alert("server socket closed");
         }
         
         updater.socket.onmessage = function(event) {
             updater.showMessage(event.data);
         }
     },

     showMessage: function(message) {
         console.log(message);
         $("#inbox").append(message);
         $("#message").val("");
     }
 };