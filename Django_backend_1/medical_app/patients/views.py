from django.shortcuts import render, redirect
from .models import Patient, HealthRecord

def register_patient(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = int(request.POST.get('age'))
        gender = request.POST.get('gender')
        patient = Patient.objects.create(name=name, age=age, gender=gender)
        return redirect('health_record', patient_id=patient.id)

    return render(request, 'patients/register_patient.html')

def health_record(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    if request.method == 'POST':
        blood_pressure = request.POST.get('blood_pressure')
        pulse = int(request.POST.get('pulse'))
        temperature = float(request.POST.get('temperature'))
        HealthRecord.objects.create(patient=patient, blood_pressure=blood_pressure, pulse=pulse, temperature=temperature)
    
    records = HealthRecord.objects.filter(patient=patient)
    context = {'patient': patient, 'records': records}
    return render(request, 'patients/health_record.html', context)
