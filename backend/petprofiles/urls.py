from django.urls import path, include
from petprofiles import views 
from django.conf import settings 
from django.conf.urls.static import static 


urlpatterns = [
    path('', views.get_user_profiles),
    path('<int:pk>/', views.pet_single),
    path('createpet/', views.create_pet),
    path('changepet/', views.change_pet),
    path('images/<int:pk>/', views.get_images),
    path('guest/', views.guest_views),
]