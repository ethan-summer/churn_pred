from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    path('fileupload/', include('fileupload.urls')),
    path('predictss/', include('prediction_service.urls')),
] + static('/images/', document_root='prediction_service/model/model_performance_output') \
  + static('/csv/', document_root='prediction_service/model/input_test')
