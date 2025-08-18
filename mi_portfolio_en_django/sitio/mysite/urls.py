from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

#from django.contrib import admin
#from django.urls import path, re_path, include
#from web import views

#urlpatterns = [
#    path("admin/", admin.site.urls),
#    path('', include('blog.urls')),
#    # Cualquier página adicional: /about, /contacto, /lo-que-sea
#    re_path(r"^(?P<page>.+)/$", views.page, name="page"),
#]""