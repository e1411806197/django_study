from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse

class M1(MiddlewareMixin):

        # ss=request.GET.get('a')
        # zz=request.GET.get('b')
        # return HttpResponse(f'{ss,zz}')

    def process_response(self,request,response):
        return response
        # return HttpResponse('kkkkkkk')


class M2(MiddlewareMixin):
    def process_request(self,request):
        print('kkkkk')
        return HttpResponse('hello')



    def process_response(self,request,response):
        return HttpResponse('zzzzzzz')



