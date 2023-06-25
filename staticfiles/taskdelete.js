$(document).ready(function () {
    $('.item_options').on('click', '.delete', function (e) {
      var taskId = $(e.target).data('task-id');
      var csrftoken = Cookies.get('csrftoken');
      var item = $(this).closest('.item');
      var optionsItem = $(this).closest('.item').find('.item_options');
      var checkbox = $(this).closest('.item').find('.options_checkbox');

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
            item.remove();
            if($('#generalTasks').children().length === 0) {
              $('#generalTasks').remove();
              $('#generalTasks-h1').remove();
              $('.item_list').append('<p>Aun no tienes ninguna tarea, haz click en "+" para agregar una! </p>')
            }
            
            
            if($('#completed-tasks').children().length === 0) {
              $('#completed-tasks').remove();
              $('#completed-tasks-h1').remove();
            }
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