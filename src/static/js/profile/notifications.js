function markNotificationsAsRead() {
    // Completar funcionalidad para marcar todas las notificaciones como leídas
    //ya existe el endpoint falta es hacer la logica para llamarlo
}

// JavaScript para abrir y cerrar el modal
document.getElementById('showModal').addEventListener('click', function () {
    document.getElementById('notificationsModal').classList.remove('hidden');
});

document.getElementById('closeModal').addEventListener('click', function () {
    document.getElementById('notificationsModal').classList.add('hidden');
});