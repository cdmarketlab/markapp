from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import View

def registro(request):
    latest_question_list ="Hola Mundo"
    template = loader.get_template('users/register.html')
    context = {
        'entrada': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def nuevoRegistro(request):
    template_name = 'users/register.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        print(password)
#        user = User.objects.create_user(
#            username=email,
#            email=email,
#            password=password,
#            is_active=False
#        )
#        user.save()
        current_site = get_current_site(request)
        subject = 'Activa tu cuenta'
        message = render_to_string('activacion_cuenta_email.html', {
            'user': email,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(email)),
            'token': default_token_generator.make_token(email),
        })
        from_email = 'info@marketlab.tech'
        to_email = "ahsangeles@gmail.com"
        send_mail(subject, message, from_email, [to_email], fail_silently=False)
        messages.success(request, 'Se ha enviado un correo electrónico de confirmación. Por favor, revisa tu correo para activar tu cuenta.')
        return 0
@csrf_exempt
def valida_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        existe = User.objects.filter(email=email).exists()
        data = {
            'existe': existe
        }
        print(existe)
        return JsonResponse(data)