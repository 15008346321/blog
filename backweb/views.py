from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from utils.functions import get_cookie_token, is_login
from django.core.paginator import Paginator
from backweb.Artform import AddArtForm, EditArtForm

# +++++++++++++++++++++++++++++++++++++++++登录功能+++++++++++++++++++++++++++++++++++++++
# 主页
from backweb.models import MyUser, Article


def index(request):
    if request.method == 'GET':

        return render(request, 'backweb/index.html')


# 登录

def login(request):
    if request.method == 'GET':
        return render(request, 'backweb/login.html')
    if request.method == 'POST':
        # 1. 获取登录提交的用户名和密码
        username = request.POST.get('username')
        password = request.POST.get('userpwd')

        # 2. 查询数据库中用户名和密码对应的用户对象
        user= MyUser.objects.filter(username=username, password=password).first()
        if not user:
            err = '用户名或密码错误'
            return render(request, 'login.html', {'err':err})
        # 3. 登录操作
        # 给予登录成功的标识符(令牌),存在于cookie中
        # res = HttpResponseRedirect('/my_index/')
        # token = get_cookie_token()
        # res.set_cookie('token', token, 900)
        # # 向TokenUser表中插入或更新数据
        # token_user = TokenUser.objects.filter(user=user).first()
        # if token_user:
        #     token_user.token = token
        #     token_user.save()
        # else:
        #     TokenUser.objects.create(token=token, user=user)

        # 3. 使用session实现登录操作
        # 3.1 向cookie中设置sessionid值,value为随机字符串
        # 3.2 向django_sessiong表中存入sessionid值,并保存键值对
        request.session['user_id'] = user.id
        # 4. 跳转到首页
        res = HttpResponseRedirect('/backweb/index/')
        return res
        # return render(request,'backweb/index.html',{'user':user})


# 注册
def register(request):
    if request.method == 'GET':
        # GET 访问http://127.0.0.1:8000/register/
        return render(request, 'backweb/register.html')
    if request.method == 'POST':
        # 1. 先获取注册的账号和密码和确认密码
        username = request.POST.get('username')
        password = request.POST.get('userpwd')
        password2 = request.POST.get('userpwd2')

        # 2.判断用户名是否已经被注册过
        user= MyUser.objects.filter(username=username).first()
        if user:
            err_name = '该账号已被注册,请重新输入'
            return render(request, 'register.html', {'err_name': err_name})

        # 3.判断密码和确认密码是否相同
        if password and password2:
            if password != password2:
                err_pwd = '两次输入密码不一致'
                data = {
                    'err_pwd': err_pwd
                }
                return render(request, 'register.html', data)
            else:
                # 4. 如果用户名不存在, 且密码和确认密码相同, 则实现注册, 保存数据
                user = MyUser()
                user.username = username
                user.password = password
                user.save()
                # return render(request,'login.html')
                return HttpResponseRedirect('/backweb/login/')
        else:
            err_pwd = '密码不能为空'
            return render(request, '/backweb/register.html', {'err_pwd':err_pwd})


# 注销
def logout(request):
    request.session.flush()
    return  HttpResponseRedirect('/backweb/login/')


# 公告页面
def notice(request):
    if request.method == 'GET':
        return render(request, '/backweb/notice.html')

# ++++++++++++++++++++++++++++++++++文章功能++++++++++++++++++++++++++++++++++++++++++++++++++
# 请求文章
def article(request):
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
        return render(request, 'backweb/article.html', {'page': page})


# 添加文章
def add_article(request):
    if request.method == 'GET':
        return render(request, 'backweb/add_article.html')

    if request.method == 'POST':
        # 把提交的数据丢给表单AddArtForm做验证
        form = AddArtForm(request.POST, request.FILES)
        # if_valid()验证参数是否有效,如果参数验证成功返回True,否则False
        if form.is_valid():
            # 表示字段验证成功
            title = form.cleaned_data['title']
            desc = form.cleaned_data['desc']
            content = form.cleaned_data['content']
            icon = form.cleaned_data['icon']
            Article.objects.create(title=title, desc=desc, content=content, icon=icon)

            return HttpResponseRedirect(reverse('user:article'))
        else:
            # 表示字段验证失败,需要将错误信息返回给页面展示
            return render(request, 'backweb/add_article.html', {'form':form})


# 删除文章
def del_art_id(request, id):
    if request.method == 'GET':
        # 查询文章并删除
        Article.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('user:article'))


# 编辑文章
def edit_art(request, id):
    if request.method == 'GET':
        article = Article.objects.filter(pk=id).first()
        return render(request, 'backweb/add_article.html', {'article': article})

    if request.method == 'POST':
        form = EditArtForm(request.POST, request.FILES)
        if form.is_valid():
            # 验证成功
            title = form.cleaned_data['title']
            desc = form.cleaned_data['desc']
            content = form.cleaned_data['content']
            icon = form.cleaned_data['icon']
            article = Article.objects.filter(pk=id).first()
            article.title = title
            article.desc = desc
            article.content = content
            if icon:
                article.icon = icon
            article.save()
            return  HttpResponseRedirect(reverse('user:article'))
        else:
            # 验证失败
            article = Article.objects.filter(pk=id).first()
            return render(request, 'backweb/add_article.html', {'form':form, 'article': article})
