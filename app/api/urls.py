# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present SEATeam S.p.A.
"""

from django.urls import include, path, re_path
from django.views.decorators.csrf import csrf_exempt

from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token 

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from api import views

schema_view = get_schema_view(
   openapi.Info(
      title="SEACloud API",
      default_version='v1',
      description="Beta",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="pvagnozzi@seateam.com"),
      license=openapi.License(name="Copyright (c) 2020 by SEATeam"),
      swagger = '2.0'     
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


#######
# URL #
#######

urlpatterns = [
    # Swagger #
    re_path(r'api/swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='swagger-schema-json'),
    re_path(r'api/swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema-swagger-ui'),
    re_path(r'api/redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='swagger-schema-redoc'),

    # Authentication #
    path('api/', include('rest_framework.urls')),

    path('api/peripheral/', views.Peripheral.as_view()),
    path('api/peripheral/<int:id>/', views.Peripheral.as_view()),
]