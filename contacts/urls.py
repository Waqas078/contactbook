from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact_list/', views.contact_list, name='contact_list'),
    path('create/', views.contact_create, name='contact_create'),
    path('update/<int:pk>/', views.contact_update, name='contact_update'),
    path('delete/<int:pk>/', views.contact_delete, name='contact_delete'),
    path('search/', views.contact_search, name='contact_search'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout_page, name='logout'),
]
