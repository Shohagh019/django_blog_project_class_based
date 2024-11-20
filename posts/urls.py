from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('add/', views.CreatePost.as_view(), name = 'add_post'),
    path('edit/<int:id>/', views.EditPost.as_view(), name = 'edit_post'),
    path('delete/<int:id>/', views.DeletePost.as_view(), name = 'delete_post'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)