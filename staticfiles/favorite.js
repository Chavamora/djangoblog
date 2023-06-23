
$(document).ready(function () {
  $('.star-icon').click(function () {
    var entryId = $(this).data('entry-id');
    var csrftoken = Cookies.get('csrftoken');
    console.log('hola', entryId)
    // Realizar la solicitud AJAX al servidor
    $.ajax({
      url: '/dairy/favorite/' + entryId + '/',  // Reemplaza con la URL de tu vista Django para marcar como favorito
      type: 'POST',
      data: {
        entry_id: entryId,
        csrfmiddlewaretoken: csrftoken // Asegúrate de incluir esto para protección CSRF en Django
      },

      success: function (response) {
        var icons = document.querySelectorAll(".star-icon");
        icons.forEach(function (icon) {
          console.log(icon);
          var iconEntryId = icon.dataset.entryId;
          console.log(iconEntryId);
          if (iconEntryId == entryId) {
            var isFavorite = icon.classList.contains("favorite");

            if (isFavorite) {
              icon.classList.remove("favorite");
            } else {
              icon.classList.add("favorite");
            }
          }
        })


        console.log(response);
      },
      error: function (xhr, errmsg, err) {
        // Manejo de errores si la solicitud falla
        console.log("ERROR:", errmsg, err, entryId, xhr)
        console.log(xhr.status + ": " + xhr.responseText);
      }
    });
  });
});






