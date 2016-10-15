from django.conf.urls import url
from .views import create_account, log_user_in, log_user_out

urlpatterns = [
    url(r'^create_account$', create_account, name='create_account'),
    url(r'^login$', log_user_in, name='login'),
    url(r'^logout$', log_user_out, name='logout'),
]
