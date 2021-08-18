from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Project, prjDataLabel, prjData
import logging
logger = logging.getLogger("mylogger")
# Create your views here.
def index(request):
    project_list = Project.objects.order_by('-create_date')[:5]
    context = {'project_list': project_list}
    return render(request, 'speakapi/index.html', context)

@csrf_exempt
def insert_data(request, project_id):
    api_key = request.GET.get('api_key')
    dataSet = request.GET.getlist('data')
    if api_key is None or dataSet is None:
        return HttpResponse('0')
    project = get_object_or_404(Project, pk=project_id)
    if api_key == project.api_key:
        querySet = []
        if request.method == "POST":
            logger.info(request.POST)
            return HttpResponse(request.POST)
            label, data = request.POST['data'].split(':')
            label = get_object_or_404(prjDataLabel,pk=label)
            prjdata = prjData(data=data, label=label, project=project)
            querySet.append(prjdata)
        else:
            for d in dataSet:
                label, data = d.split(':')
                label = get_object_or_404(prjDataLabel, pk=label)
                prjdata = prjData(data=data, label=label, project=project)
                querySet.append(prjdata)
        prjData.objects.bulk_create(querySet)
        return HttpResponse('1')
    else:
        return HttpResponse('0')

def delete_data(request, project_id, label_id):
    project = get_object_or_404(Project, pk=project_id)
    dataLabel = get_object_or_404(prjDataLabel, pk=label_id, project=project)
    data = prjData.objects.filter(project=project, label=dataLabel)
    if data.exists():
        data._raw_delete(data.db)
    #messages.info(request, 'This series has been emptied.')
    #return redirect('/userpanel/project/%d/series/%d/' % (project_id, label_id))
    return HttpResponse('1')
