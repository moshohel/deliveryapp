from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from core import views
from . import login_view
from django.conf.urls.static import static

urlpatterns = [
    path('', login_view.login_auth, name='login'),
    path('logout/', login_view.logout_view, name='logout'),
    path('admin_user/parcel_list/', views.parcel_list, name='parcel_list'),
    path('admin_user/createUser/', views.createUser, name='createUser'),
    path('merchant/parcel_list/', views.merchant_parcel_list, name='merchant_parcel_list'),
    path('get-districts/<int:divi_id>', views.districts_api),
    # path('', views.home_page, name="home_page"),
    path('admin/', admin.site.urls),
    path('core/', include('core.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
