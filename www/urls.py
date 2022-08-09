from . import views
from django.urls import path, include

app_name = 'www'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.ContactView.as_view(), name='contact'),

]
