from email.message import EmailMessage
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings



def home(request):
    if request.method == 'POST':
        name = request.POST.get('contactName')
        hr_email = request.POST.get('contactEmail')  # HR's email
        subject = request.POST.get('contactSubject', 'No Subject')
        message = request.POST.get('contactMessage')

        email_subject = f"New Contact Form Submission: {subject}"
        email_body = f"Name: {name}\nEmail: {hr_email}\n\nMessage:\n{message}"

        recipient_email = "ashwinthsudha2003@gmail.com" 

        email = EmailMessage(
            subject=email_subject,
            body=email_body,
            from_email=hr_email,  # ✅ HR's email as "From"
            to=[recipient_email],
        )

        try:
            email.send(fail_silently=False)
            return redirect('/')
        except Exception as e:
            print(f"Email sending failed: {e}")

    return render(request, "portfolio.html")

