from django.urls import path
from . import views


from .views import NewslettersView

app_name = 'newsletters'

urlpatterns = [
path('newsletter', NewslettersView.as_view(), name='newsletters'),
]