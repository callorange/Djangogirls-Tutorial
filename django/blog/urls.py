from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list),
    path('1111', views.post_list2),
    path('detail/', views.post_detail),
]
