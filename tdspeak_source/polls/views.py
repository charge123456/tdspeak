from django.shortcuts import render
from django.http import HttpResponse
from speakapi.models import Project, prjDataLabel, prjData
# Create your views here.
#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    project_list = Project.objects.order_by('-create_date')[:5]
    context = {'project_list': project_list}
    return render(request, 'polls/index.html', context)
