"""firstsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from firstapp.views import detail, detail_comment, listing, index_login, register, detail_vote
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import logout
from DjangoUeditor import urls as DjangoUeditor_urls
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ueditor/', include(DjangoUeditor_urls)),
    url(r'^login/$', index_login, name='login'),
    url(r'^logout/$', logout, {'next_page': '/login'}, name='logout'),
    url(r'^register/$', register, name='register'),
    url(r'^list/$', listing, name="listing"),
    url(r'^list/(?P<cate>[A-Za-z]+)$', listing, name="list"),
    url(r'^detail/(?P<id>\d+)$', detail, name="detail"),
    url(r'^detail/vote/(?P<id>\d+)$', detail_vote, name="detail_vote"),
    url(r'^detail/(?P<page_num>\d+)/comment$', detail_comment, name="detail_comment"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
