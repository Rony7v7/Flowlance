let url = `ws://${window.location.host}/ws/notifications/${username}`

const notificationsSocket = new WebSocket(url);

notificationsSocket.onmessage = function (e) {
    let data = JSON.parse(e.data)
    console.log('Data: ', data)

    if (data.type === 'new_notification') {
        console.log('Nueva notificación:', data);

        // Obtener el contador de notificaciones
        let notificationCounter = document.getElementById('notification-counter');

        // Actualizar el contador
        let unreadCount = parseInt(notificationCounter.innerText) || 0;
        unreadCount += 1;
        notificationCounter.innerText = unreadCount;

        // Mostrar el contador si está oculto
        if (notificationCounter.classList.contains('hidden')) {
            notificationCounter.classList.remove('hidden');
        }
    }
}
