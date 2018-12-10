from django.conf.urls import url

from backweb import views

urlpatterns = [
    # 后台管理系统主页
    url(r'^index/', views.index),
    # 后台管理系统登录页面
    url(r'^login/', views.login),
    # 管理员注册
    url(r'^register/', views.register),
    # 注销
    url(r'^logout/', views.logout),

    # url(r'^my_index/', views.my_index),
    url(r'^article/', views.article, name='article'),
    # 公告
    url(r'^notice/', views.notice),
    # 添加文章
    url(r'^add_article/',views.add_article),
    # 删除文章
    url(r'^del_art_id/(\d+)/', views.del_art_id, name='del_art_id'),
    # 文章编辑
    url(r'^edit_art/(\d+)/', views.edit_art, name='edit_art'),

]