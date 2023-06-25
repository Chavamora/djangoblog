$(document).ready(function () {
    
    $('.item_options').on('click', '.completada',function (e) {
        
        var taskId = $(e.target).data('task-id');
        console.log(taskId)
        var csrftoken = Cookies.get('csrftoken');
        var item = $(this).closest('.item');
        var optionsItem = $(this).closest('.item').find('.item_options');

        var checkbox = $(this).closest('.item').find('.options_checkbox');
        urgencia = $(this).closest('.item').find('h2[name="urgencia"]');
        
        console.log('boton que dice completada')
        
            console.log('completada')
            $.ajax({
                type: 'POST',
                url: '/tasks/completed',
                data: {
                    'task_id': taskId,
                    'csrfmiddlewaretoken': csrftoken
                },
                success: function (response) {
    
                    if (response.success) {
                        if($('#completed-tasks').length === 0) {
                           
                            $('.tasks').append(`<h1 id="completed-tasks-h1">Tareas Completadas</h1>`)
                            $('.tasks').append(`<div id="completed-tasks" class="item_group" > </div>`)
                            
                        }
                        
                        console.log(item)
                        var updatedStatus = response.status;
    
                        if (updatedStatus == "completada") {
                            item.detach().appendTo('#completed-tasks').fadeIn();
                            urgencia.detach();
                            checkbox.prop("checked", false)
                            optionsItem.removeClass('mostrar');
                            optionsItem.removeClass('fade-in');
                            optionsItem.addClass('fade-out');
                            optionsItem.html(`<div class="optionsLinks">
                            <button data-task-id="${taskId}" class="pendiente">marcar como pendiente</button>
                            <button data-task-id="${taskId}" class="delete">eliminar</button>
                        </div>`);
                                optionsItem.css('display', 'none');
                        } 
                    }
                    
    
                },
                error: function (xhr, textStatus, errorThrown) {
                    console.log('Error:', errorThrown);
                }
            });
        
            
        
    });

    $('.item_options').on('click', '.pendiente',function (e) {
        console.log(e)
        var taskId = $(e.target).data('task-id');
        var csrftoken = Cookies.get('csrftoken');
        var item = $(this).closest('.item');
        var optionsItem = $(this).closest('.item').find('.item_options');
        var checkbox = $(this).closest('.item').find('.options_checkbox');

        console.log('boton que dice pendiente', taskId)

       
            $.ajax({
                type: 'POST',
                url: '/tasks/pending',
                data: {
                    'task_id': taskId,
                    'csrfmiddlewaretoken': csrftoken
                },
                success: function (response) {
                    
                    if (response.success) {
                        console.log('pendiente', response.urgencia)
                        urgencia = response.urgencia;
                        var updatedStatus = response.status;
                        console.log($('#completed-tasks'))
                        
                        if (updatedStatus == "pendiente") {
                            item.detach().appendTo('#generalTasks').fadeIn();
                            checkbox.prop("checked", false)
                            optionsItem.removeClass('mostrar');
                            optionsItem.removeClass('fade-in');
                            optionsItem.addClass('fade-out');
                            optionsItem.css('display', 'none');
                            optionsItem.closest('.item').find('.item_header').prepend(`<h2 name="urgencia" class="${urgencia}"> ${urgencia} </h2>`)
                            optionsItem.html(`<div class="optionsLinks">
                            <button data-task-id="${taskId}" class="completada">marcar como completada</button>
                            <button data-task-id="${taskId}" class="delete">eliminar</button>
                        </div>`);
                        } 
                        
                    }
                    if($('#completed-tasks').children().length === 0) {
                        $('#completed-tasks').remove();
                        $('#completed-tasks-h1').remove();
                    }
                },
                error: function (xhr, textStatus, errorThrown) {
                    console.log('Error:', errorThrown);
                }
            });
        
    });

    var optionsCheckboxList = document.querySelectorAll('.options_checkbox');
    optionsCheckboxList.forEach(optionsCheckbox => {
        optionsCheckbox.addEventListener('click', function () {
            var checkbox = $(this)
            var optionsItem = checkbox.closest('.item').find('.item_options');

            console.log(this.closest('.item'))
            if (optionsItem.hasClass('mostrar')) {
                optionsItem.removeClass('fade-in');
                optionsItem.addClass('fade-out');
                setTimeout(function () {
                    optionsItem.css('display', 'none');
                }, 300);
            } else {
                optionsItem.removeClass('fade-out');
                optionsItem.addClass('fade-in');
                optionsItem.css('display', 'block')
            }
            optionsItem.toggleClass('mostrar');
        });
    });
});
