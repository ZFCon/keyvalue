from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView

router = routers.DefaultRouter()
router.register(r'keyvalue-pair', views.KeyValuePairView)
router.register(r'keyfile-pair', views.KeyFilePairView)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('sign-up/', views.UserSignUpView.as_view(), name='sign-up'),
    path('', include(router.urls)),
]