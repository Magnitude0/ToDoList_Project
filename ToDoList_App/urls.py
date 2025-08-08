from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('register/', views.register_view, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('task/create/', views.task_create, name='task-create'),
    path('task/update/<int:pk>/', views.task_update, name='task-update'),
    path('task/delete/<int:pk>/', views.task_delete, name='task-delete'),
]
