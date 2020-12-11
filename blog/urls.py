from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blogs, name='blogs'),  # set url home path to html with job models
    path('<int:blog_id>/' , views.detail, name='detail')  # look for an integer after
]

