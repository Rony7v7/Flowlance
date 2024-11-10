let ratingId; // Variable para almacenar el ID de la calificación
let responseId; // Variable para almacenar el ID de la respuesta en caso de edición

// Abre el modal para crear una nueva respuesta
function openResponseModal(id) {
    ratingId = id; 
    document.getElementById('responseModal').classList.remove('hidden');
    document.getElementById('id_response_text').value = ''; // Limpiar campo de texto
}

// Abre el modal para editar una respuesta existente
function openEditResponseModal(id) {
    responseId = id;
    document.getElementById('responseModal').classList.remove('hidden');
    
    // Rellenar el textarea con la respuesta existente
    fetch(`/profile/get_rating_response/${responseId}/`, {
        method: 'GET',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
        }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('id_response_text').value = data.response_text;
    })
    .catch(error => console.error('Error al obtener la respuesta:', error));
}

// Cierra el modal de respuesta
function closeResponseModal() {
    document.getElementById('responseModal').classList.add('hidden');
}

// Manejador del formulario de respuesta (para crear o editar)
document.getElementById('responseForm').addEventListener('submit', function (event) {
    event.preventDefault();
    const formData = new FormData(this);

    const url = responseId 
        ? `/profile/edit_rating_response/${responseId}/`  // URL de edición
        : `/profile/add_rating_response/${ratingId}/`;   // URL de creación

    fetch(url, {
        method: 'POST',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': '{{ csrf_token }}',
        },
        body: formData
    })
    .then(response => {
        if (response.ok) {
            closeResponseModal();
            location.reload();
        } else {
            return response.json();
        }
    })
    .then(data => {
        if (data && data.errors) {
            alert('Error al enviar la respuesta: ' + JSON.stringify(data.errors));
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Ha ocurrido un error. Intenta nuevamente.');
    });
});

// Manejador del formulario de calificación
document.getElementById('ratingForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const stars = document.getElementById('id_stars').value;
    if (stars < 1) {
        alert("Debes seleccionar al menos 1 estrella.");
        return;
    }

    const formData = new FormData(this);

    fetch("{% url 'add_rating' request.profile.user.username %}", {
        method: 'POST',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': '{{ csrf_token }}',  
        },
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            closeRatingModal();
            location.reload();
        } else if (data.errors) {
            alert('Error al enviar la calificación: ' + JSON.stringify(data.errors));
        }
    })
    .catch(error => console.error('Error:', error));
});

// Cierra el modal de calificación
function closeRatingModal() {
    document.getElementById('ratingModal').classList.add('hidden');
}

function openRatingModal() {
    document.getElementById('ratingModal').classList.remove('hidden');
    document.getElementById('id_stars').value = '0';  // Resetear la selección de estrellas
    resetStars();
}

function resetStars() {
    document.querySelectorAll('#starContainer svg').forEach(star => {
        star.classList.remove('text-primary_dark');
        star.classList.add('text-primary_lightest');
    });
}

function setRating(ratingValue) {
    // Guardar el valor de las estrellas seleccionadas en el input oculto
    document.getElementById('id_stars').value = ratingValue;

    // Resetear todas las estrellas al color claro
    document.querySelectorAll('#starContainer svg').forEach(star => {
        star.classList.remove('text-primary_dark');
        star.classList.add('text-primary_lightest');
    });

    // Cambiar el color de todas las estrellas hasta la seleccionada
    for (let i = 1; i <= ratingValue; i++) {
        document.getElementById(`star-${i}`).classList.remove('text-primary_lightest');
        document.getElementById(`star-${i}`).classList.add('text-primary_dark');
    }
}

function toggleDropdown() {
    const dropdownMenu = document.getElementById("dropdownMenu");
    dropdownMenu.classList.toggle("hidden");
}

window.addEventListener("click", function(e) {
    const dropdownMenu = document.getElementById("dropdownMenu");
    if (!e.target.closest(".relative")) {
        dropdownMenu.classList.add("hidden");
    }
});