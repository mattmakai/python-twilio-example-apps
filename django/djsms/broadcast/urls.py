from django.conf.urls import url
from . import views

urlpatterns = [
    url('broadcast/', views.broadcast_sms, name="default"),
]

