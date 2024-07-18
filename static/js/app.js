document.getElementById('sidebarToggle').addEventListener('click', function() {
    document.querySelector('.sidebar').classList.toggle('show');
    document.getElementById('overlay').classList.toggle('show');
});

document.getElementById('overlay').addEventListener('click', function() {
    document.querySelector('.sidebar').classList.remove('show');
    document.getElementById('overlay').classList.remove('show');
});

