from django.contrib import admin
from django.urls import include, path
from api import views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('courses',views.CourseViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls))

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
