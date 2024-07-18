from django.urls import path, reverse_lazy
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetCompleteView,
)
from .views import home

urlpatterns = [
    path('', home, name="home"),
    path('login/', LoginView.as_view(template_name='registrations/login.html'), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]