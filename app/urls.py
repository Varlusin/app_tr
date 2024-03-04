from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns
from users.views import singin, registerPage, lgout
from app import settings
from django.conf.urls.static import static

urlpatterns = [
    path(('admin/'), admin.site.urls),
    path(("post/"), include('users.urls')),
    path('location/', include('location.urls')),
    path('sign-in/',singin, name = "singin" ),
    path("register/", registerPage, name = 'register'),
    path("log-out/", lgout, name='log-out'),
    path('', include('mayin.urls')),
]

if settings.DEBUG:
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls")),
                    
                    ]
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
    ]




