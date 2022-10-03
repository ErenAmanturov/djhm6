"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from posts.views import main, post_detail, create_post
from django.conf.urls.static import static
from django.conf import settings
from users.views import register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('posts/<int:id>/', post_detail),
    path('posts/create/', create_post),
    path('users/register/', register_view),
    path('users/login/', login_view),
    path('users/logout/', logout_view)
    # path('posts/<posts_id>/edit/', edit_post)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
