from django import forms
from dataviewer.models import Chart, Trace
from speakapi.models import Project, prjDataLabel

class PrjForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'project_disc', ]
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control'}),
            'project_disc': forms.TextInput(attrs={'class': 'form-control'}),
        }

class chartForm(forms.ModelForm):
    class Meta:
        model = Chart
        fields = ['chartTitle', 'chartType', 'chartDisc', 'chartXaxis', 'chartYaxis']
        widgets = {
            'chartTitle': forms.TextInput(attrs={'class': 'form-control'}),
            'chartType': forms.Select(attrs={'class': 'form-control'}),
            'chartDisc': forms.TextInput(attrs={'class': 'form-control'}),
            'chartXaxis': forms.TextInput(attrs={'class': 'form-control'}),
            'chartYaxis': forms.TextInput(attrs={'class': 'form-control'}),
        }

class traceForm(forms.ModelForm):
    class Meta:
        model = Trace
        fields = ['traceName', 'xAxis', 'yAxis']
        widgets = {
            'traceName': forms.TextInput(attrs={'class': 'form-control'}),
            'xAxis': forms.Select(attrs={'class': 'form-control'}),
            'yAxis': forms.Select(attrs={'class': 'form-control'}),
        }
    def __init__(self, project, *args, **kwargs):
        super(traceForm, self).__init__(*args, **kwargs)
        self.fields['xAxis'].queryset = prjDataLabel.objects.filter(project=project)
        self.fields['yAxis'].queryset = prjDataLabel.objects.filter(project=project)

class seriesForm(forms.ModelForm):
    class Meta:
        model = prjDataLabel
        fields = ['label']
