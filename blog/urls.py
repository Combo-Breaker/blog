from django.conf.urls import include, url
from . import views
#from blog.views import board_list, post_list
from blog.views import board_list


urlpatterns = [
	url(r'^$', views.board_list, name='board_list'),
	url(r'^board/(?P<pk>[0-9]+)/$', views.board_detail, name='board_detail'),
	#url(r'^$', board_list.as_view(), name='board_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/board/(?P<bd>[0-9]+)$', views.post_new, name='post_new'),
	#url(r'^flood/', views.post_list, name='post_list'), #тындын
	# url(r'^list/$', 'list', name='list'),
	#url(r'^(?P<slug>[-_\w]+)/$', post_detail.as_view(), name='article'),
	#url(r'^board/(?P<slug>[-_\w]+)/$', board_list.as_view(), name='board'),
	# url(r'^post/(?P<slug>[-_\w]+)/$', post_list.as_view(), name='board_list'),
	]

