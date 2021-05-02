from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from core import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.parcel_list, name='parcel_list'),
    path('get-districts/<int:divi_id>', views.districts_api),
    # path('', views.home_page, name="home_page"),
    path('admin/', admin.site.urls),
    path('core/', include('core.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
