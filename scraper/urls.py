from django.urls import path

from . import views

urlpatterns = [
    path('', views.topWeekly),
    path('tag/', views.categories),
    path('tag/<slug:tag_value>/', views.tagList)
]