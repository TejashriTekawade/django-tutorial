from django.urls import path

# . means isi folder se 
from .import views

urlpatterns = [
    path('',views.index, name="index"),
    path('job',views.job, name="job"),
    path('jobtemplate',views.jobtemplate, name="jobtemplate")
]
