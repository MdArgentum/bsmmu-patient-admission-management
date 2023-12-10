from django.shortcuts import render, redirect
from .forms import PatientForm, ContactForm
from .models import Patient
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def home(request):
    return render(request, 'home.html')

def patient_admission(request):
    if request.method=="POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your From alredy Submited.")
            # pk = form.instance.pk  # Get the primary key of the saved instance
            # return generate_pdf(request, pk)
            return redirect('home')
    else:
        form =  PatientForm()
    context = {
        'form': form,
    }
    return render(request, 'hospital/patient_admission.html', context)

def admited_patient(request):

    admitted_patients = Patient.objects.filter(status='admited').order_by('-created_at')
    items_per_page = 5  
    paginator = Paginator(admitted_patients, items_per_page)
    page_number = request.GET.get('page', 1)
    try:
        patients_page = paginator.page(page_number)
    except PageNotAnInteger:
        patients_page = paginator.page(1)
    except EmptyPage:
        patients_page = paginator.page(paginator.num_pages)
    context = {
        'patients_page': patients_page,
    }
    return render(request, 'hospital/admited_patient.html', context)

def old_patient(request):
    admitted_patients = Patient.objects.filter(status='released').order_by('-created_at')
    items_per_page = 5  
    paginator = Paginator(admitted_patients, items_per_page)
    page_number = request.GET.get('page', 1)
    try:
        patients_page = paginator.page(page_number)
    except PageNotAnInteger:
        patients_page = paginator.page(1)
    except EmptyPage:
        patients_page = paginator.page(paginator.num_pages)
    context = {
        'patients_page': patients_page,
    }
    return render(request, 'hospital/old_patient.html', context)

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.templatetags.static import static
from django.conf import settings

def generate_pdf(request, pk):
    patient = Patient.objects.get(pk=pk)
    template_path = 'pdf_template.html'
    context = {
        'patient' : patient,
    }
    # Render the template
    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Patient_profile.pdf"'

    # Create PDF
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Error generating PDF')

    return response


def contact(request):
    form = ContactForm()
    if request.method =="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Message has been sent already.")
            return redirect('home')
    else:
        return render(request, 'hospital/contact.html',{'form':form})

def patient_single(request, pk):
    patient = Patient.objects.get(pk=pk)
    context = {
        'patient': patient,
    }
    return render(request, 'hospital/patient_single.html', context)

def realised_patient(request, pk):
    patient = Patient.objects.get(pk=pk)
    patient.status = "released"
    patient.save()
    return redirect(request. META['HTTP_REFERER'])
