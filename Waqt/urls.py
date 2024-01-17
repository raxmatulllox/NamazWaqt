from django.urls import path

from . import views


urlpatterns = [
    path('', views.NamazTimesViews),
    path('andijon/', views.AndijonNamazWaqt, name='andijon'),
]