from django.conf.urls import url
from rest_framework.routers import SimpleRouter
from web import views
# 生成路由对象
router = SimpleRouter()

# 路由管理资源
# router.register('art',views.ArticleView)

urlpatterns = [
    # 博客首页
    # 127.0.0.1:8090/web/index/
    url(r'^index/', views.index),
    url(r'^list/', views.list_art),

]
# router.urls 生成资源对应的路由地址
urlpatterns += router.urls