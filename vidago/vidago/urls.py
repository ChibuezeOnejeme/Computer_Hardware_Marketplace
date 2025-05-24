
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
      path("",include('core.urls')),
      path("item/",include('item.urls')),
      path("conversation/",include('conversation.urls')),
      path("dashboard/", include('dashboard.urls')),
      path("admin/", admin.site.urls),

 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Serve media files in development
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)