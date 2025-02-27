"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

# Three modules for swagger: 
from rest_framework import permissions 
from drf_yasg.views import get_schema_view 
from drf_yasg import openapi

from rest_framework_simplejwt.views import (
    TokenObtainPairView,

)


schema_view = get_schema_view( 
    openapi.Info( 
        title="Django Template For Creating API", 
        default_version="v1", 
        description="This template provides all the needs to create a project using Django", 
        terms_of_service="#", 
        contact=openapi.Contact(email="ibrahim.kurut@gmail.com"), # Change e-mail on this line! 
        license=openapi.License(name="BSD License"), 
    ), 
    public=True, 
    permission_classes=[permissions.AllowAny], 
) 
urlpatterns = [ 
    path("admin/", admin.site.urls), 

    # Debug Toolbar:
    path(' debug /', include('debug_toolbar.urls')),

    # Url paths for swagger: 
    path("swagger(<format>\.json|\.yaml)", 
    schema_view.without_ui(cache_timeout=0), name="schema-json"), 
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), 
    name="schema-swagger-ui"), 
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    
    # Register endpoint
    path('api/users/', include("account.urls")),
    path('api/token/', TokenObtainPairView.as_view()),


    path('api/', include("flight_app.urls")),
]
