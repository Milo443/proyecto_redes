"""
URL configuration for client project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from ftpclient import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('archivos/', views.archivos, name='archivos'),

    path('upload/', views.upload, name='upload'),
    path('upload_directory/<str:directory>', views.upload_directory, name='upload_directory'),

    path('download/<str:file_name>', views.download, name='download'),
    path('download_files/<str:directory>/<str:file_name>', views.download_files, name='download_files'),

    path('delete/<str:file>', views.delete, name='delete'),
    path('delete_directory/<str:directory>', views.delete_directory, name='delete_directory'),
    path('delete_files/<str:directory>/<str:file>', views.delete_files, name='delete_files'),

    path('rename/<str:file>', views.rename, name='rename'),
    path('create_directory/', views.create_directory, name='create_directory'),
    #path('navigate/<str:directory>', views.navigate, name='navigate'),
    path('directory/<str:directory>', views.directory, name='directory'),


]
