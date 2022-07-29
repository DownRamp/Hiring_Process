from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from HireApp.models import Jobs,Applicants
from HireApp.serializers import JobsSerializer,ApplicantsSerializer

from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def jobApi(request,id=0):
    if request.method=='GET':
        jobs = Jobs.objects.all()
        jobs_serializer=JobsSerializer(jobs,many=True)
        return JsonResponse(jobs_serializer.data,safe=False)

    elif request.method=='POST':
        job_data=JSONParser().parse(request)
        jobs_serializer=JobsSerializer(data=job_data)
        if jobs_serializer.is_valid():
            jobs_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

    elif request.method=='PUT':
        job_data=JSONParser().parse(request)
        job=Jobs.objects.get(JobsId=job_data['JobsId'])
        jobs_serializer=JobsSerializer(job,data=job_data)
        if jobs_serializer.is_valid():
            jobs_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")

    elif request.method=='DELETE':
        job=Jobs.objects.get(JobsId=id)
        job.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def applicantApi(request,id=0):
    if request.method=='GET':
        applicants = Applicants.objects.all()
        applicants_serializer=ApplicantsSerializer(applicants,many=True)
        return JsonResponse(applicants_serializer.data,safe=False)
    elif request.method=='POST':
        applicant_data=JSONParser().parse(request)
        applicants_serializer=ApplicantsSerializer(data=applicant_data)
        if applicants_serializer.is_valid():
            applicants_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        applicant_data=JSONParser().parse(request)
        applicant=Applicants.objects.get(ApplicantsId=applicant_data['ApplicantsId'])
        applicants_serializer=ApplicantsSerializer(applicant,data=applicant_data)
        if applicants_serializer.is_valid():
            applicants_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        applicant=Applicants.objects.get(ApplicantsId=id)
        applicant.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)