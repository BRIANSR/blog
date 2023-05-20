from django.contrib import admin
from django.urls import path,include
import blogapp.urls
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
import blogapp
import members.urls
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogapp/',include(blogapp.urls)),
    path('members/',include('django.contrib.auth.urls')),
    path('members/',include(members.urls)),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)