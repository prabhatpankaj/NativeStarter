from django.conf.urls import include, url
from .views import AuthLogin, AuthRegister
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(),name = 'login'),
    url(r'^logout/$', views.LogoutView.as_view() ,name = 'logout'),
    url(r'^(?P<username>[a-zA-Z]{1,18})/$', views.ProfileView.as_view(), name='profile'),


    url(r'^api/v1/auth/login/', obtain_jwt_token),
    url(r'^api/v1/auth/token-refresh/', refresh_jwt_token),
    url(r'^api/v1/auth/token-verify/', verify_jwt_token),
    url(r'^api/v1/auth/register/$', AuthRegister.as_view()),
]