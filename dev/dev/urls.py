
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('backend.urls.backend')),
    path('admin/', admin.site.urls),
    path('martor/', include('martor.urls')),
]
