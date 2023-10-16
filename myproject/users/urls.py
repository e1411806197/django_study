from django.urls import path,re_path
from . import views


app_name='users'
urlpatterns = [

    path('<int:year>/',views.index,name='year'),
    path('index/',views.index2,name='index'),
    path('string/',views.find_string,name='string'),
    path('form/',views.find_form,name='form'),
    path('non_form/',views.find_noform,name='no_form'),
    path('test1/',views.test1,name='test1'),
    path('js_res/',views.js_res,name='js_res'),
    path('rect/',views.rect,name='rect'),
    path('demo_cookie/',views.demot_cookie,name='demo_cookie'),
    path('xxxx/',views.register.as_view(),name='ppo'),
    path('test2/',views.test2,name='test2'),
    path('test3/',views.test3,name='test3'),
    path('test4/',views.test4,name='test4'),
    path('test5/',views.test5,name='test5')
]
