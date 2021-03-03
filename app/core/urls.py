from django.contrib import admin
from django.urls import path, include, re_path  # add this

urlpatterns = [        
    path("admin/", admin.site.urls),   # Admin
    path("", include("api.urls"))      # REST API 
]

#if bool(settings.DEBUG):
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)