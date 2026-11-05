// Cabinet CS : menu mobile, boutons « Copier », sommaire de page et Blason interactif.
(function () {
  var btn = document.querySelector('.menu-btn');
  var nav = document.getElementById('nav');
  if (btn && nav) {
    btn.addEventListener('click', function () {
      var open = btn.getAttribute('aria-expanded') !== 'true';
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      nav.classList.toggle('open', open);
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) { btn.setAttribute('aria-expanded', 'false'); nav.classList.remove('open'); }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('open')) { btn.click(); btn.focus(); }
    });
  }

  document.querySelectorAll('.copy').forEach(function (b) {
    b.addEventListener('click', function () {
      var t = b.getAttribute('data-copy');
      var done = function () { b.textContent = 'Copié'; setTimeout(function () { b.textContent = 'Copier'; }, 1600); };
      try { navigator.clipboard.writeText(t).then(done, function () {}); } catch (e) {}
    });
  });

  // Sommaire : met en évidence la section visible
  var toc = document.querySelector('.toc');
  if (toc && 'IntersectionObserver' in window) {
    var links = {};
    toc.querySelectorAll('a').forEach(function (a) { links[a.getAttribute('href').slice(1)] = a; });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting && links[en.target.id]) {
          Object.keys(links).forEach(function (k) { links[k].classList.remove('on'); });
          var a = links[en.target.id]; a.classList.add('on');
          a.scrollIntoView({ block: 'nearest', inline: 'center', behavior: 'smooth' });
        }
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    Object.keys(links).forEach(function (id) { var s = document.getElementById(id); if (s) io.observe(s); });
  }

  // Blason : affiche le détail d'une compétence
  document.querySelectorAll('.blason').forEach(function (bl) {
    var panel = bl.querySelector('.bl-detail');
    bl.querySelectorAll('.comp').forEach(function (c) {
      c.addEventListener('click', function () {
        var same = c.getAttribute('aria-pressed') === 'true';
        bl.querySelectorAll('.comp').forEach(function (x) { x.setAttribute('aria-pressed', 'false'); });
        if (same) { panel.hidden = true; return; }
        c.setAttribute('aria-pressed', 'true');
        panel.querySelector('small').textContent = c.getAttribute('data-axe');
        panel.querySelector('b').textContent = c.textContent;
        panel.querySelector('p').textContent = c.getAttribute('data-desc');
        panel.hidden = false;
      });
    });
  });
})();
