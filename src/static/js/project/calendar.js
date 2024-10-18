$(document).ready(function() {
    var projectId = projectId;  // projectId ya viene desde el script en la plantilla HTML
    
    var calendar = $('#calendar').fullCalendar({
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,agendaWeek,agendaDay'
        },
        events: function(start, end, timezone, callback) {
            $.ajax({
                url: '/all_events/',
                dataType: 'json',
                data: {
                    project_id: projectId  // Pasamos el projectId como parámetro
                },
                success: function(data) {
                    callback(data);  // Muestra los eventos en el calendario
                }
            });
        }
    });
});
