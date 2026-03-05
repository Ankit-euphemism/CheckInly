from django.urls import path
from .views import mark_attendance, view_attendance

urlpatterns = [
#    path('admin/', admin, name='admin')
    path('mark/', mark_attendance, name='mark_attendance'),
    path('', view_attendance, name='view_attendance'),
]
