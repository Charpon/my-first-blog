from django.conf.urls import url
import blog.views

urlpatterns = [
	url(r'^$', blog.views.post_list, name='post_list'),
	url(r'^post/(?P<pk>\d+)/$', blog.views.post_detail, name='post_detail'),
	url(r'^post/new/$', blog.views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', blog.views.post_edit, name='post_edit'),
	url(r'^drafts/$', blog.views.post_draft_list, name='post_draft_list'),
	url(r'^post/(?P<pk>\d+)/publish/$', blog.views.post_publish, name='post_publish'),
	url(r'^post/(?P<pk>\d+)/remove/$', blog.views.post_remove, name='post_remove'),
	url(r'^post/(?P<pk>\d+)/comment/$', blog.views.add_comment_to_post, name='add_comment_to_post'),
	url(r'^comment/(?P<pk>\d+)/approve/$', blog.views.comment_approve, name='comment_approve'),
	url(r'^comment/(?P<pk>\d+)/remove/$', blog.views.comment_remove, name='comment_remove'),
]