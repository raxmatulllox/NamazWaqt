from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('Waqt.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]
