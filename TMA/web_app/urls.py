from django.urls import path
from . import views
from .views import items_list, items_list_coordinator, request_list, submit_request

urlpatterns = [

    path('', views.home, name=""),
    path('login', views.user_login, name="login"),
    path("coordinator_dashboard", views.coordinator_dashboard, name="coordinator_dashboard"),
    path('employee_dashboard', views.employee_dashboard, name="employee_dashboard"),
    path('user-logout', views.user_logout, name="user-logout"),
    path('Items', items_list, name='items_list'),
    path('Button', views.open_windows, name='order_button'),
    path('Items_coordinator', items_list_coordinator, name='items_list_coordinator'),
    path('request_data', request_list, name='request_data'),
    path('submit_request', submit_request, name='submit_request'),

]
