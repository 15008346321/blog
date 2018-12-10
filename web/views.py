from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from web.article_filter import ArticleFilter
from backweb.models import Article
from web.article_serializer import ArtcileSerializer
from django.core.paginator import Paginator



# def index(request):
#     if request.method == 'GET':
#
#         return render(request, 'web/index.html')
#
#
# class ArticleView(viewsets.GenericViewSet,
#                   mixins.ListModelMixin,
#                   mixins.DestroyModelMixin,
#                   mixins.CreateModelMixin,
#                   mixins.UpdateModelMixin,
#                   mixins.RetrieveModelMixin):
#
#     # 查询返回的数据
#     queryset = Article.objects.filter(is_delete=0)
#     # 序列化返回的数据
#     serializer_class = ArtcileSerializer
#     # 过滤
#     filter_class = ArticleFilter
#
#     def perform_destroy(self, instance):
#         instance.is_delete = 1
#         instance.save()
#
#     def retrieve(self, request, *args, **kwargs):
#         try:
#             instance = self.get_object()
#             serializer = self.get_serializer(instance)
#             return Response(serializer.data)
#         except:
#             data = {}
#             data['code'] = 500
#             data['msg'] = '获取数据失败'
#
#     def get_queryset(self):
#         search_title = self.request.GET.get('title')
#         search_desc = self.request.GET.get('desc')
#         search_content = self.request.GET.get('content')
#
#         # 既要搜索title, desc, content
#         return self.queryset.filter(title__contains=search_title, desc__contains=search_desc, content__contains=search_content)


def list_art(request):
    if request.method == 'GET':
        return render(request, 'index.html')

def index(request):
    if request.method == 'GET':
        # 文章列表页面
        page = int(request.GET.get('page', 1))
        # page = request.GET.get('page') if request.GET.get('page') else 1
        # 第一种: 使用切片完成分页
        # articles = Article.objects.all()[(page-1) * 2 : page * 2]
        # 第二种
        # from django.core.paginator import Paginator
        articles = Article.objects.all()
        # 将所有数据按照每一页2条数据进行切块处理
        paginator = Paginator(articles, 2)
        # 获取分页中的第几页数据
        page = paginator.page(page)
        return render(request, 'web/index.html', {'page':page})
