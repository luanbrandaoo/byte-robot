function cleanScreen() {
    const screen = document.getElementById('robot-screen')
    var child = screen.lastElementChild; 
        while (child) {
            screen.removeChild(child);
            child = screen.lastElementChild;
        }
}

function weather(mode) {
    const screen = document.getElementById('robot-screen')
    cleanScreen()
    var img = document.createElement('img')
    img.setAttribute('class', 'animated-icons')
    img.setAttribute('src', "assets/weather/"+mode+".svg")
    screen.appendChild(img)
}

function emotion(mode) {
    const screen = document.getElementById('robot-screen')
    cleanScreen()
    var img = document.createElement('img')
    img.setAttribute('class', 'animated-icons')
    img.setAttribute('src', "assets/emotions/"+mode+".png")
    screen.appendChild(img)
}

function processingScreen() {
    const screen = document.getElementById('robot-screen')
    cleanScreen()
    var img = document.createElement('div')
    //img.setAttribute('class', 'animated-icons')
    img.innerHTML = '<div class="dot-typing-screen"></div>'
    screen.appendChild(img)
}

function startScreen() {
setTimeout(() => { 
    emotion('neutral');
},500);
}

window.onload = startScreen();
