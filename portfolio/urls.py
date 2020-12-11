from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import jobs.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name='home'),  # set url home path to html with job models
    path('blog/', include('blog.urls')),  # include blog/urls.py links in /blog slug
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # set url route/link to see static files in admin

