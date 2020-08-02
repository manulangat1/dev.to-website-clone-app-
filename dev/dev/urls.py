
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('api/',include('backend.urls.backend')),
    path('auth/',include('backend.urls.auth')),
    path('',include('backend.urls.norm')),
    path('admin/', admin.site.urls),
    path('martor/', include('martor.urls')),
]
