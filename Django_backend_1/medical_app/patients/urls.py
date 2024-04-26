from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_patient, name='register_patient'),
    path('health_record/<int:patient_id>/', views.health_record, name='health_record'),
]