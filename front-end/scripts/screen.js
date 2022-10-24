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
    img.setAttribute('src', "assets/emotion/"+mode+".png")
    screen.appendChild(img)
}