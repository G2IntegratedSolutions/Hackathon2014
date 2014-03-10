from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from vote_app.views import MobileApp

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SAMVotes.views.home', name='home'),
    # url(r'^SAMVotes/', include('SAMVotes.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^mobile/', MobileApp.as_view()),
)
