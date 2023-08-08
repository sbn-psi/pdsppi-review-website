from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from django.views.generic import RedirectView

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views

urlpatterns = [
    path('django-admin/', admin.site.urls),

    path('admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),

    path('search/', search_views.search, name='search'),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('userauth.urls')),

    path('comments/', include('django_comments_xtd.urls')),

    path('reviews/', include('allauth.urls')), # Creates urls like yourwebsite.com/login/
    # url(r'^accounts/', include('allauth.urls')), # Creates urls like yourwebsite.com/accounts/login/
    path('', RedirectView.as_view(url='/reviews/')),
]

print("settings.DEBUG:")
print(settings.DEBUG)

if settings.DEBUG == 'True':
    print('wagtail serves static files')
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    print('nginx serves static files')

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("reviews/", include(wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]