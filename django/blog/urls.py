from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.post_list),
    path('1111', views.post_list2),
    re_path(r"(?P<pk>[0-9]+)/$", views.post_detail)
]
