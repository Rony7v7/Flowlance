import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

from flowlance.decorators import role_required
from project.models import ProjectMember

# Solo los administradores pueden actualizar roles 
@require_POST
def update_role(request, member_id):
    # Verificar si el usuario tiene permiso para actualizar roles
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'No tienes permiso para hacer esto.'}, status=403)
    
    # Obtener el ProjectMember por ID
    member = get_object_or_404(ProjectMember, id=member_id)

    # Obtener el nuevo rol desde la solicitud
    data = json.loads(request.body)
    new_role = data.get('role')

    # Validar que el nuevo rol sea uno de los permitidos
    if new_role not in ['administrator', 'member', 'viewer']:
        return JsonResponse({'error': 'Rol inválido.'}, status=400)

    # Actualizar el rol
    member.role = new_role
    member.save()

    return JsonResponse({'message': 'Rol actualizado correctamente.'})
