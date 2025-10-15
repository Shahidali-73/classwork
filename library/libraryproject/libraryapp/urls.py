from django.urls import path
from . import views

urlpatterns = [
    path('', views.library_add_book, name='addbook'),
    path('retrieve/', views.library_read, name='library'),
    path('update/<int:id>/', views.library_update, name='update'),
    path('delete/<int:pk>/', views.library_delete, name='delete'),
    
]
