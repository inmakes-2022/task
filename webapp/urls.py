from . import views
from django.urls import path

app_name='schoolweb'

urlpatterns = [
    path('', views.home,name='home'),
    path('login/', views.login_view, name='login'),
    path('register/',views.register_view, name='register'),
    path('form/', views.form, name='form'),
    path('logout/', views.logout, name='logout'),
    path('store/', views.store, name='store'),
]


