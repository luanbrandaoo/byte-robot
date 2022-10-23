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
}

function getCommands(commands) {
    for (var i = 0; i < commands.length; i++) {
        if (commands[i].startsWith('print(') == true ) {
            receivedMessage(commands[i].replace('print(', '').slice(0, -1))
        }
        if (commands[i].startsWith('speak(') == true ) {
            var snd = new Audio("data:audio/wav;base64," + commands[i].replace('speak(', '').slice(2, -2));
            snd.play();
        }
    }
}

function updateScreen() {
    var image = document.getElementById('robot-image')
    var imagepos = image.getBoundingClientRect()
    var root = document.querySelector(':root')
    root.style.setProperty('--screen-top', (imagepos.top+image.offsetHeight/7.6)+'px')
    root.style.setProperty('--screen-left', (imagepos.left+image.offsetWidth/2.70)+'px')
    root.style.setProperty('--screen-height', (image.offsetHeight/4.95)+'px')
    root.style.setProperty('--screen-width', (image.offsetWidth/3.88)+'px')
}

function sendMessage() {
    var messageText = document.getElementById("message-to-send").value
    if (messageText.replace(' ', '') == '') return
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

function voiceRecognition() {
    document.getElementById('voicebutton').classList.add("voiceanim");
    setTimeout(() => {document.getElementById('voicebutton').classList.remove("voiceanim")}, 5000)
}

window.onload = updateScreen;
window.addEventListener('resize', function(event){
    updateScreen()
})