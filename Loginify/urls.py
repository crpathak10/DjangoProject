from django.urls import path
from . import views
from .views import create_user, get_all_users, get_user_by_email, update_user, delete_user


urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('users/create/', create_user, name='create_user'),
    path('users/', get_all_users, name='get_all_users'),
    path('users/<str:email>/', get_user_by_email, name='get_user_by_email'),
    path('users/update/<str:email>/', update_user, name='update_user'),
    path('users/delete/<str:email>/', delete_user, name='delete_user'),
    
]
