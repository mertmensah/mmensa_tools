const navItems = Array.from(document.querySelectorAll('.nav-item'));
const panels = Array.from(document.querySelectorAll('.panel'));

function activatePanel(targetId) {
  navItems.forEach((item) => {
    item.classList.toggle('active', item.dataset.target === targetId);
  });
  panels.forEach((panel) => {
    panel.classList.toggle('active', panel.id === targetId);
  });
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

navItems.forEach((item) => {
  item.addEventListener('click', () => activatePanel(item.dataset.target));
});

document.addEventListener('keydown', (event) => {
  const currentIndex = navItems.findIndex((item) => item.classList.contains('active'));
  if (event.key === 'ArrowDown') {
    const nextIndex = Math.min(currentIndex + 1, navItems.length - 1);
    activatePanel(navItems[nextIndex].dataset.target);
  }
  if (event.key === 'ArrowUp') {
    const nextIndex = Math.max(currentIndex - 1, 0);
    activatePanel(navItems[nextIndex].dataset.target);
  }
});
