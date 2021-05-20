
from django.contrib import admin
from django.urls import path, include
from p_library import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.generic.base import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('p_library.urls')),
    path('', views.index),
    path('friends/book_increment/', views.book_increment),
    path('index/book_increments/', views.book_increments),
    path('index/book_decrements/', views.book_decrements),
    path('redactions/', views.redactions),
    path('friends/', views.friends),
    path('accounts/', include('allauth.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
