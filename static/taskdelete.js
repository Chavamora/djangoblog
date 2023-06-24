$(document).ready(function () {
    $('.delete').click(function () {
      var taskId = $(this).data('task-id');
      var csrftoken = Cookies.get('csrftoken');
      var deletedItem = $(this).closest(".item");

      // Mostrar ventana de confirmación
      if (confirm("¿Estás seguro de que deseas eliminar este elemento?")) {
        // Realizar la solicitud AJAX al servidor si se confirma la acción
        $.ajax({
          url: '/tasks/delete/' + taskId + '/',
          type: 'DELETE',
          beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", Cookies.get("csrftoken"));
          },
          data: {
            entry_id: taskId,
          },
  
          success: function (response) {
            console.log(response);
            deletedItem.css("display", "none");
          },
          error: function (xhr, errmsg, err) {
            // Manejo de errores si la solicitud falla
            console.log("ERROR:", errmsg, err, taskId, xhr)
            console.log(xhr.status + ": " + xhr.responseText);
          }
        });
      } else {
        // Anular la transacción si se selecciona "Cancelar"
        console.log("Acción cancelada");
      }
    });
    
  });