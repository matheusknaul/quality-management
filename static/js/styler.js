const link = document.getElementById('normas-link');

link.addEventListener('click', function(event){
    event.preventDefault();
    this.classList.toggle('activate');
});