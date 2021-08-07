from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from apps.jobs.models import Application

@login_required
def dashboard(request):
    return render(request, 'userprofiles/dashboard.html', {'userprofile':request.user.userprofile})


@login_required
def view_application(request, app_id):
    application = get_object_or_404(Application, pk=app_id, created_by=request.user)
    return render(request, 'userprofiles/view_application.html', {'application': application})