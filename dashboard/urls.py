"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from rest_framework import routers
from rest_framework.authtoken import views as auth_views

from events import views as events_view
from organizations import views as organizations_view

router = routers.DefaultRouter()
router.register(r'events', events_view.EventsViewSet)
router.register(r'incidents', events_view.IncidentsViewSet)
router.register(r'organizations', organizations_view.OrganizationsViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/authenticate/', auth_views.obtain_auth_token),


    path('admin/', admin.site.urls),
]
