from django.urls import path

from shorturl import views

urlpatterns = [
    path("g/<int:pk>", views.go_to_url),
]
