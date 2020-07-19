"""porfolio_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings  # add this
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static  # add this
from django.contrib import admin
from django.urls import include, path, re_path  # add this
from django.views.generic.base import RedirectView
import os
ADMIN_URL = os.environ.get('ADMIN_URL','admin/')

urlpatterns = i18n_patterns(
    path(ADMIN_URL, admin.site.urls),
    path('api/', include('core.urls')),
    path('', RedirectView.as_view(url='api/', permanent=False)),
    prefix_default_language=True      # add this
)
