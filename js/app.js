/**
 * Gestión & Tecno-Pedagogía: Blog Educativo
 * Interactividad, Filtros, Comentarios en LocalStorage, Progreso y Modo Oscuro
 */

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initReadingProgress();
  initSearchAndTags();
  initComments();
});

/* ==========================================================================
   1. Control de Tema (Modo Claro / Modo Oscuro)
   ========================================================================== */
function initTheme() {
  const toggleBtn = document.getElementById('theme-toggle');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const savedTheme = localStorage.getItem('blog_theme');

  if (savedTheme) {
    document.documentElement.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);
  } else if (prefersDark) {
    document.documentElement.setAttribute('data-theme', 'dark');
    updateThemeIcon('dark');
  }

  if (toggleBtn) {
    toggleBtn.addEventListener('click', () => {
      const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('blog_theme', newTheme);
      updateThemeIcon(newTheme);
    });
  }
}

function updateThemeIcon(theme) {
  const icon = document.getElementById('theme-icon');
  if (icon) {
    icon.textContent = theme === 'dark' ? '☀️' : '🌙';
    icon.setAttribute('aria-label', theme === 'dark' ? 'Cambiar a modo claro' : 'Cambiar a modo oscuro');
  }
}

/* ==========================================================================
   2. Barra de Progreso de Lectura
   ========================================================================== */
function initReadingProgress() {
  const progressBar = document.getElementById('reading-progress');
  if (!progressBar) return;

  window.addEventListener('scroll', () => {
    const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = height > 0 ? (winScroll / height) * 100 : 0;
    progressBar.style.width = scrolled + '%';
  }, { passive: true });
}

/* ==========================================================================
   3. Búsqueda Reactiva y Filtrado por Etiquetas
   ========================================================================== */
function initSearchAndTags() {
  const searchInput = document.getElementById('search-input');
  const tagButtons = document.querySelectorAll('.tag-filter-btn');
  const articles = document.querySelectorAll('.article-card');
  const countIndicator = document.getElementById('visible-count');

  let activeTag = 'all';
  let searchTerm = '';

  function filterArticles() {
    let visibleCount = 0;

    articles.forEach(article => {
      const tags = (article.getAttribute('data-tags') || '').toLowerCase();
      const content = article.textContent.toLowerCase();

      const matchesTag = activeTag === 'all' || tags.includes(activeTag.toLowerCase());
      const matchesSearch = !searchTerm || content.includes(searchTerm.toLowerCase());

      if (matchesTag && matchesSearch) {
        article.style.display = 'block';
        visibleCount++;
      } else {
        article.style.display = 'none';
      }
    });

    if (countIndicator) {
      countIndicator.textContent = `Mostrando ${visibleCount} de ${articles.length} artículos`;
    }
  }

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchTerm = e.target.value.trim();
      filterArticles();
    });
  }

  tagButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      tagButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      activeTag = btn.getAttribute('data-tag');
      filterArticles();
    });
  });

  // Permitir clics directos sobre las etiquetas dentro de cada artículo
  const articleTags = document.querySelectorAll('.article-tag');
  articleTags.forEach(tagElem => {
    tagElem.style.cursor = 'pointer';
    tagElem.addEventListener('click', () => {
      const tagText = tagElem.textContent.trim().replace('#', '');
      const matchingBtn = Array.from(tagButtons).find(b => b.getAttribute('data-tag').toLowerCase() === tagText.toLowerCase());
      if (matchingBtn) {
        matchingBtn.click();
        window.scrollTo({ top: document.querySelector('.controls-section').offsetTop - 70, behavior: 'smooth' });
      }
    });
  });
}

/* ==========================================================================
   4. Sistema Interactivo de Comentarios por Artículo (LocalStorage)
   ========================================================================== */
function initComments() {
  const commentForms = document.querySelectorAll('.comment-form');

  commentForms.forEach(form => {
    const articleId = form.getAttribute('data-article-id');
    const feed = document.getElementById(`comments-feed-${articleId}`);

    // Cargar comentarios existentes de localStorage
    renderStoredComments(articleId, feed);

    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const nameInput = form.querySelector('.comment-author-input');
      const textInput = form.querySelector('.comment-text-input');

      const author = nameInput.value.trim() || 'Colega Académico';
      const comment = textInput.value.trim();

      if (!comment) return;

      const newEntry = {
        author,
        comment,
        date: new Date().toLocaleDateString('es-ES', { day: '2-digit', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit' })
      };

      saveComment(articleId, newEntry);
      appendCommentToFeed(feed, newEntry);

      textInput.value = '';
    });
  });
}

function getStoredComments(articleId) {
  try {
    const stored = localStorage.getItem(`blog_comments_${articleId}`);
    return stored ? JSON.parse(stored) : [];
  } catch (err) {
    return [];
  }
}

function saveComment(articleId, commentObj) {
  const comments = getStoredComments(articleId);
  comments.push(commentObj);
  localStorage.setItem(`blog_comments_${articleId}`, JSON.stringify(comments));
}

function renderStoredComments(articleId, feedElement) {
  if (!feedElement) return;
  const comments = getStoredComments(articleId);
  feedElement.innerHTML = '';

  if (comments.length === 0) {
    const emptyMsg = document.createElement('p');
    emptyMsg.className = 'empty-comments-note';
    emptyMsg.style.fontSize = '0.8rem';
    emptyMsg.style.color = 'var(--text-light)';
    emptyMsg.style.fontStyle = 'italic';
    emptyMsg.textContent = 'Sé el primero en compartir tu perspectiva crítica o responder a la interrogante.';
    feedElement.appendChild(emptyMsg);
    return;
  }

  comments.forEach(c => appendCommentToFeed(feedElement, c, false));
}

function appendCommentToFeed(feedElement, commentObj, clearEmpty = true) {
  if (!feedElement) return;

  const emptyMsg = feedElement.querySelector('.empty-comments-note');
  if (emptyMsg && clearEmpty) {
    emptyMsg.remove();
  }

  const commentCard = document.createElement('div');
  commentCard.className = 'comment-item';
  commentCard.innerHTML = `
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 0.25rem;">
      <div class="comment-author-name">${escapeHTML(commentObj.author)}</div>
      <span style="font-size:0.72rem; color:var(--text-light);">${commentObj.date}</span>
    </div>
    <p style="color:var(--text-muted); line-height:1.45; margin:0;">${escapeHTML(commentObj.comment)}</p>
  `;
  feedElement.appendChild(commentCard);
}

function escapeHTML(str) {
  return str.replace(/[&<>'"]/g, 
    tag => ({
      '&': '&amp;',
      '<': '&lt;',
      '>': '&gt;',
      "'": '&#39;',
      '"': '&quot;'
    }[tag] || tag)
  );
}
