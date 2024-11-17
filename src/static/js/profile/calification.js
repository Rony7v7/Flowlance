    // Capturar los clics en los botones de estrellas y asignar el valor al campo oculto
    document.querySelectorAll("button[id^='star-']").forEach(button => {
        button.addEventListener('click', function() {
            // Extraer el número de estrellas del ID del botón
            const rating = this.id.split('-')[1];
            // Asignar el valor al campo oculto
            document.getElementById('selected-rating').value = rating;
            // Cambiar el color del botón seleccionado
            document.querySelectorAll("button[id^='star-']").forEach(btn => btn.classList.remove('bg-green-500'));
            this.classList.add('bg-green-500');
        });
    });