import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

from flowlance.decorators import role_required
from project.models import ProjectMember

@role_required(['administrator'])
@require_POST
def update_role(request, member_id):
    member = get_object_or_404(ProjectMember, id=member_id)

    data = json.loads(request.body)
    new_role = data.get('role')

    if new_role not in ['administrator', 'member', 'viewer']:
        return JsonResponse({'error': 'Rol inválido.'}, status=400)

    # Actualizar el rol
    member.role = new_role
    member.save()

    return JsonResponse({'message': 'Rol actualizado correctamente.'})
