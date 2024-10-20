document.addEventListener('DOMContentLoaded', function() {
    // The 'events' variable will be passed dynamically from the template
    $('#calendar').fullCalendar({
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,agendaWeek,agendaDay'
        },
        events: calendarEventsUrl,  // Use the dynamic URL passed from the template
        selectable: true,  // Allow date selection
        selectHelper: true,
        select: function(start, end) {
            // Open the modal to add a new event
            openModal();
            
            // Set the selected dates in the form fields
            $('#id_start_time').val(start.format('YYYY-MM-DDTHH:mm:ss'));
            $('#id_end_time').val(end.format('YYYY-MM-DDTHH:mm:ss'));
        },
        editable: true,  // Allow event dragging and resizing if necessary

        // Function to open the edit modal when an event is clicked
        eventClick: function(event) {
            openEditModal(event);  // Open the edit modal
        },
    });

    // Submit the new event form via AJAX
    $('#eventForm').on('submit', function(e) {
        e.preventDefault();  // Prevent the default form submission
        
        $.ajax({
            type: 'POST',
            url: window.location.href,  // Use the current URL to submit the form
            data: $(this).serialize(),  // Serialize the form data
            success: function(response) {
                closeModal();  // Close the modal if successful
                $('#calendar').fullCalendar('refetchEvents');  // Refetch the events from the server
            },
            error: function(response) {
                console.log(response.responseJSON.errors);  // Log errors to the console
            }
        });
    });

    // Submit the edit event form via AJAX
    $('#editEventForm').on('submit', function(e) {
        e.preventDefault();

        var eventId = $('#edit_event_id').val();
        var url = '/edit_event/' + eventId + '/';  // Add the trailing slash

        $.ajax({
            type: 'POST',
            url: url,
            data: $(this).serialize(),
            success: function(response) {
                closeEditModal();
                $('#calendar').fullCalendar('refetchEvents');  // Refetch the events from the server
            },
            error: function(response) {
                console.log(response.responseJSON.errors);
            }
        });
    });

    // Functions to open and close the edit modal
    function openEditModal(event) {
        $('#edit_name').val(event.title);
        $('#edit_start_time').val(moment(event.start).format('YYYY-MM-DDTHH:mm:ss'));
        $('#edit_end_time').val(moment(event.end).format('YYYY-MM-DDTHH:mm:ss'));
        $('#edit_description').val(event.description);
        $('#edit_event_id').val(event.id);  // Set the event ID for editing
        $('#editEventModal').removeClass('hidden');
    }

    function closeEditModal() {
        $('#editEventModal').addClass('hidden');
    }

    // Close the edit modal when the "X" is clicked
    $('.close-edit-modal').on('click', function() {
        closeEditModal();
    });

    // Functions to handle the add event modal
    function openModal() {
        document.getElementById("customModal").classList.remove("hidden");
    }

    function closeModal() {
        document.getElementById("customModal").classList.add("hidden");
    }

    // Close the add event modal when clicking outside the content
    window.onclick = function(event) {
        if (event.target == document.getElementById("customModal")) {
            closeModal();
        } else if (event.target == document.getElementById("editEventModal")) {
            closeEditModal();
        }
    }
});
