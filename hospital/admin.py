from django.contrib import admin
from .models import Patient, Contact
# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    '''Admin View for Patient'''

    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('-id',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    '''Admin View for Contact'''

    list_display = ('name',)
