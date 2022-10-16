const Http = new XMLHttpRequest();
const responseUrl='/response?input=';

function getResponse(input){
    Http.open("GET", (responseUrl+input));
    Http.send();
    
    Http.onreadystatechange = (e) => {
      return Http.responseText
    }
}

function updateScreen() {
    var image = document.getElementById('robot-image')
    var imagepos = image.getBoundingClientRect();
    var root = document.querySelector(':root');
    root.style.setProperty('--screen-top', (imagepos.top+image.offsetHeight/7.6)+'px');
    root.style.setProperty('--screen-left', (imagepos.left+image.offsetWidth/2.70)+'px');
    root.style.setProperty('--screen-height', (image.offsetHeight/4.95)+'px');
    root.style.setProperty('--screen-width', (image.offsetWidth/3.88)+'px');
}

function sendMessage() {
    var messageText = document.getElementById("message-to-send").value
    if (messageText.replace(' ', '') == '') return
    var message = document.createElement('li');
    time = new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'})
    message.setAttribute('class', 'message-list');
    message.innerHTML = '<div class="message-data align-right"><span class="message-time timestamp">'+time+'</span><span class="message-time">Você</span><i class="fa fa-circle me"></i></div><div class="message user-message float-right">'+messageText+'</div>';
    document.getElementById("message-to-send").value = ""
    document.getElementById('chat-messages').appendChild(message);
    console.log(getResponse(messageText))
}

function receivedMessage(messageText) {
    var message = document.createElement('li');
    time = new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'})
    message.innerHTML = '<div class="message-data"><span class="message-time"><i class="fa fa-circle byte-circle"></i>Byte</span><span class="message-time timestamp">'+time+'</span></div><div class="message byte-message">'+messageText+'</div>';
    document.getElementById('chat-messages').appendChild(message);
}

window.onload = updateScreen;
window.addEventListener('resize', function(event){
    updateScreen()
});