from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from sap_renter import settings
from video_tenant.forms import LoginForm, ResetPWord

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sap_renter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # Account and Registration Related
    url(r'^account/', 'video_tenant.views.account', name='account'),
    url(r'^registration/$', 'video_tenant.views.register', name='register'),
    url(r'^registration/login/$', 'django.contrib.auth.views.login', kwargs={'authentication_form': LoginForm}, name='login'),
    url(r'^registration/logout/$', 'django.contrib.auth.views.logout', kwargs={'next_page': '/'}, name='logout'),
    url(r'^registration/password_reset/$', 'django.contrib.auth.views.password_reset', kwargs={'password_reset_form': ResetPWord}, name='password_reset'),
    url(r'^registration/password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^registration/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^registration/reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),


    # other stuff
    url(r'^rental/$', 'video_tenant.views.rental', name='rental'),
    url(r'^view-rental/(?P<rental_id>\d+)$','video_tenant.views.view_rental', name='view_rental'),
)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)