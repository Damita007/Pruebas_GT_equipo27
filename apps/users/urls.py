#from allauth.account.views import confirm_email
#from django.conf.urls import url
from django.urls import path
#from . import views
from .views import SignUpView


urlpatterns = [
    #path('', views.UserListView.as_view()),
    path('signup/', SignUpView.as_view(), name='signup'),
]
