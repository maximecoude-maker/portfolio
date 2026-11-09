// Case-study section navigation. Content remains readable without JavaScript.
const initCats = () => {
  const burger = document.querySelector('.nav-burger');
  const nav = document.querySelector('.nav');
  document.addEventListener('keydown', (event) => {
    if (!['Escape', 'Esc'].includes(event.key) || !burger || !nav || !nav.classList.contains('open')) return;
    nav.classList.remove('open');
    burger.setAttribute('aria-expanded', 'false');
    burger.focus();
  });
  const links = [...document.querySelectorAll('.cats-toc a')];
  const sections = links.map((link) => document.querySelector(link.hash)).filter(Boolean);
  if (!links.length || !sections.length || !('IntersectionObserver' in window)) return;
  const observer = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      for (const link of links) {
        if (link.hash === '#' + entry.target.id) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      }
    }
  }, { rootMargin: '-18% 0px -62% 0px', threshold: 0 });
  sections.forEach((section) => observer.observe(section));
};
if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initCats, { once: true });
else initCats();
