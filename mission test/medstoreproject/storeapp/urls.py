from django.urls import path
from . import views
from storeapp import views

urlpatterns = [
    path('', views.medicine_list, name='medicine_list'),
    path('medicine/add/', views.medicine_create, name='medicine_add'),
    path('medicine/<int:pk>/edit/', views.medicine_edit, name='medicine_edit'),
    path('medicine/<int:pk>/delete/', views.medicine_delete, name='medicine_delete'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
