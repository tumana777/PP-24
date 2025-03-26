from django.urls import path
from .views import UserRegisterView, UserLoginView, UserLogoutView, activate_account

app_name = 'user'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('activate/<int:uid>/<str:token>/', activate_account, name='activate'),
]