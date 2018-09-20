from django.conf.urls import include, url
from post import views
from django.contrib import admin

urlpatterns=[
    url(r'^$' , views.home , name = 'home'),
    url(r'^login/', views.login_site , name = 'login'),
    url(r'^signup/' , views.signup , name = 'signup'),
    url(r'^posts/add/$' , views.addpost , name = 'addposts'),
    url(r'^blogs/$' , views.blogs , name = 'blogview'),
    url(r'^blogs/add/$' , views.add_b , name = 'addblog'),
    url(r'^logout/' , views.logout_req , name = 'logout'),
    url(r'^blogs/delete/(?P<pk>\d+)/',views.delete_b,name='deleteblog'),
    url(r'^posts/delete/(?P<pk>\d+)/',views.delete_p,name='deletepost'),
    url(r'^blogs/edit/(?P<pk>\d+)/',views.edit_b,name='edit_blog'),
    url(r'^posts/edit/(?P<pk>\d+)/',views.edit_p,name='edit_post'),
    url(r'^admin/', include(admin.site.urls)),

]