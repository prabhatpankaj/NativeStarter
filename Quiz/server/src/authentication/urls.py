from django.conf.urls import include, url
from authentication.api_views import AuthAPILogin, AuthAPIRegister
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    # web url

    # api url
    url(r'^api/v1/auth/login/$', obtain_jwt_token),
    url(r'^api/v1/auth/token-refresh/', refresh_jwt_token),
    url(r'^api/v1/auth/token-verify/', verify_jwt_token),
    url(r'^api/v1/auth/register/$', AuthAPIRegister.as_view()),
]