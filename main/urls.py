from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('student_form/', views.student_form, name='student_form'),
    path('delete_data/<int:id>/', views.delete_data, name='delete_data'),
    path('update_date/<int:id>/', views.update_data, name='update_data')
]