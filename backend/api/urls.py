from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
# from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from . import views

app_name = 'api'

# router = routers.SimpleRouter()

urlpatterns = [
    path('v1/csrf/', views.CsrfView.as_view(), name='csrf'),
    path('v1/login/', views.LoginView.as_view(), name='login'),
    path('v1/logout/', views.LogoutView.as_view(), name='logout'),
    path('v1/authenticate/', views.AuthenticateView.as_view(), name='authenticate'),

    path('v1/service-type/', views.ServiceTypeListView.as_view(), name='service-type'),
    path('v1/service-type/<int:pk>/', views.ServiceTypeDetailView.as_view(), name='service-type-pk'),

    path('v1/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('v1/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('v1/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

# urlpatterns += router

urlpatterns = format_suffix_patterns(urlpatterns)
