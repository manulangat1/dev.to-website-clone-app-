from ._base import *


urlpatterns = [
    
    path('api/auth',include('knox.urls')),
    path('register/',views.RegisterAPI.as_view()),
    path('login/',views.LoginAPI.as_view()),
    path('user/',views.UserAPI.as_view()),
    path('logout/',knox_views.LogoutView.as_view())
]