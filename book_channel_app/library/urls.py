from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('book/<str:isbn>', views.book, name='book'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)