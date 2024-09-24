from django.shortcuts import render, get_object_or_404

from django.contrib import messages

from .models import About,Social,Skill,Education,Experience,Portfolio,Contact,Service

from django.core.mail import send_mail


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        messages.success(request, "Message received! I'll get back to you soon😊")

        # send an email to yourself
        send_mail(
            subject,
            f"Name: {name}\nEmail: {email}\nMessage: {message}",
            email,
            ['wiseangle13@gmail.com'], # your email address
            fail_silently=True,
        )

    about = About.objects.all()
    social = Social.objects.all()
    skills = Skill.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    portfolio = Portfolio.objects.all().order_by('-created_at')
    services = Service.objects.all()
    return render(request, "index.html", {'about': about, 'social': social, 'skills': skills, 'education': education, 'experience': experience, 'portfolio': portfolio, 'services': services})


def portfolio_detail(request, pk):
    portfolio_item = get_object_or_404(Portfolio, pk=pk)
    return render(request, 'portfolio_details.html', {'portfolio_item': portfolio_item})
