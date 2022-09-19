from django.urls import path
from . import views

app_name='calendar'

urlpatterns = [
    path('', views.calendar_detail.as_view(), name='calendar_detail'),
    path('new/', views.event, name='calendar_create'),
    path('update/<int:event_id>', views.event, name='calendar_update'),
]
