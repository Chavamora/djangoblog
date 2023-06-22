const filtroFavoritos = document.getElementById('filtro-favoritos');
const posts = document.getElementsByClassName('item');

filtroFavoritos.addEventListener('change', () => {
  const mostrarFavoritos = filtroFavoritos.checked;

  for (let i = 0; i < posts.length; i++) {
    const post = posts[i];
    const iconoFavorito = post.querySelector('.star-icon');

    if (mostrarFavoritos && !iconoFavorito.classList.contains('favorite')) {
      post.style.display = 'none';
    } else {
      post.style.display = 'block';
    }
  }
});

    
    
