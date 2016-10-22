## 使用WebSocket的典型流程：
  - 1.检查浏览器是否支持WebSocket                 --- Check for WebSocket browser support
  - 2.创建WebSocket的js对象                       --- Create an instance of the WebSocket JS Object
  - 3.连接WebSocket服务器                         --- Connect to the WebSocket Server
  - 4.注册WebSocket事件                           --- Register for the WebSocket events
  - 5.根据用户交互进行数据传输                    --- Perform the proper data transmission according to users' actions
  - 6.关闭连接                                    --- Close the connection


  - **1.Browser Support ---  检测浏览器是否支持WebSocket**
       if(window.WebSocket){
       console.log("WebSocket supported");
       //通过WebSocket进行操作
       }else{
       //不支持WebSocket，给出相应的提示和处理策略
       alert("Consider updating your browser for a richer experience");
       }

  - **2.The WebSocket Object**   --- WebSocket的JavaScript对象
   new WebSocket(url)   --- url：表示WebSocket要连接的服务器
       var socket = new WebSocket("ws://echo.websocket.org");
     说明：
          当创建一个WebSocket的JS对象后，它会立即连接到指定的服务器

  - **3.WebSocket 事件**        --- WebSocket Events
      WebSocket的四个主要事件：
                              事件              对应方法
                              Open              onopen
                              Message           onmessage
                              Close             onclose
                              Error             onerror

            事件处理的两种方式
            1.通过事件的对应方法     ---  推荐：简单结构清晰
            2.addEventListener方法去实现事件处理

      说明：当不同的事件发生时，会触发相应的方法，执行逻辑代码

   - 4.**WebSocket的事件处理**

      onopen      --  事件在连接成功时触发，达成第一个握手，准备传输数据
         eg：
           socket.onopen = function(event){
             console.log("Connection established");
             //在这类可以初始化资源，并展示一些用户友好提示信息
             var label = document.getElementById("status-label");
             label.innerHTML="Connection established";
           }


      onmessage   -- 数据传输事件，客户端随时监听Server，当服务器端发送给客户端数据时触发  --- 数据包括：文本、图片、二进制数据等
         eg：
           socket.onmessage = function(event){
             console.log("Data received");
             if(typeof event.data == "string"){
             var label = document.getElementById("status-label");
             label.innerHTML = event.data;
             }
           }


      onclose    --  关闭客户端与服务器的连接，不能在进行数据的传输。
                     关闭连接的原因有多种：服务器关闭，客户端调用close()方法关闭，或者TCP错误  --- 可通过 code，reason，wasClean参数检测连接关闭的原因
                     code    ---    用一个唯一的数字，表示连接中断的原因
                     reason  ---    连接中断的原因
                     wasClean  ---  用于判断连接关闭，是因为服务器的原因，还是未知的网络错误
         eg：
           socket.onclose = function(event){
           console.log("Connections closed");
           var code = event.code;
           var reason = event.reason;
           var wasClean = event.wasClean;

           var label = document.getElementById("status-label");

           if(wasClean){
               label.innerHTML = "Connection closed normally";
           }else{
               label.innerHTML ="Connection closed with message "+reason+"(Code: "+code+")";
           }
           }


      onerror    --  出错时触发的事件，该事件出发后，会接着触发close事件，终止连接  ---  注意出错时给出提示，并尝试重新建立连接
         eg：
           socket.onerror = function(event){
              console.log("Error occurred");
              //出错提示
              var label = document.getElementById("status-label");
              label.innerHTML = "Error: "+event;
           }

  - 5.**WebSocket的操作处理Actions**  即：处理方法
            两种  send()和close()

         1.send()    ---    当连接成功后，客户端可与服务端进行数据传输，send()方法用于传输数据到服务器
             eg：
                var textView = document.getElementById("text-view");
                var buttonSend = document.getElementById("send-button");
                buttonSend.onClick = function(){
                //发送数据
                if(socket.readyState == WebSocket.OPEN){
                socket.send(textView.value);
                }
                }
         特别注意：
                 只有在连接成功时才能发送数据，因此，要么把send()方法放在onopen事件中处理，要么在发送数据是进行判断：当前连接是否成功


         2.close()   ---   中断连接
              eg：
                 通过点击按钮事件来中断当前连接
                   var textView = document.getElementById("text-view");
                   var buttonStop = document.getElementById("stop-button");
                   buttonSend.onClick = function(){
                   if(socket.readyState == WebSocket.OPEN){
                      socket.close();
                      //也可之前提到的传递code和reason参数
                      //socket.close(1000,"Deliberate disconnection");
                   }
                   }


  - **6.WebSocket的属性**  Properties
        url          ---  返回WebSocket的URL
        protocol     ---  返回Server服务器使用的协议
        readyState   ---  连接状态
                                  WebSocket.OPEN           --- 已连接
                                  WebSocket.CLOSED         --- 已关闭
                                  WebSocket.CONNECTING     --- 正在连接
                                  WebSocket.CLOSING        --- 正在关闭
        bufferedAmount   ---  返回send()方法被调用时，已进入队列但尚未发送到服务器的总字节数
        binaryType       ---  返回接收到的二进制数据  -- (onmessage事件被触发时)

   
