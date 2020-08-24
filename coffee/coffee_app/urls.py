from django.conf.urls import url
from coffee_app import views

#TEMPLTE TAGGING
app_name = 'coffee_app'

urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]