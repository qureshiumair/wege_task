from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path("", views.IndexView.as_view(), name="home_page"),
    path("add_user", views.AddUserView.as_view(), name="add_user"),
    path("error_page", views.ErrorView.as_view(), name="error_page"),
    path("login", views.LoginView.as_view(), name="login_page"),
    path('new_token',jwt_views.TokenObtainPairView.as_view(),name='new_token'),
    path('refresh_token',jwt_views.TokenRefreshView.as_view(),name='token_refresh'),
    path('get_userinfo_api',views.Get_UserInfo_API.as_view(),name="get_userinfo_api"),
    path('home',views.HomeView.as_view(),name="home"),
]

