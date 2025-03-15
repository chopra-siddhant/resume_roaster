from django.urls import path
from .. import views

urlpatterns = [
    path('upload_resume/', views.upload_resume, name='upload_resume'),
    path('resume_results/<int:resume_id>/', views.get_resume_results, name='resume_results'),
    path('hr_simulator/', views.hr_simulator, name='hr_simulator'),
    path('linkedin_flex/', views.linkedin_flex, name='linkedin_flex'),
]
