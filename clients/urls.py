from django.urls import path
from .views import ClientListView, PassportListView, ClientPassportListView, HomePageView, SignUpView

from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # URL для выхода
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('passports/', PassportListView.as_view(), name='passport_list'),
    path('client_passports/', ClientPassportListView.as_view(), name='client_passport_list'),
]
