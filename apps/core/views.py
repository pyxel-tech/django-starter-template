from shared.logger import create_log
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def dashboard(request):
    """Carrega uma tela de acordo com o nível do usuário"""
    user = request.user
    create_log(f'Usuário {user} acessou a plataforma', 'warning')
    if user.is_superuser:
        return render(request, 'core/admin_dashboard.html')
    else:
        return render(request, 'core/user_dashboard.html')
