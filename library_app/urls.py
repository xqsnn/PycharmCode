from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('uLogin/', views.uLogin, name='uLogin'),
    path('uregister/', views.uregister, name='uregister'),
    path('aLogin/', views.aLogin, name='aLogin'),
    path('book_manage/', views.book_manage, name='book_manage'),#管理员管理页面
    path('book_manage/allbooks/', views.allbooks, name='allbooks'),#展示所有图书
    path('book_manage/allbooks/choose/', views.choose, name='choose'),#展示所有图书
    path('book_manage/delete/', views.book_manage_delete, name='book_manage_delete'),#删除指定图书
    path('book_manage/<int:nid>/edit/', views.book_manage_edit, name='book_manage_edit'),#编辑指定图书


    path('uLogin/uSpace/', views.uSpace, name='uSpace'),
    path('search_result/', views.search_result, name='search_result'),







]