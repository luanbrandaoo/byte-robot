let isListening = false

document.addEventListener('keyup', event => {
    // Verifica se a tecla pressionada é a tecla de espaço ('Space')
    if (event.code === 'Space' && event.target.tagName !== 'TEXTAREA') {
      voiceButton();
    }
  });
  
async function responseRequest(address) {
    $.ajax({
        url: address,
        type: "GET",
        success: function(result) {
            getCommands(result.slice(1, -1).split('", "'))
        },
    });
}

function processing() {
    var message = document.createElement('li')
    time = new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'})
    message.innerHTML = '<div class="message-data" id="processing"><span class="message-time"><i class="fa fa-circle byte-circle"></i>Byte</span><span class="message-time timestamp">'+time+'</span></div><div class="message byte-message" id="processing_message"><div class="processing"><div class="dot-typing"></div></div></div>'
    document.getElementById('chat-messages').appendChild(message)
    var chatHistory = document.getElementById("chat-history")
    chatHistory.scrollTo(0, chatHistory.scrollHeight)
    processingScreen()
}

function getCommands(commands) {
    for (var i = 0; i < commands.length; i++) {
        if (commands[i].startsWith('print(') == true ) {
            receivedMessage(commands[i].replace('print(', '').slice(0, -1))
        }
        if (commands[i].startsWith('speak(') == true ) {
            var snd = new Audio("data:audio/mp3;base64," + commands[i].replace('speak(', '').slice(2, -2));
            snd.play();
        }
        if (commands[i].startsWith('weather(') == true ) {
            weather(commands[i].replace('weather(', '').slice(0, -1))
        }
        if (commands[i].startsWith('temperature(') == true ) {
            temperature(commands[i].replace('temperature(', '').slice(0, -1))
        }
        if (commands[i].startsWith('emotion(') == true ) {
            emotion(commands[i].replace('emotion(', '').slice(0, -1))
        }
    }
}

function updateScreen() {
    var image = document.getElementById('robot-image')
    var imagepos = image.getBoundingClientRect()
    var root = document.querySelector(':root')
    root.style.setProperty('--screen-top', (imagepos.top+image.offsetHeight/7.15)+'px')
    root.style.setProperty('--screen-left', (imagepos.left+image.offsetWidth/2.75)+'px')
    root.style.setProperty('--screen-height', (image.offsetHeight/5.04)+'px')
    root.style.setProperty('--screen-width', (image.offsetWidth/3.62)+'px')
}

function sendMessage() {
    var messageText = document.getElementById("message-to-send").value
    if (messageText.replace('\n', '').replace(' ', '') == '') return
    var message = document.createElement('li')
    time = new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'})
    message.setAttribute('class', 'message-list')
    message.innerHTML = '<div class="message-data align-right"><span class="message-time timestamp">'+time+'</span><span class="message-time">Você</span><i class="fa fa-circle me"></i></div><div class="message user-message float-right">'+messageText+'</div>'
    document.getElementById("message-to-send").value = ""
    document.getElementById('chat-messages').appendChild(message)
    var chatHistory = document.getElementById("chat-history")
    chatHistory.scrollTo(0, chatHistory.scrollHeight)
    processing()
    responseRequest("/response?input="+messageText)
}

function receivedMessage(messageText) {
    var message = document.createElement('li')
    time = new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'})
    message.innerHTML = '<div class="message-data"><span class="message-time"><i class="fa fa-circle byte-circle"></i>Byte</span><span class="message-time timestamp">'+time+'</span></div><div class="message byte-message">'+messageText+'</div>'
    document.getElementById('chat-messages').appendChild(message)
    var chatHistory = document.getElementById("chat-history")
    chatHistory.scrollTo(0, chatHistory.scrollHeight)
    document.getElementById("processing").remove()
    document.getElementById("processing_message").remove()
}

function voiceButton() {
    if (isListening) {
        document.getElementById('voicebutton').classList.remove("voiceanim")
        isListening = false
        console.log('não ouvindo')
      } else {
        document.getElementById('voicebutton').classList.add("voiceanim")
        isListening = true
        console.log('ouvindo')
      }
}

window.onload = updateScreen;
window.addEventListener('resize', function(event){
    updateScreen()
})