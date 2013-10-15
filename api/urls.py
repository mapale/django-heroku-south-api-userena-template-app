from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('api.views',
    url(r'^$', 'api_root'),
    url(r'^auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)

