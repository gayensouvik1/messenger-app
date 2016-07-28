from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', 'messenger.views.register',name='register'),
    url(r'^register/success/$', 'messenger.views.register_success',name='success'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^contact/$', 'messenger.views.contact',name='contact'),
    url(r'^logout_success/$', 'messenger.views.logout_success',name='logout_success'),
    url(r'^accounts/profile/$', 'messenger.views.profile',name='profile'),
    url(r'^list/$', 'messenger.views.list', name='list'),
    url(r'^list_only/$', 'messenger.views.list_only', name='list_only'),
    url(r'^home/$','messenger.views.home',name='home'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
