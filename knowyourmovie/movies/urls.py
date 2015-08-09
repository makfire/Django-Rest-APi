from django.conf.urls import include, url,patterns
from movies import views
urlpatterns = patterns('',
			(r'^login/$',views.login_check.as_view()),
			(r'^api/$',views.movielist.as_view()),
			(r'^api/(?P<token>[\w-]+)/$',views.movielist.as_view()),
			(r'^api/(?P<pk>[\w-]+)/$',views.single_view.as_view()),
			(r'^api/(?P<pk>[\w-]+)/(?P<token>[\w-]+)/$',views.single_view.as_view()),
			
			)



