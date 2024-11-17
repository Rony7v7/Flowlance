document.addEventListener('DOMContentLoaded', function () {
    const csrfToken = document.getElementById('csrfToken').value;

    // Función para actualizar el rol del miembro
    function updateRole(memberId, newRole) {
        fetch(`/project/update_role/${memberId}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
            },
            body: JSON.stringify({ role: newRole })
        }).then(response => {
            if (!response.ok) {
                alert('Error al actualizar el rol.');
            }
        });
    }

    // Función para eliminar un miembro del proyecto
    function deleteMember(memberId) {
        if (confirm("¿Estás seguro de eliminar a este miembro del proyecto?")) {
            fetch(`/project/delete_member/${memberId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken,
                },
            })
            .then(response => {
                if (response.ok) {
                    location.reload();
                } else {
                    alert('Error al eliminar al miembro.');
                }
            });
        }
    }

    // Asignar eventos a los elementos
    document.querySelectorAll('.role-select').forEach(select => {
        select.addEventListener('change', function () {
            updateRole(this.dataset.memberId, this.value);
        });
    });

    document.querySelectorAll('.delete-button').forEach(button => {
        button.addEventListener('click', function () {
            deleteMember(this.dataset.memberId);
        });
    });
});
