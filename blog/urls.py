from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('home', views.post_list, name='home'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/edit/<int:pk>', views.post_edit, name='post_edit'),
    path('del/<int:pk>', views.post_del, name='post_del'),
    path('atividades', views.atividades, name='atividades'),
    path('accounts/', include('django.contrib.auth.urls')),
]