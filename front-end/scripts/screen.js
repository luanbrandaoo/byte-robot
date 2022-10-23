function weather(mode) {
    const screen = document.getElementById('robot-screen')
    var img = document.createElement('img')
    img.setAttribute('class', 'animated-icons')
    img.setAttribute('src', "assets/weather/"+mode+".svg")
    screen.appendChild(img)
}