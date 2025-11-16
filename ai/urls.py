from django.urls import path
from . import views, ai_views
app_name = 'ai'
urlpatterns = [
    path('chat/', views.startchat, name='startchat'),
    path('settings/', views.ai_settings, name='settings'),
    path('chat/<uuid:session_id>/', views.chatinterface, name='chatinterface'),
    path('v1/', ai_views.ai_v1_view, name='v1'),
  ]
