from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from apps.jobs.models import Application, Job
from apps.userprofiles.models import  ConversationMessage

# import utitilities for notification sending 
from apps.notification.utilities import create_notification

@login_required
def dashboard(request):
    return render(request, 'userprofiles/dashboard.html', {'userprofile':request.user.userprofile})


@login_required
def view_application(request, application_id):
    if request.user.userprofile.is_employer:
        application = get_object_or_404(Application, pk=application_id, job__created_by=request.user)
    else:
        application = get_object_or_404(Application, pk=application_id, created_by=request.user)
    
    if request.method == 'POST':
        content = request.POST.get('content')

        if content:
            conversationmessage = ConversationMessage.objects.create(application=application, content=content, created_by=request.user)

            create_notification(request, application.created_by, 'message', extra_id=application.id)

            return redirect('view_application', application_id=application_id)
    
    return render(request, 'userprofiles/view_application.html', {'application': application})

    
@login_required
def view_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id, created_by=request.user)

    return render(request, 'userprofiles/view_job_detail.html', {'job':job})