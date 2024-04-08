from django.shortcuts import render  # pylint: disable=unused-import
from django.http import HttpResponse
from .models import Job # pylint: disable=unused-import
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):  # pylint: disable=unused-argument
    return HttpResponse("Hello, welcome to my portfolio")

@csrf_exempt
def jobtemplate(request):

    if request.method == "GET":  
        jobsasd = Job.objects.all()
        return render(request,"portfolio/index.html",{'jobsasd':jobsasd})
    
def job(request):
    if request.method == "GET":
        result = []

        jobs = Job.objects.all()
        for job in jobs:
            data={
                "company" : job.company,
                "description" : job.description
            }
            result.append(data)
            
        return HttpResponse(json.dumps(result))

    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        company = data['company']
        description = data['description']

        job = Job(company = company, description = description)
        job.save()
        return HttpResponse({"company  added successfully"})
    
    if request.method == "DELETE":
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        company = data['company']        

        job = Job.objects.filter(company=company).delete()
        return HttpResponse({"company  deleted successfully"})      

