from django.urls import path

from mersana_app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('send-comment', views.comment, name='send_comment')
]