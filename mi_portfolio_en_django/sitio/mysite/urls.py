from django.contrib import admin
from django.urls import path, re_path
from web import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    # Cualquier página adicional: /about, /contacto, /lo-que-sea
    re_path(r"^(?P<page>.+)/$", views.page, name="page"),
]