from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from waiter import views

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('table/', views.waiter_table_list),
    path('table/<int:id>/', views.waiter_table_detail),
    path('table/create/', views.create_table_from_user),
    path('table/assign/', views.assign_to_waiter),
    path('table/update/', views.update_table_status),
    path('table/check-assign/<int:pk>/', views.check_assign),
]