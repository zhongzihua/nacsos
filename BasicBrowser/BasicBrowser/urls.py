from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views as auth_views
from scoping import views
import BasicBrowser.views as site_views
from django.urls import include, path

urlpatterns = [
    #path('lotto/', include('lotto.urls')),
    url(r'^tmv_app/', include('tmv_app.urls')),
    url(r'^scoping/', include('scoping.urls')),
    url(r'^parliament/', include('parliament.urls')),
    path('lotto', include('lotto.urls')),
    url(r'^admin/', admin.site.urls),
	url(r'^$', site_views.index),
 	path('accounts/login/', auth_views.LoginView.as_view(), {'template_name': 'scoping/login.html'}),
 	url(r'^accounts/logout/$', views.logout_view, name='logout_view'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
