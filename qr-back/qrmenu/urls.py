from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from menu import views


urlpatterns = [
    path("api/store/<str:slug>", views.get_store),
    path('api/store/categories', views.get_categories),
    path('api/store/foods/<int:id>', views.get_foods_by_category),
    path("api/food/<int:id>", views.get_detail_food),
    path("admin/", admin.site.urls),
    # path("api/", include("waiter.urls"))
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
