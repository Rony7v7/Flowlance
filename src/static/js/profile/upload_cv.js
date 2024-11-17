document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.getElementById('file');
    const uploadSuccess = document.getElementById('uploadSuccess');

    fileInput.addEventListener('change', function () {
        if (this.files.length > 0) {
            uploadSuccess.classList.remove('hidden');
            setTimeout(() => {
                uploadSuccess.classList.add('hidden');
            }, 3000); // Ocultar el mensaje después de 3 segundos
        }
    });
});
