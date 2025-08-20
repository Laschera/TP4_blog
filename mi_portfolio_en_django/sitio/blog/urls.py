from django.urls import path
from . import view

app_name = 'blog'

urlpatterns = [
    path('', view.post_list, name='post_list'),
    path('post/<int:pk>/', view.post_detail, name='post_detail'),
    path('post/new/', view.post_new, name='post_new'),
    path('post/<int:pk>/edit/', view.post_edit, name='post_edit'),
    path('post/<int:pk>/comment/', view.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', view.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', view.comment_remove, name='comment_remove'),
]