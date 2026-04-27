const navItems = Array.from(document.querySelectorAll('.nav-item'));
const panels = Array.from(document.querySelectorAll('.panel'));
const copyButtons = Array.from(document.querySelectorAll('.copy-button'));

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

copyButtons.forEach((button) => {
  button.addEventListener('click', async () => {
    const targetId = button.dataset.copyTarget;
    const snippet = document.getElementById(targetId);
    if (!snippet) {
      return;
    }

    try {
      await navigator.clipboard.writeText(snippet.textContent);
      const previousLabel = button.textContent;
      button.textContent = 'Copied';
      button.classList.add('copied');
      window.setTimeout(() => {
        button.textContent = previousLabel;
        button.classList.remove('copied');
      }, 1400);
    } catch (error) {
      button.textContent = 'Copy failed';
      window.setTimeout(() => {
        button.textContent = 'Copy code';
      }, 1400);
    }
  });
});

document.addEventListener('keydown', (event) => {
  const currentIndex = navItems.findIndex((item) => item.classList.contains('active'));
  if (event.key === 'ArrowDown' || event.key === 'ArrowRight') {
    const nextIndex = Math.min(currentIndex + 1, navItems.length - 1);
    activatePanel(navItems[nextIndex].dataset.target);
  }
  if (event.key === 'ArrowUp' || event.key === 'ArrowLeft') {
    const nextIndex = Math.max(currentIndex - 1, 0);
    activatePanel(navItems[nextIndex].dataset.target);
  }
});
