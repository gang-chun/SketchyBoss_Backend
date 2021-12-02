"""SketchyBossBE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from api import views
from rest_auth.views import (
    LoginView, LogoutView, UserDetailsView, PasswordChangeView,
    PasswordResetView, PasswordResetConfirmView
)

from django.urls import re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', obtain_jwt_token),

    path('rest-auth/', include('rest_auth.urls')),
    url('api/rest-auth/registration', include('rest_auth.registration.urls')),

    ## The following APIs do not work
    url(r'api/password/reset/$', PasswordResetView.as_view(),
        name='rest_password_reset'),
    url(r'^api/password/change/$', PasswordChangeView.as_view(),
        name='rest_password_change'),
    url(r'^api/password/reset/confirm/', PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),


    path('', views.report_list),
    url(r'^api/reports/$', views.report_list),
    url(r'^api/reports/(?P<pk>[0-9]+)$', views.get_report),
    path('companies/', views.company_list),
    url(r'^api/companies/$', views.company_list),
    url(r'^api/companies/(?P<pk>[0-9]+)$', views.get_company),
    path('actors/', views.actor_list),
    url(r'^api/actors/$', views.actor_list),
    url(r'^api/actors/(?P<pk>[0-9]+)$', views.get_actor),
    path('api/password_reset/', include('django_rest_passwordreset.urls')),
    url(r'^api/company/reports/(?P<pk>[0-9]+)$', views.company_report_list),
]
