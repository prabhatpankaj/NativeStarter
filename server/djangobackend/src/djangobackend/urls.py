from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^docs/', include('rest_framework_docs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/auth/', include('authentication.urls')),
    url(r'^api/v1/quizzes/', include('quiz.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
