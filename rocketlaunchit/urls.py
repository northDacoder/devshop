from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'projects.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^admin/', include('django.contrib.admin')),
    url(r'^register/$', 'projects.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),


    url(r'^profile/$', 'projects.views.profile', name='profile'),
    url(r'^profile/(?P<user_id>\w+)/update/$', 'projects.views.profile_update', name='profile_update'),


    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),

    # Support old style base36 password reset links; remove in Django 1.7
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm_uidb36'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),

    url(r'^companies/$', 'projects.views.companies', name='companies'),
    url(r'^companies/new/$', 'projects.views.new_company', name='new_company'),
    url(r'^companies/(?P<company_id>\w+)/$', 'projects.views.view_company', name='view_company'),
    url(r'^companies/(?P<company_id>\w+)/edit/$', 'projects.views.edit_company', name='edit_company'),
    url(r'^companies/(?P<company_id>\w+)/delete/$', 'projects.views.delete_company', name='delete_company'),

    url(r'^projects/$', 'projects.views.projects', name='projects'),
    url(r'^projects/new/$', 'projects.views.new_project', name='new_project'),
    # url(r'^projects/projects/(?P<project_id>\w+)/$', 'projects.views.view_projects', name='view_projects'),
    url(r'^projects/(?P<project_id>\w+)/$', 'projects.views.view_project', name='view_project'),
    url(r'^projects/(?P<project_id>\w+)/edit/$', 'projects.views.edit_project', name='edit_project'),
    url(r'^projects/(?P<project_id>\w+)/delete/$', 'projects.views.delete_project', name='delete_project'),

    url(r'^developers/$', 'projects.views.developers', name='developers'),
    url(r'^developers/new/$', 'projects.views.new_developer', name='new_developer'),
    url(r'^developers/(?P<developer_id>\w+)/$', 'projects.views.view_developer', name='view_developer'),
    url(r'^developers/(?P<developer_id>\w+)/edit/$', 'projects.views.edit_developer', name='edit_developer'),
    url(r'^developers/(?P<developer_id>\w+)/delete/$', 'projects.views.delete_developer', name='delete_developerr'),

)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
