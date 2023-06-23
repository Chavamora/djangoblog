const filtroFavoritos = document.getElementById('filtro-favoritos');
const posts = document.getElementsByClassName('item');

if(filtroFavoritos) {
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
} else {
  const checkbox = document.getElementById("filtro_fecha_limite");
  const tasksContainer = document.getElementById("tasks");

  checkbox.addEventListener("change", function() {
    if (this.checked) {
      // Ordenar tareas por fecha límite
      const tasks = Array.from(tasksContainer.getElementsByClassName("item"));
      tasks.forEach((task, index) => {
        task.dataset.originalOrder = index;
      });

      const sortedTasks = tasks.sort(compareDates);

      // Mover las tareas ordenadas al contenedor
      sortedTasks.forEach(task => {
        tasksContainer.appendChild(task);
      });
    } else {
      // Restaurar el orden original de las tareas
      const tasks = Array.from(tasksContainer.getElementsByClassName("item"));

      tasks.sort(compareOriginalOrder);

      // Mover las tareas en el orden original al contenedor
      tasks.forEach(task => {
        tasksContainer.appendChild(task);
      });
    }
  });

  // Función de comparación para ordenar por fecha límite
  function compareDates(a, b) {
    const dateA = new Date(a.dataset.fechaLimite);
    const dateB = new Date(b.dataset.fechaLimite);

    return dateA - dateB;
  }

  // Función de comparación para restaurar el orden original
  function compareOriginalOrder(a, b) {
    return a.dataset.originalOrder - b.dataset.originalOrder;
  }
} 

  

    
    
