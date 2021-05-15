"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from p_library import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.generic.base import TemplateView
from p_library.urls import urlpatterns as p_library_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('p_library.urls')),
    path('', views.index),
    #path('', views.books_list),
    path('friends/book_increment/', views.book_increment),
    path('index/book_increments/', views.book_increments),
    path('index/book_decrements/', views.book_decrements),
    path('redactions/', views.redactions),
    path('friends/', views.friends)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += p_library_urls