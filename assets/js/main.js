// Portfolio Maxime COUDE — JS commun

// 1) Remplace les images manquantes par un placeholder stylé
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('img[data-ph]').forEach((img) => {
    img.addEventListener('error', () => {
      const ph = document.createElement('div');
      ph.className = 'img-ph' + (img.dataset.tall !== undefined && img.dataset.tall !== 'false' ? ' tall' : '');
      ph.textContent = '🖼 ' + (img.dataset.ph || img.alt || 'Image à exporter depuis Figma');
      img.replaceWith(ph);
    });
    // déclenche si l'image est déjà en erreur (cache)
    if (img.complete && img.naturalWidth === 0) img.dispatchEvent(new Event('error'));
  });

  // 2) Animation d'apparition au scroll
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('visible'); io.unobserve(e.target); } });
  }, { threshold: 0.08 });
  document.querySelectorAll('.reveal').forEach((el) => io.observe(el));

  // 3) Menu burger (mobile)
  const burger = document.querySelector('.nav-burger');
  const navEl = document.querySelector('.nav');
  if (burger && navEl) {
    const setOpen = (open) => {
      navEl.classList.toggle('open', open);
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    };
    burger.addEventListener('click', (e) => { e.stopPropagation(); setOpen(!navEl.classList.contains('open')); });
    navEl.querySelectorAll('.nav-links a').forEach((a) => a.addEventListener('click', () => setOpen(false)));
    document.addEventListener('click', (e) => { if (!navEl.contains(e.target)) setOpen(false); });
  }
});
