import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import SalonService, SalonAppointment, Stylist


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['salonservice_count'] = SalonService.objects.count()
    ctx['salonservice_haircut'] = SalonService.objects.filter(category='haircut').count()
    ctx['salonservice_coloring'] = SalonService.objects.filter(category='coloring').count()
    ctx['salonservice_facial'] = SalonService.objects.filter(category='facial').count()
    ctx['salonservice_total_price'] = SalonService.objects.aggregate(t=Sum('price'))['t'] or 0
    ctx['salonappointment_count'] = SalonAppointment.objects.count()
    ctx['salonappointment_booked'] = SalonAppointment.objects.filter(status='booked').count()
    ctx['salonappointment_confirmed'] = SalonAppointment.objects.filter(status='confirmed').count()
    ctx['salonappointment_in_progress'] = SalonAppointment.objects.filter(status='in_progress').count()
    ctx['salonappointment_total_amount'] = SalonAppointment.objects.aggregate(t=Sum('amount'))['t'] or 0
    ctx['stylist_count'] = Stylist.objects.count()
    ctx['stylist_active'] = Stylist.objects.filter(status='active').count()
    ctx['stylist_on_leave'] = Stylist.objects.filter(status='on_leave').count()
    ctx['stylist_inactive'] = Stylist.objects.filter(status='inactive').count()
    ctx['stylist_total_rating'] = Stylist.objects.aggregate(t=Sum('rating'))['t'] or 0
    ctx['recent'] = SalonService.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def salonservice_list(request):
    qs = SalonService.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(category=status_filter)
    return render(request, 'salonservice_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def salonservice_create(request):
    if request.method == 'POST':
        obj = SalonService()
        obj.name = request.POST.get('name', '')
        obj.category = request.POST.get('category', '')
        obj.duration_mins = request.POST.get('duration_mins') or 0
        obj.price = request.POST.get('price') or 0
        obj.status = request.POST.get('status', '')
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/salonservices/')
    return render(request, 'salonservice_form.html', {'editing': False})


@login_required
def salonservice_edit(request, pk):
    obj = get_object_or_404(SalonService, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.category = request.POST.get('category', '')
        obj.duration_mins = request.POST.get('duration_mins') or 0
        obj.price = request.POST.get('price') or 0
        obj.status = request.POST.get('status', '')
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/salonservices/')
    return render(request, 'salonservice_form.html', {'record': obj, 'editing': True})


@login_required
def salonservice_delete(request, pk):
    obj = get_object_or_404(SalonService, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/salonservices/')


@login_required
def salonappointment_list(request):
    qs = SalonAppointment.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(client_name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'salonappointment_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def salonappointment_create(request):
    if request.method == 'POST':
        obj = SalonAppointment()
        obj.client_name = request.POST.get('client_name', '')
        obj.client_phone = request.POST.get('client_phone', '')
        obj.service_name = request.POST.get('service_name', '')
        obj.stylist = request.POST.get('stylist', '')
        obj.date = request.POST.get('date') or None
        obj.time_slot = request.POST.get('time_slot', '')
        obj.status = request.POST.get('status', '')
        obj.amount = request.POST.get('amount') or 0
        obj.save()
        return redirect('/salonappointments/')
    return render(request, 'salonappointment_form.html', {'editing': False})


@login_required
def salonappointment_edit(request, pk):
    obj = get_object_or_404(SalonAppointment, pk=pk)
    if request.method == 'POST':
        obj.client_name = request.POST.get('client_name', '')
        obj.client_phone = request.POST.get('client_phone', '')
        obj.service_name = request.POST.get('service_name', '')
        obj.stylist = request.POST.get('stylist', '')
        obj.date = request.POST.get('date') or None
        obj.time_slot = request.POST.get('time_slot', '')
        obj.status = request.POST.get('status', '')
        obj.amount = request.POST.get('amount') or 0
        obj.save()
        return redirect('/salonappointments/')
    return render(request, 'salonappointment_form.html', {'record': obj, 'editing': True})


@login_required
def salonappointment_delete(request, pk):
    obj = get_object_or_404(SalonAppointment, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/salonappointments/')


@login_required
def stylist_list(request):
    qs = Stylist.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'stylist_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def stylist_create(request):
    if request.method == 'POST':
        obj = Stylist()
        obj.name = request.POST.get('name', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.specialization = request.POST.get('specialization', '')
        obj.experience_years = request.POST.get('experience_years') or 0
        obj.rating = request.POST.get('rating') or 0
        obj.status = request.POST.get('status', '')
        obj.commission_rate = request.POST.get('commission_rate') or 0
        obj.save()
        return redirect('/stylists/')
    return render(request, 'stylist_form.html', {'editing': False})


@login_required
def stylist_edit(request, pk):
    obj = get_object_or_404(Stylist, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.specialization = request.POST.get('specialization', '')
        obj.experience_years = request.POST.get('experience_years') or 0
        obj.rating = request.POST.get('rating') or 0
        obj.status = request.POST.get('status', '')
        obj.commission_rate = request.POST.get('commission_rate') or 0
        obj.save()
        return redirect('/stylists/')
    return render(request, 'stylist_form.html', {'record': obj, 'editing': True})


@login_required
def stylist_delete(request, pk):
    obj = get_object_or_404(Stylist, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/stylists/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['salonservice_count'] = SalonService.objects.count()
    data['salonappointment_count'] = SalonAppointment.objects.count()
    data['stylist_count'] = Stylist.objects.count()
    return JsonResponse(data)
