from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
    path('password-reset/', views.RequestPasswordResetView.as_view(), name='password_reset'),
    path('password-reset-confirm/', views.PasswordResetView.as_view(), name='password_reset_confirm'),
]