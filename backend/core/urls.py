from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('salonservices/', views.salonservice_list, name='salonservice_list'),
    path('salonservices/create/', views.salonservice_create, name='salonservice_create'),
    path('salonservices/<int:pk>/edit/', views.salonservice_edit, name='salonservice_edit'),
    path('salonservices/<int:pk>/delete/', views.salonservice_delete, name='salonservice_delete'),
    path('salonappointments/', views.salonappointment_list, name='salonappointment_list'),
    path('salonappointments/create/', views.salonappointment_create, name='salonappointment_create'),
    path('salonappointments/<int:pk>/edit/', views.salonappointment_edit, name='salonappointment_edit'),
    path('salonappointments/<int:pk>/delete/', views.salonappointment_delete, name='salonappointment_delete'),
    path('stylists/', views.stylist_list, name='stylist_list'),
    path('stylists/create/', views.stylist_create, name='stylist_create'),
    path('stylists/<int:pk>/edit/', views.stylist_edit, name='stylist_edit'),
    path('stylists/<int:pk>/delete/', views.stylist_delete, name='stylist_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
