from django.contrib import admin
from .models import SalonService, SalonAppointment, Stylist

@admin.register(SalonService)
class SalonServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "duration_mins", "price", "status", "created_at"]
    list_filter = ["category", "status"]
    search_fields = ["name"]

@admin.register(SalonAppointment)
class SalonAppointmentAdmin(admin.ModelAdmin):
    list_display = ["client_name", "client_phone", "service_name", "stylist", "date", "created_at"]
    list_filter = ["status"]
    search_fields = ["client_name", "client_phone", "service_name"]

@admin.register(Stylist)
class StylistAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "specialization", "experience_years", "created_at"]
    list_filter = ["status"]
    search_fields = ["name", "email", "phone"]
