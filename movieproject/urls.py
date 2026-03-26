from django.contrib import admin
from django.urls import path, include
from movies import views as movie_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('login/', auth_views.LoginView.as_view(template_name='movies/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # App
    path('', movie_views.movie_list, name='home'),
    path('app/', include('movies.urls')),
    path('register/', movie_views.register, name='register'),
]