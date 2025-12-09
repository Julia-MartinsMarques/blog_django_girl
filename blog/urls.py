from django.urls import path
<<<<<<< HEAD
from . import views
=======
from . import views 
>>>>>>> a405d1494648b5ad3a19afba839c923370898106

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
]