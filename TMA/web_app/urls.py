from django.urls import path
from . import views
from .views import items_list

urlpatterns = [

    path('', views.home, name=""),
    path('login', views.user_login, name="login"),
    path("coordinator_dashboard", views.coordinator_dashboard, name="coordinator_dashboard"),
    path('employee_dashboard', views.employee_dashboard, name="employee_dashboard"),
    path('user-logout', views.user_logout, name="user-logout"),
    path('Items', items_list, name='items_list')
]
