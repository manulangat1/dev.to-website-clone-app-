from ._base import *


urlpatterns = [
    
    path('api/auth',include('knox.urls')),
    path('register/',RegisterAPI.as_view()),
    path('login/',LoginAPI.as_view()),
    path('user/',UserAPI.as_view()),
    path('logout/',knox_views.LogoutView.as_view())
]