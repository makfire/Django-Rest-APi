from django.conf.urls import include, url,patterns
from django.contrib import admin
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^movies/',include('movies.urls')),
]



