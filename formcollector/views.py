from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import DataEntryForm
from .utils import get_email_settings

def form_view(request):
    if request.method == 'POST':
        form = DataEntryForm(request.POST)
        if form.is_valid():
            entry = form.save()
            
            # Get dynamic email settings
            email_settings = get_email_settings()
            
            # Email content
            subject = 'New Form Submission Received'
            message = f"""
            New form submission details:
            
            First Field: {entry.first_field}
            Second Field: {entry.second_field}
            Submitted at: {entry.timestamp}
            """
            
            # Send email using dynamic settings
            send_mail(
                subject,
                message,
                email_settings['EMAIL_HOST_USER'],
                [email_settings['EMAIL_HOST_USER']],
                fail_silently=False,
            )
            
            return redirect('success')
    else:
        form = DataEntryForm()
    
    return render(request, 'formcollector/form.html', {'form': form})

def success_view(request):
    return render(request, 'formcollector/success.html')
