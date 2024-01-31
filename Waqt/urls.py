from django.urls import path

from . import views


urlpatterns = [
    path('', views.NamazTimesViews),
    path('andijon/', views.AndijonNamazWaqt, name='andijon'),
    path('buxoro/', views.BuxoroNamazWaqt, name='buxoro'),
    path('denov/', views.DenovNamazWaqt, name='denov'),
    path('guliston/', views.GulistonNamazWaqt, name='guliston'),
    path('jizzax/', views.JizzaxNamazWaqt, name='jizzax'),
    path('margilon/', views.MargilanNamazWaqt, name='margilan'),
    path('namangan/', views.NamanganNamazWaqt, name='namangan'),
    path('navoiy/', views.NavoiyNamazWaqt, name='navoiy'),
    path('nukus/', views.NukusNamazWaqt, name='nukus'),
    path('olmaliq/', views.OlmaliqNamazWaqt, name='olmaliq'),
    path('qarshi/', views.QarshiNamazWaqt, name='qarshi'),
    path('qoqan/', views.QoqanNamazWaqt, name='qoqan'),
    path('samarqand/', views.SamarqandNamazWaqt, name='samarqand'),
    path('termiz/', views.TermizNamazWaqt, name='termiz'),
    path('xiva/', views.XivaNamazWaqt, name='xiva'),
    path('map/', views.MapView, name='map'),
]
