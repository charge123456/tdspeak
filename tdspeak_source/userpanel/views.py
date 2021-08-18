import uuid
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from speakapi.models import Project, prjDataLabel, prjData
from dataviewer.models import Chart, Trace

# Create your views here.
@login_required
def index(request):
    project_list = Project.objects.filter(project_creator=request.user.id).order_by('-create_date')
    form = PrjForm()
    context = {'project_list': project_list, 'form': form}
    return render(request, 'userpanel/index.html', context)

@login_required
def newProject(request):
    if request.method == 'POST':
        form = PrjForm(request.POST)
        if form.is_valid():
            #Generate the apikey and check is it exist
            while True:
                new_apikey = uuid.uuid4()
                checkApikey = Project.objects.filter(api_key=new_apikey)
                if len(checkApikey) == 0:
                    break
            form = form.save(commit=False)
            form.api_key = new_apikey
            form.project_creator = request.user
            form.save()
            return redirect('/userpanel/')
    form = PrjForm()
    return render(request, 'userpanel/create.html', {'form': form})

@login_required
def prjDetail(request, project_id):
    project = get_object_or_404(Project, pk=project_id, project_creator=request.user)
    charts = Chart.objects.filter(project=project_id).order_by('id')
    series = prjDataLabel.objects.filter(project=project_id).order_by('id')
    form = PrjForm(request.POST or None, instance=project)
    newChartForm = chartForm()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/userpanel/project/%d/' % project_id)
    context = {'project': project, 'form': form, 'chartForm': newChartForm, 'charts': charts, 'series': series}
    return render(request, 'userpanel/project.html', context)

@login_required
def newChart(request, project_id):
    project = get_object_or_404(Project, pk=project_id, project_creator=request.user)
    if request.method == 'POST':
        form = chartForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.project_id = project_id
            form.save()
            return redirect('/userpanel/project/%d' % project_id)
    form = chartForm()
    return render(request, 'userpanel/create.html', {'form': form})

@login_required
def chartDetail(request, project_id, chart_id):
    project = get_object_or_404(Project, pk=project_id, project_creator=request.user)
    chart = get_object_or_404(Chart, pk=chart_id, project=project)
    traces = Trace.objects.filter(chart=chart).order_by('id')
    form = chartForm(request.POST or None, instance=chart)
    blankTraceForm = traceForm(project)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.info(request, 'Update success!')
            return redirect('/userpanel/project/%d/chart/%d/' % (project_id, chart_id))
        else:
            messages.info(request, 'Update error!')
            return redirect('/userpanel/project/%d/chart/%d/' % (project_id, chart_id))
    context = {'chart': chart, 'traces': traces, 'form': form, 'traceForm': blankTraceForm}
    return render(request, 'userpanel/chart.html', context)

@login_required
def newTrace(request, project_id, chart_id):
    project = get_object_or_404(Project, pk=project_id, project_creator=request.user)
    chart = get_object_or_404(Chart, pk=chart_id, project=project)
    if request.method == 'POST':
        form = traceForm(project, request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.chart_id = chart_id
            form.save()
            return HttpResponse(1)
            #return redirect('/userpanel/project/%d/chart/%d/' % (project_id, chart_id))
    form = traceForm(project)
    return render(request, 'userpanel/create.html', {'form': form, 'chart': chart})

@login_required
def traceDetail(request, project_id, chart_id, trace_id):
    project = get_object_or_404(Project, pk=project_id, project_creator=request.user)
    chart = get_object_or_404(Chart, pk=chart_id, project=project)
    trace = get_object_or_404(Trace, pk=trace_id, chart=chart)
    form = traceForm(project, request.POST or None, instance=trace)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.info(request, 'Update success!')
            return redirect('/userpanel/project/%d/chart/%d/trace/%d/' % (project_id, chart_id, trace_id))
        else:
            messages.info(request, 'Update error!')
            return redirect('/userpanel/project/%d/chart/%d/trace/%d/' % (project_id, chart_id, trace_id))
    context = {'trace': trace, 'form': form, 'chartType': chart.chartType}
    return render(request, 'userpanel/trace.html', context)

@login_required
def newSeries(request, project_id):
    project = get_object_or_404(Project, pk=project_id, project_creator=request.user)
    if request.method == 'POST':
        form = seriesForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.project_id = project_id
            form.save()
            return redirect('/userpanel/project/%d/' % project_id)
    form = seriesForm()
    return render(request, 'userpanel/create.html', {'form': form})

@login_required
def seriesDetail(request, project_id, series_id):
    project = get_object_or_404(Project, pk=project_id, project_creator=request.user)
    series = get_object_or_404(prjDataLabel, pk=series_id, project=project)
    form = seriesForm(request.POST or None, instance=series)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.info(request, 'Update success!')
            return redirect('/userpanel/project/%d/series/%d/' % (project_id, series_id))
        else:
            messages.info(request, 'Update error!')
            return redirect('/userpanel/project/%d/series/%d/' % (project_id, series_id))
    context = {'series': series, 'form': form, 'project': project}
    return render(request, 'userpanel/series.html', context)
