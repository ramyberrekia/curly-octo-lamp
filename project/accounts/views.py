from django.shortcuts import render, redirect, reverse
from django.contrib.auth import get_user_model 
from .models import Profile  
from django.contrib.auth import get_user_model
from .forms import UserCreationForm
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import DjangoUnicodeDecodeError, force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import urls
from .tokens import create_token
from project.views import Handler_404
from django.contrib.auth import authenticate, login
# from .forms import RequestEmailActivationForm


User = get_user_model()

def send_activation_email(user, request):
    site = get_current_site(request)
    email_subject = 'Activate your account'
    protocol = 'https' if request.is_secure() else 'http'

    email_body = render_to_string('email/activate.html',{
        'protocol': protocol,
        'user':user,
        'domain': site, 
        'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': create_token.make_token(user)
    })
    send_mail(email_subject,email_body,settings.EMAIL_HOST_USER, [user.email,])


def register(request):
    form = UserCreationForm()

    context = {
        'form': form
    }
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if User.objects.filter(email=request.POST.get('email')).exists():
            messages.error(request, 'This email is used by another user.')
            return render(request, 'registration/register.html', context)

        elif User.objects.filter(username=request.POST.get('username')).exists():
            messages.error(request, 'This email is used by another user.')
            return render(request, 'registration/register.html', context)

        if form.is_valid():
            form.save()
            send_activation_email(form.instance,request)
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            messages.success(request, 'You are currently logged in; You need to activate your email to make activities on the site.')
            return redirect('auth:login')
        else:
            messages.success(request, 'Your registration failed.')


    return render(request, 'registration/register.html', context)


def account_activation(request, uidb64, token):
    try:
        pk = urlsafe_base64_decode(force_str(uidb64))
        user = User.objects.get(pk=pk)
    except Exception as e:
        user= None

    if uidb64 == urlsafe_base64_encode(force_bytes(request.user.pk)):
        if user and create_token.check_token(user, token):
            user.profile.is_activated = True
            user.profile.save()
            messages.success(request,'Your account has been activated.')
            return redirect(reverse('login'))
        elif not user.profile.is_activated:
            messages.error(request,'Something went wrong.')
            render(request, 'email/activate_failed.html')
            if request.method =='POST':
                print('Yo im here')
                send_activation_email(user, request)
        else:
            return redirect(reverse('blog:posts_list'))
    else:
        return Handler_404(request)

    return render(request, 'email/activate_failed.html')



        
    # return render(request, 'email/activation-failed.html', {'user':user})


def activation_failed(request, user):
    if request.method=='POST':
        send_activation_email(user, request)

    return render(request, 'email/activate_failed.html')
