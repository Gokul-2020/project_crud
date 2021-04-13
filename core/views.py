from django.shortcuts import render, redirect
from .models import Patient
from datetime import datetime
from django.http.response import JsonResponse
# from django.core import serializers
from django.template.loader import render_to_string


def genForwarder(request):
    return redirect('list-patient')


def createPatient(request):
    context = {}
    if request.method == 'POST':
        try:
            v_first_name = request.POST.get('first_name')
            v_last_name = request.POST.get('last_name')
            v_date_of_birth = datetime.strptime(
                request.POST.get('date_of_birth'), '%m/%d/%Y').date()
            patient_obj, created = Patient.objects.get_or_create(
                first_name=v_first_name, last_name=v_last_name, date_of_birth=v_date_of_birth)
            return redirect('list-patient')
        except:
            return redirect('list-patient')
    return render(request, 'core/add_patient.html', context)


def patientDetails(request):
    if request.method == 'GET':
        try:
            patient_id = request.GET.get('patient_id')
            patient_obj = Patient.objects.get(pk=patient_id)
            context = {}
            context['patient'] = patient_obj
            return render(request, 'core/patient_details.html', context)
        except Patient.DoesNotExist:
            return redirect('list-patient')
    else:
        return redirect('list-patient')


def updatePatient(request):
    if request.method == 'GET':
        try:
            patient_id = request.GET.get('patient_id')
            patient_obj = Patient.objects.get(pk=patient_id)
            context = {}
            context['patient'] = patient_obj
            return render(request, 'core/edit_patient_details.html', context)
        except Patient.DoesNotExist:
            return redirect('list-patient')
    elif request.method == 'POST':
        try:
            patient_id = int(request.POST.get('patient_id'))
            patient_obj = Patient.objects.get(pk=patient_id)
            patient_obj.first_name = request.POST.get('first_name')
            patient_obj.date_of_birth = datetime.strptime(
                request.POST.get('date_of_birth'), '%m/%d/%Y').date()
            patient_obj.gender = request.POST.get('gender')
            patient_obj.save()
            return redirect('list-patient')
        except Patient.DoesNotExist:
            return redirect('list-patient')
    else:
        return redirect('list-patient')


def deletePatient(request):
    if request.method == 'POST':
        try:
            patient_id = int(request.POST.get('patient_id'))
            Patient.objects.get(pk=patient_id).delete()
            return JsonResponse({'status': 'deleted'})
        except Patient.DoesNotExist:
            return JsonResponse({'status': 'failed'})
    return redirect('list-patient')


def listPatient(request):
    context = {}
    context['patient_list'] = Patient.objects.all().order_by('first_name')
    return render(request, 'core/list_patients.html', context)


def getPatientsList(request):
    if request.method == 'GET':
        context = {}
        context['patient_list'] = Patient.objects.all().order_by('first_name')
        html = render_to_string('core/patient_table.html', context, request=request)
        return JsonResponse({'table_html': html})
