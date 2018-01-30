from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list),
    path('admin/', views.post_list2),
]
