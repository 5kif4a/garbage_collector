from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index),
    path('dumps', views.dumps),
    path('events', views.events),
    path('dumps/<int:id>/', views.dump_by_id),
    path('events/<int:id>', views.event_by_id)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

