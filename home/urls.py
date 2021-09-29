from os import name
from django.urls import path
from django.urls.conf import include 
from . import views
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about , name="about"),
    path("contact", views.contact , name="contact"),
    path("add_student", views.add_student , name="add_student"),
    path("view_student" , views.view_studend , name="view_student"),
    path("edit_info/<int:id>" , views.edit_info , name="edit_info"),
    path("update/<int:id>" , views.update , name="update"),
    path("delete/<int:id>" , views.delete , name="delete"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("media/(?P<path>.*)$" , serve,{'document_root': settings.MEDIA_ROOT}),
    path("static/?(P<path>.*)$", serve,{'document_root':settings.STATIC_ROOT}),
]
