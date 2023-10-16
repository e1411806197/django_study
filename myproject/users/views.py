
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import redirect,render
import json
from django.views.generic import View
from django.utils.decorators import method_decorator
from .models import BookInfo
# Create your views here.


def outer(func):
    print('--------')
    def inner(request,*args):
        print('222222222')
        return func(request)
    return inner

class register(View):
    @method_decorator(outer)
    def get(self,request):
        print('hhhhhh')
        return HttpResponse('222')

    @method_decorator(outer)
    def post(self,request):
        print('zzzz')
        return HttpResponse('kkkk')




def index(request,year):

    url=reverse('users:index')
    print(url)
    return HttpResponse(f'hello world {year}')

def index2(request):
    cointext={'city':'北京'}


    return render(request,'index.html',context=cointext)



def find_string(request):
    a=request.GET.get('a')
    b=request.GET.get('b')
    alist=request.GET.getlist('c')
    print(a)
    print(b)
    print(alist)
    print(type(alist))
    return HttpResponse('666666666')


def find_form(request):
    s=request.POST.get("ss")
    kk=request.POST.get("kk")
    print(s)
    print(kk)
    return HttpResponse('ok')


def find_noform(request):
    content=request.body
    mes=json.loads(content)
    print(mes['a'])
    print(mes['b'])
    return HttpResponse('kkkkkkzzzzz')


def test1(request):
    response=HttpResponse()
    response['lis']='python'
    response['ppp']='zzz'
    response.status_code=207
    return response


def js_res(request):
    return JsonResponse({'ssss':2222,'kkkk':7777})


def rect(request):
    return redirect('http://www.baidu.com')


def demo_cookie(request):
    cokies=request.COOKIES
    print(cokies.get('csrftoken'))
    return HttpResponse('pppp')

def demot_cookie(request):
    response = HttpResponse('ok')
    response.set_cookie('itcast1', 'python1')  # 临时cookie
    response.set_cookie('itcast2', 'python2', max_age=3600)  # 有效期一小时
    return response

def test2(request):
    if request.method=='GET':
        book=BookInfo(1,'天龙八部','2022-03-04')
        book.save()
        return HttpResponse('添加成功')
def test3(request):
    if request.method=='GET':
        book=BookInfo.objects.get(id=2)
        book.delete()
        return HttpResponse('delete successful')


def test4(request):
    if request.method == 'GET':
        book = BookInfo.objects.get(id=1)
        book.btitle='我的名字叫顺溜'
        book.save()
        return HttpResponse('修改成功')


def test5(request):
    if request.method=='GET':
        book=BookInfo.objects.all()
        print(book)
        return HttpResponse('all ok')

