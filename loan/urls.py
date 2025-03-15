from django.urls import path
from .views import home, apply_loan, loan_status, repayment, register, dashboard, user_login
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('apply/', apply_loan, name='apply_loan'),
    path('status/', loan_status, name='loan_status'),
    path('repayment/', repayment, name='repayment'),
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]


