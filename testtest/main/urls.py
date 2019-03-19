from django.conf.urls import url
from django.contrib import admin
from main import views
urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^$', views.index, name='index'),
  url(r'^register/$',views.register,name='register'),
  url(r'^user_login/$',views.user_login,name='user_login'),
  url(r'^logout/$', views.user_logout, name='logout'),
  url(r'^special/',views.special,name='special'),
]
