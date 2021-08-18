from django.contrib import admin
from django.forms import Form, ModelChoiceField
# Register your models here.
from .models import Project, prjDataLabel, prjData

admin.site.register(Project)
#admin.site.register(prjDataLabel, prjDataLabelAdmin)
admin.site.register(prjDataLabel)
'''
class ProjectForm(Form):
    project = ModelChoiceField(
        queryset=Project.objects.all(),
        label=u"Project",
        widget=ModelSelect2Widget(
            model=Project,
            search_fields=['project_name__icontains'],
        )
    )

    label = forms.ModelChoiceField(
        queryset=prjDataLabel.objects.all(),
        label=u"Label",
        widget=ModelSelect2Widget(
            model=prjDataLabel,
            search_fields=['label__icontains'],
            dependent_fields={'project': 'project'},
            max_results=500,
        )
    )

class prjDataAdmin(admin.ModelAdmin):
    form = ProjectForm
'''
admin.site.register(prjData)
