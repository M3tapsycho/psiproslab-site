(function () {
  var menu = document.querySelector('.menu');
  var nav = document.querySelector('.nav');
  if (menu && nav) menu.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    menu.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
})();
