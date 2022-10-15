function updateScreen() {
    var image = document.getElementById('robot-image')
    var imagepos = image.getBoundingClientRect();
    var root = document.querySelector(':root');
    root.style.setProperty('--screen-top', (imagepos.top+image.offsetHeight/7.6)+'px');
    root.style.setProperty('--screen-left', (imagepos.left+image.offsetWidth/2.70)+'px');
    root.style.setProperty('--screen-height', (image.offsetHeight/4.95)+'px');
    root.style.setProperty('--screen-width', (image.offsetWidth/3.88)+'px');
}

window.onload = updateScreen;
window.addEventListener('resize', function(event){
    updateScreen()
});