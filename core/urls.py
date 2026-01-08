from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    # SERVICES
    path('auth/', include('auth_service.urls')),
    path('', include('room_gateway.urls')),
    path('memory/', include('memory_service.urls')),
    path('response/', include('response_engine.urls')),
    path('moderation/', include('moderation_service.urls')),
    path('', include('dialogue_service.urls')),
    path('api/', include('audio_broadcast.urls')),
    path("response-engine/", include("response_engine.urls")),
    
    
    

]
