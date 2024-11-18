document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('confirmationModal');
    const acceptButton = document.getElementById('acceptButton');
    const uploadSuccess = document.getElementById('uploadSuccess');

    // Leer el valor de registrationSuccessful desde el atributo data- de modal
    const registrationSuccessful = modal.getAttribute('data-registration-successful') === 'true';

    if (registrationSuccessful) {
        modal.classList.remove('hidden');
    }

    acceptButton.addEventListener('click', function() {
        window.location.href = "/dashboard/";
    });

    document.getElementById('id_photo').addEventListener('change', function () {
        if (this.files.length > 0) {
            uploadSuccess.classList.remove('hidden');
            setTimeout(() => {
                uploadSuccess.classList.add('hidden');
            }, 3000);
        }
    });
});
