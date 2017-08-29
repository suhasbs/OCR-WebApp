from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^$', views.index, name = 'index'), 
	url(r'^upload/$', views.upload, name='upload'),
	url(r'^(?P<imgid>\d+)/get_data/$', views.get_data, name = 'get_data'),
]
