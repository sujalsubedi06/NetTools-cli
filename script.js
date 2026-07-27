/**
 * NetTools CLI — script.js
 * Handles: icon rendering, mobile menu, scroll reveals,
 * animated terminal typing sequence, and copy-to-clipboard.
 */

document.addEventListener('DOMContentLoaded', () => {
  initIcons();
  initMobileMenu();
  initScrollReveal();
  initTerminalTyping();
  initCopyButtons();
});

/* ---------- Lucide icon rendering ---------- */
function initIcons() {
  if (window.lucide) {
    window.lucide.createIcons();
  } else {
    // lucide script loads with `defer`; retry shortly if not ready yet
    window.addEventListener('load', () => window.lucide && window.lucide.createIcons());
  }
}

/* ---------- Mobile navigation menu ---------- */
function initMobileMenu() {
  const toggle = document.getElementById('menuToggle');
  const menu = document.getElementById('mobileMenu');
  if (!toggle || !menu) return;

  toggle.addEventListener('click', () => {
    const isOpen = menu.classList.toggle('is-open');
    toggle.setAttribute('aria-expanded', String(isOpen));
  });

  // Close the menu after a link is chosen
  menu.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      menu.classList.remove('is-open');
      toggle.setAttribute('aria-expanded', 'false');
    });
  });
}

/* ---------- Scroll-triggered reveal animations ---------- */
function initScrollReveal() {
  const targets = document.querySelectorAll('.reveal');
  if (!targets.length) return;

  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (prefersReducedMotion) {
    targets.forEach((el) => el.classList.add('is-visible'));
    return;
  }

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15 }
  );

  targets.forEach((el) => observer.observe(el));
}

/* ---------- Animated hero terminal typing sequence ---------- */
function initTerminalTyping() {
  const body = document.getElementById('terminalBody');
  if (!body) return;

  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (prefersReducedMotion) return; // keep static markup as-is

  const sequence = [
    { type: 'command', text: 'nettools scan example.com' },
    { type: 'output', text: 'Resolving example.com...' },
    { type: 'output', text: 'DNS records found' },
    { type: 'output', text: 'Starting TCP scan...' },
    { type: 'output', text: '9 open ports detected' },
    { type: 'output', text: 'HTTP headers analyzed' },
    { type: 'output', text: 'SSL certificate validated' },
    { type: 'output', text: 'Report generated' },
  ];

  body.innerHTML = '';
  body.setAttribute('aria-live', 'polite');

  let lineIndex = 0;

  const runNextLine = () => {
    if (lineIndex >= sequence.length) {
      appendFinalPrompt(body);
      return;
    }

    const item = sequence[lineIndex];
    lineIndex += 1;

    if (item.type === 'command') {
      typeCommandLine(body, item.text, runNextLine);
    } else {
      appendOutputLine(body, item.text);
      window.setTimeout(runNextLine, 220);
    }
  };

  // Small delay before the sequence starts, so the hero can settle in first
  window.setTimeout(runNextLine, 500);
}

function typeCommandLine(body, text, onDone) {
  const line = document.createElement('p');
  line.className = 'terminal__line';

  const prompt = document.createElement('span');
  prompt.className = 'terminal__prompt';
  prompt.textContent = '$';

  const command = document.createElement('span');
  command.className = 'terminal__command';

  line.append(prompt, document.createTextNode(' '), command);
  body.appendChild(line);

  let charIndex = 0;
  const typeChar = () => {
    if (charIndex <= text.length) {
      command.textContent = text.slice(0, charIndex);
      charIndex += 1;
      window.setTimeout(typeChar, 28);
    } else {
      window.setTimeout(onDone, 260);
    }
  };
  typeChar();
}

function appendOutputLine(body, text) {
  const line = document.createElement('p');
  line.className = 'terminal__line terminal__line--out';

  const check = document.createElement('span');
  check.className = 'ok';
  check.textContent = '[✓]';

  line.append(check, document.createTextNode(' ' + text));
  body.appendChild(line);
}

function appendFinalPrompt(body) {
  const line = document.createElement('p');
  line.className = 'terminal__line';

  const prompt = document.createElement('span');
  prompt.className = 'terminal__prompt';
  prompt.textContent = '$';

  const cursor = document.createElement('span');
  cursor.className = 'terminal__cursor';

  line.append(prompt, document.createTextNode(' '), cursor);
  body.appendChild(line);
}

/* ---------- Copy-to-clipboard for install snippet ---------- */
function initCopyButtons() {
  const buttons = document.querySelectorAll('.copy-btn');

  buttons.forEach((button) => {
    const targetId = button.getAttribute('data-copy-target');
    const target = targetId ? document.getElementById(targetId) : null;
    if (!target) return;

    button.addEventListener('click', async () => {
      const text = Array.from(target.querySelectorAll('p'))
        .map((p) => p.textContent.trim())
        .filter(Boolean)
        .join('\n');

      try {
        await navigator.clipboard.writeText(text);
        showCopied(button);
      } catch (err) {
        fallbackCopy(text);
        showCopied(button);
      }
    });
  });
}

function showCopied(button) {
  const icon = button.querySelector('i');
  button.classList.add('is-copied');
  if (icon) icon.setAttribute('data-lucide', 'check');
  if (window.lucide) window.lucide.createIcons();

  window.setTimeout(() => {
    button.classList.remove('is-copied');
    if (icon) icon.setAttribute('data-lucide', 'copy');
    if (window.lucide) window.lucide.createIcons();
  }, 1800);
}

function fallbackCopy(text) {
  const textarea = document.createElement('textarea');
  textarea.value = text;
  textarea.style.position = 'fixed';
  textarea.style.opacity = '0';
  document.body.appendChild(textarea);
  textarea.select();
  document.execCommand('copy');
  document.body.removeChild(textarea);
}