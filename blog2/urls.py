from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_post, name='post'),
    path('<int:post_id>', views.post_detail)
]