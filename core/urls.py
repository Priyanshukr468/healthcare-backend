from django.urls import path
from .views import (
    RegisterView,
    PatientListCreateView,
    PatientDetailView,
    DoctorListCreateView,
    DoctorDetailView,
    MappingListCreateView,
    MappingByPatientView,
    MappingDeleteView,
    get_patients  
)

urlpatterns = [
   
    path('auth/register/', RegisterView.as_view(), name='register'),
   
    path('patients/authenticated/', get_patients, name='get_patients'),

    path('patients/', PatientListCreateView.as_view(), name='patients'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),

    
    path('doctors/', DoctorListCreateView.as_view(), name='doctors'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),

    
    path('mappings/', MappingListCreateView.as_view(), name='mappings'),
    path('mappings/<int:patient_id>/', MappingByPatientView.as_view(), name='mappings-by-patient'),
    path('mappings/delete/<int:pk>/', MappingDeleteView.as_view(), name='delete-mapping'),
]
