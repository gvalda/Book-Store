from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # User manager
    path('accounts/', include('allauth.urls')),

    # Local
    path('books/', include('books.urls')),
    path('', include('pages.urls')),
]
