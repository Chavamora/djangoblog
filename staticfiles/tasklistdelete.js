$(document).ready(function () {
    $('.delete-icon').click(function () {
      var entryId = $(this).data('entry-id');
      var csrftoken = Cookies.get('csrftoken');
      var deletedItem = $(this).closest(".item");

      // Mostrar ventana de confirmación
      if (confirm("¿Estás seguro de que deseas eliminar este elemento?")) {
        // Realizar la solicitud AJAX al servidor si se confirma la acción
        $.ajax({
          url: '/tasks/tasklist/delete/' + entryId + '/',
          type: 'DELETE',
          beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", Cookies.get("csrftoken"));
          },
          data: {
            entry_id: entryId,
          },
  
          success: function (response) {
            console.log(response);
            deletedItem.remove()
            deletedItem.css("display", "none");
            
            if($('#completed-tasks').children().length === 0) {
              $('#completed-tasks').remove();
              $('#completed-tasks-h1').remove();
              
            }
          },
          error: function (xhr, errmsg, err) {
            // Manejo de errores si la solicitud falla
            console.log("ERROR:", errmsg, err, entryId, xhr)
            console.log(xhr.status + ": " + xhr.responseText);
          }
        });
      } else {
        // Anular la transacción si se selecciona "Cancelar"
        console.log("Acción cancelada");
      }
    });
    
  });