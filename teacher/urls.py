from django.shortcuts import redirect
from django.contrib import admin
import pages.views as pages_views
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('contact/', include('contact.urls')),
    re_path(r'^auth/', include('social_django.urls', namespace='social')),
    path('accounts/', include('accounts.urls')),
    path('chat/', include('chat.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)