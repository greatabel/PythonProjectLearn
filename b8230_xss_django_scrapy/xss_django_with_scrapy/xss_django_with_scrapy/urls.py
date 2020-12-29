from django.conf.urls import url,include
from django.contrib import admin
from app01 import views

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    # url(r'^index/$', views.index),
    url(r'^login/$', views.login),
    url(r'^register/$', views.register),
    url(r'^logout/', views.logout),
    url(r"^captcha/",include('captcha.urls')),
    url(r"^showbooks/$", views.showbooks,name="showbooks"),
    url(r"^addbook/$", views.addbook,name="addbook"),
    url(r"^delbook/$", views.delbook,name="delbook"),
    url(r"^editbook/(\d+)/$", views.editbook,name="editbook"),



]
'''
未登录人员，不论是访问index还是login和logout，全部跳转到login界面
已登录人员，访问login会自动跳转到index页面
已登录人员，不允许直接访问register页面，需先logout
登出后，自动跳转到login界面
'''