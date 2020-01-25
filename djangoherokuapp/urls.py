from django.contrib import admin
from django.urls import path, include
from scraper.views import scrape,index,clear


urlpatterns = [
    path('admin/', admin.site.urls),
    path('scrape/',scrape),
    path('', include('scraper.urls')),
    path('clear/',clear)
]
