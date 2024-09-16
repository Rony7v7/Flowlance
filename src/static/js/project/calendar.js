
document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');

    // Inicializar el calendario
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'timeGridWeek', // Vista inicial del calendario
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay'
        },
        buttonText: {
            today: 'Hoy',
            month: 'Mes',
            week: 'Semana',
            day: 'Día',
        },
        events: [
            {
                title: 'Evento 1',
                start: '2024-09-15',
                end: '2024-09-16'
            },
            {
                title: 'Evento 2',
                start: '2024-09-20'
            }
        ],
          eventContent: function (arg) {
            // Create custom HTML for events
            let italicEl = document.createElement('div');
            italicEl.innerHTML = '<b>' + arg.event.title + '</b><br><i>Details here</i>';

            let arrayOfDomNodes = [italicEl]
            return { domNodes: arrayOfDomNodes }
        },

        eventColor: '#378006',    // Change default event color
    });

    // Renderizar el calendario
    calendar.render();
});