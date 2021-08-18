import json
from time import sleep
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, StreamingHttpResponse
from speakapi.models import Project, prjDataLabel, prjData
from .models import Chart, Trace
# Create your views here.
#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    project_list = Project.objects.order_by('-create_date')
    context = {'project_list': project_list}
    return render(request, 'dataviewer/index.html', context)

def project_view(request, pid):
    #Load project information
    project = get_object_or_404(Project, pk=pid)
    #Load data set
    dataLabels = prjDataLabel.objects.filter(project_id=pid)
    #dataSet = {}
    #for label in dataLabels:
    #    dataSet[label.label] = prjData.objects.values_list('data', 'id').filter(project_id=pid, label_id=label.id).order_by('id')[:2000]
    #Load chart information
    charts = Chart.objects.filter(project_id=pid)
    chartSet = {}
    for chart in charts:
        chartSet[chart.chartTitle] = [chart.chartType, chart.chartDisc, chart.chartXaxis, chart.chartYaxis, list(Trace.objects.filter(chart_id=chart.id).values())]
    return render(request, 'dataviewer/viewer_new.html', {'project': project, 'series_set': dataLabels, 'chart_set': chartSet, 'charts': charts})

def getData(request):
    data_id = request.POST.get('data_id')
    label_id = request.POST.get('label_id')
    if data_id is None and label_id is None:
        return HttpResponse('Data error!')
    elif data_id is None or label_id == '0':
        Data = prjData.objects.filter(label_id=label_id)[5000]
        if len(Data) > 0:
            newDataLength = 1
        else:
            newDataLength = 0
    else:
        Data = prjData.objects.filter(label_id=label_id, id__gt=data_id)[:5000]
        newDataLength = len(Data)
    if newDataLength > 0:
        returnData = {}
        newData = list(Data.values('id', 'data', 'insert_date'))
        for data in newData[0].keys():
            returnData[data] = tuple(returnData[data] for returnData in newData)
        return JsonResponse(returnData, safe=False)
        #return StreamingHttpResponse(returnData)
    else:
        return HttpResponse(0)
