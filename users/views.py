from django.http import HttpResponse
from django.template import loader



def registro(request):
    latest_question_list ="Hola Mundo"
    template = loader.get_template('users/register.html')
    context = {
        'entrada': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def nuevoRegistro(request):
    latest_question_list = request.POST["username"]
    print(latest_question_list)
    template = loader.get_template('home/home.html')
    context = {
        'entrada': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
