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
});
