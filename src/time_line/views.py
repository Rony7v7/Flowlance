from django.shortcuts import render, get_object_or_404
from .models import Freelancer, Calificacion

def calificar_freelancer(request, freelancer_id):
    # Obtener el freelancer a calificar
    freelancer = get_object_or_404(Freelancer, id=freelancer_id)
    selected_rating = None  # Para almacenar la calificación seleccionada
    mensaje = None  # Para el mensaje de confirmación
    
    # Manejar el envío de estrellas o del comentario
    if request.method == 'POST':
        # Obtener las estrellas seleccionadas del formulario
        estrellas = request.POST.get('estrellas')
        comentario = request.POST.get('descripcion')

        # Si se seleccionaron estrellas, actualiza el valor en la vista
        if estrellas:
            selected_rating = int(estrellas)  # Guardamos la selección en la variable
            
            # Si también se envió un comentario, guarda la calificación completa
            if comentario:
                # Guardar la calificación en la base de datos
                Calificacion.objects.create(
                    freelancer=freelancer,
                    user=request.user,  # El usuario que está calificando
                    estrellas=selected_rating,
                    comentario=comentario
                )
                mensaje = "¡Tu calificación ha sido guardada con éxito!"  # Mensaje de éxito

    # Renderizar la plantilla con la calificación seleccionada (si existe) y el mensaje de éxito
    return render(request, 'time_line/calificacion.html', {
        'freelancer': freelancer,
        'selected_rating': selected_rating,  # Pasar la calificación seleccionada a la plantilla
        'mensaje': mensaje  # Pasar el mensaje de éxito
    })
