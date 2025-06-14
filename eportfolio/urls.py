from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Put the admin paths ABOVE the core ones to avoid an error where it otherwise
    # gets confused and thinks 'admin' is the name of a portfolio project page
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]

# Add/edit this line to customize the admin site (CHANGE TO *YOUR* NAME!)
admin.site.site_header = "Sam Werlin's ePortfolio Editor"

# If in development mode, just serve admin/user images from Django's own media folder
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)