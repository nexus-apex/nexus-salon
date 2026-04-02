from django.db import models

class SalonService(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=[("haircut", "Haircut"), ("coloring", "Coloring"), ("facial", "Facial"), ("massage", "Massage"), ("nails", "Nails"), ("waxing", "Waxing")], default="haircut")
    duration_mins = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("inactive", "Inactive")], default="active")
    description = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class SalonAppointment(models.Model):
    client_name = models.CharField(max_length=255)
    client_phone = models.CharField(max_length=255, blank=True, default="")
    service_name = models.CharField(max_length=255, blank=True, default="")
    stylist = models.CharField(max_length=255, blank=True, default="")
    date = models.DateField(null=True, blank=True)
    time_slot = models.CharField(max_length=255, blank=True, default="")
    status = models.CharField(max_length=50, choices=[("booked", "Booked"), ("confirmed", "Confirmed"), ("in_progress", "In Progress"), ("completed", "Completed"), ("no_show", "No Show")], default="booked")
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.client_name

class Stylist(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, default="")
    phone = models.CharField(max_length=255, blank=True, default="")
    specialization = models.CharField(max_length=255, blank=True, default="")
    experience_years = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("on_leave", "On Leave"), ("inactive", "Inactive")], default="active")
    commission_rate = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
