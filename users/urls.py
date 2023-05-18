
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [

path('login/', views.loginUser, name='login'),
path('logout/', views.logoutUser, name='logout'),
path('register/', views.registerUser, name='register'),


path('', views.profiles, name='profiles'),
path('profile/<str:pk>/', views.userProfile, name='user-profile'),

path('edit-account/', views.editAccount, name='edit-account'),

path('edit-balance/<str:pk>/', views.editProfileBalance, name='edit-balance'),

path('balance', views.balance, name='balance'),
]

urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
