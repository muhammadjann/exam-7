from django.urls import path

from apps.users.api_endpoints.User import UserLoginView, UserRegistration, UserLogoutView, ActivateAccountView, \
    ChangePasswordView, PasswordResetRequest

urlpatterns = [
    path('login/', UserLoginView.as_view()),
    path('register/', UserRegistration.as_view()),
    path('logout/', UserLogoutView.as_view()),

    path('activation/', ActivateAccountView.as_view()),
    path('chage-password/', ChangePasswordView.as_view()),
    path('reset-password', PasswordResetRequest.as_view()),
]