from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User


def registro(request):
    latest_question_list ="Hola Mundo"
    template = loader.get_template('users/register.html')
    context = {
        'entrada': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def nuevoRegistro(request):
    latest_question_list = request.POST["username"]
    print(request.POST)
    template = loader.get_template('users/register.html')
    context = {
        'entrada': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
def validaUser(request):
    u = User.objects.get(username='john')
    return u