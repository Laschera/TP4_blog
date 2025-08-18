from django.contrib import admin
from django.urls import path, re_path, include
from web import views
from blog import view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path('blog/', include('blog.urls')),
    path('post/new/', view.post_new, name='post_new'),
    path('post/<int:pk>/', view.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', view.post_edit, name='post_edit'),
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