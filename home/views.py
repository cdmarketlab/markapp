from django.http import HttpResponse
from django.template import loader



def index(request):
    latest_question_list ="Hola Mundo"
    template = loader.get_template('home/home.html')
    context = {
        'entrada': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

