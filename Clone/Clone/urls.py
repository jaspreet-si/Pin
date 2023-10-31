"""
URL configuration for Clone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from pinapp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('signin/',views.Login,name='signin'),
    path('signup/',views.Signup,name='signup'),
    path('upload/',views.addpin,name='upload'),
    path('profilepage/',views.profilepage,name='profileprofile'),
    path('addprofile/',views.addprofile,name='addprofile'),
    path('logout/',views.logout,name='logout'),
    path('search/',views.search,name='search'),
     path('readMore/<int:id>',views.readMore,name='readMore'),
    path('CommentBox/<int:id>/<str:Post>',views.CommentBox,name='Commentbox'),
    path('DeleteCommentById/<int:id>/<int:postid>',views.DeleteCommentById,name='deletecomment'),
    path('LikePin/<int:id>',views.LikePin,name='LikePin'),
    path('deletePin/<int:id>',views.deletePin,name='DeletePin'),
    path('user_uploaded',views.user_profile,name="user_uploaded")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
