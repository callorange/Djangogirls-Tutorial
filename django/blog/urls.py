from django.urls import path, re_path
from . import views

urlpatterns = [
    path('list', views.post_list, name='post-list'),

    #path('<int:pk>', views.post_detail),
    path('post/<int:pk>', views.post_detail, name='post-detail'),
    # re_path(r"(?P<pk>[0-9]+)$", views.post_detail)
    path('post/<int:pk>/del', views.post_del, name='post-del'),

    path('trash/list', views.trash_list, name='trash-list'),
    path('trash/<int:pk>', views.trash_detail, name='trash-detail'),
    path('trash/<int:pk>/rollback', views.trash_rollback, name='trash-rollback'),
]
