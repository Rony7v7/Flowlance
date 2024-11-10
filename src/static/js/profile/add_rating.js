    // JavaScript para manejar la selección de estrellas
    document.querySelectorAll('#starContainer svg').forEach(star => {
        star.addEventListener('click', () => {
            const ratingValue = star.getAttribute('data-value');
            document.getElementById('id_stars').value = ratingValue;

            // Cambia el color de las estrellas según la calificación seleccionada
            document.querySelectorAll('#starContainer svg').forEach(star => {
                const starValue = star.getAttribute('data-value');
                star.classList.remove('text-primary_medium', 'text-primary_dark');
                if (starValue <= ratingValue) {
                    star.classList.add('text-primary_dark');
                } else {
                    star.classList.add('text-primary_lightest');
                }
            });
        });
    });

    // Validación del formulario para asegurarse de que se seleccione una calificación
    document.getElementById('ratingForm').addEventListener('submit', function(e) {
        const stars = document.getElementById('id_stars').value;
        if (stars === '0') {
            e.preventDefault();
            alert('Por favor, seleccione una calificación.');
        }
    });