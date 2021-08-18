from django.db import models
from speakapi.models import Project, prjDataLabel

# Chart model
class Chart(models.Model):
    CHART_TYPE_CHOICES = (
        ('0', 'Line graph'),
        ('9', 'Heatmap'),
    )
    chartTitle = models.CharField(max_length=50)
    chartType = models.CharField(max_length=2,
                                 choices=CHART_TYPE_CHOICES,
                                 default='0')
    chartDisc = models.CharField(max_length=200, default='')
    chartXaxis = models.CharField(max_length=200, default='')
    chartYaxis = models.CharField(max_length=200, default='')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    def __str__(self):
        return self.chartTitle

class Trace(models.Model):
    traceName = models.CharField(max_length=200)
    chart = models.ForeignKey(Chart, on_delete=models.CASCADE)
    xAxis = models.ForeignKey(prjDataLabel, related_name='xaxis', on_delete=models.CASCADE)
    yAxis = models.ForeignKey(prjDataLabel, related_name='yaxis', on_delete=models.CASCADE)
    def __str__(self):
        return self.traceName
