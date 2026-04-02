from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import SalonService, SalonAppointment, Stylist
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusSalon with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexussalon.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if SalonService.objects.count() == 0:
            for i in range(10):
                SalonService.objects.create(
                    name=f"Sample SalonService {i+1}",
                    category=random.choice(["haircut", "coloring", "facial", "massage", "nails", "waxing"]),
                    duration_mins=random.randint(1, 100),
                    price=round(random.uniform(1000, 50000), 2),
                    status=random.choice(["active", "inactive"]),
                    description=f"Sample description for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 SalonService records created'))

        if SalonAppointment.objects.count() == 0:
            for i in range(10):
                SalonAppointment.objects.create(
                    client_name=f"Sample SalonAppointment {i+1}",
                    client_phone=f"+91-98765{43210+i}",
                    service_name=f"Sample SalonAppointment {i+1}",
                    stylist=f"Sample {i+1}",
                    date=date.today() - timedelta(days=random.randint(0, 90)),
                    time_slot=f"Sample {i+1}",
                    status=random.choice(["booked", "confirmed", "in_progress", "completed", "no_show"]),
                    amount=round(random.uniform(1000, 50000), 2),
                )
            self.stdout.write(self.style.SUCCESS('10 SalonAppointment records created'))

        if Stylist.objects.count() == 0:
            for i in range(10):
                Stylist.objects.create(
                    name=["Rajesh Kumar","Priya Sharma","Amit Patel","Deepa Nair","Vikram Singh","Ananya Reddy","Suresh Iyer","Meera Joshi","Karthik Rao","Fatima Khan"][i],
                    email=f"demo{i+1}@example.com",
                    phone=f"+91-98765{43210+i}",
                    specialization=f"Sample {i+1}",
                    experience_years=random.randint(1, 100),
                    rating=round(random.uniform(1000, 50000), 2),
                    status=random.choice(["active", "on_leave", "inactive"]),
                    commission_rate=round(random.uniform(1000, 50000), 2),
                )
            self.stdout.write(self.style.SUCCESS('10 Stylist records created'))
