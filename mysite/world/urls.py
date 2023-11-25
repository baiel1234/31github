from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:worldn_id>/", views.detail, name="detail"),
    path("<int:worldn_id>/results/", views.results, name="results"),
    path("<int:worldn_id>/vote/", views.vote, name="vote"),
]