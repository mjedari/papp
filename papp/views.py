
from django.http import HttpResponse
from django.template import loader


def about(request):
    return HttpResponse("about")

def index(request):
    template = loader.get_template('index.html')
    context = {
        'status': 'HI',
    }
    return HttpResponse(template.render(context, request))