import json

from django.shortcuts import render,redirect
import library_app.models as models
import os
from django.db.models import Q
from django.http import JsonResponse

book_path='static/img/'

# Create your views here.
from django.shortcuts import render
from library_app.models import library_book

# Create your views here.
def main(request):
    #图书馆主页面
    if request.method == 'GET':
        img_name=[]
        for file_name in os.listdir(book_path):
            name = os.path.join(book_path, file_name)
            name = '/' + name
            img_name.append(name)
        print(img_name[1])
        return render(request, 'main.html',{'img_name':img_name,'log_meg':0})

def uregister(request):
    #用户注册账号
    if request.method == 'GET':
        return render(request,'uregister.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')
        print(username, password)
        if models.user_account.objects.filter(name=username).exists():
            return render(request,'uregister.html', {"error_meg":"用户名已存在！请重新注册！"})
        else:
            if password != confirm_password:
                return render(request,'uregister.html', {"error_meg":"两次密码不一致！"})
            else:
                models.user_account.objects.create(name=username,password=password)
                return render(request,'uregister.html', {"error_meg":"注册成功，请前往登录！"})

def uLogin(request):
    #用户登录账号
    if request.method == 'GET':
        return render(request, 'uLogin.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if models.user_account.objects.filter(name=username).exists():
            if models.user_account.objects.filter(name=username,password=password):
                return render(request,'main.html', {"log_meg":1})
            else:
                return render(request, 'uLogin.html', {"error_meg": "密码错误！请重新输入！"})
        else:
            return render(request, 'uLogin.html', {"error_meg": "用户不存在，先注册！"})

def search_result(request):
    # 用户 查询图书结果
    if request.method == 'GET':
        search_info = request.GET.get('search_info')
        result = models.library_book.objects.filter(Q(book_name=search_info) | Q(book_author=search_info))
        return render(request, 'search_result.html', {"result": result})

def aLogin(request):
    #管理员登录账号
    if request.method == 'GET':
        return render(request, 'aLogin.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if models.admin_account.objects.filter(name=username).exists():
            if models.admin_account.objects.filter(name=username,password=password):
                return redirect('book_manage')
            else:
                return render(request, 'aLogin.html', {"error_meg": "密码错误！请重新输入！"})
        else:
            return render(request, 'aLogin.html', {"error_meg": "用户不存在，请联系工作人员开通权限！"})

def book_manage(request):
    #管理员 图书管理页面
    if request.method == 'GET':
        return render(request,'book_manage.html')

def allbooks(request):
    #管理员 图书馆所有图书
    if request.method == 'GET':
        data = models.library_book.objects.all()
        catalog = models.library_book_catalog.objects.all()
        return render(request, 'allbooks.html', {"data": data,"catalog": catalog})
    if request.method == 'POST':
        name = request.POST.get('input_name')
        author = request.POST.get('input_author')
        catalog = request.POST.get('input_catalog')
        number = request.POST.get('input_number')
        time = request.POST.get('input_time')
        if models.library_book.objects.filter(book_name=name).exists():
            obj = models.library_book.objects.filter(book_name=name)
            number = int(number) + obj[0].number_of_books
            models.library_book.objects.filter(book_name=name).update(number_of_books=number,time_into=time)
        else:
            models.library_book.objects.create(book_name=name, book_author=author, book_catalog=catalog,time_into=time, number_of_books=number)
        data = models.library_book.objects.all()
        return render(request, 'allbooks.html', {"data": data})
def choose(request):
    value = request.GET.get('value')
    catalog = models.library_book_catalog.objects.filter(id=value).first()
    book_catalog = catalog.library_book_catalog
    data = models.library_book.objects.filter(book_catalog=book_catalog)

    return JsonResponse(json.dumps(data))


def book_manage_delete(request):
    #管理员 删除图书操作
    # http://127.0.0.1:8000/library/book_manage/delete/?book_name=
    if request.method == 'GET':
        book_id = request.GET.get('book_id')
        print(book_id)
        models.library_book.objects.filter(id=book_id).delete()
        return redirect('/library/book_manage/allbooks')



def book_manage_edit(request,nid):
    if request.method == 'GET':
        book = models.library_book.objects.filter(id=nid).first()
        return render(request, 'book_manage_edit.html',{'book':book})
    if request.method == 'POST':
        name = request.POST.get('input_name')
        author = request.POST.get('input_author')
        catalog = request.POST.get('input_catalog')
        number = request.POST.get('input_number')
        time = request.POST.get('input_time')
        models.library_book.objects.filter(book_name=name).update(book_name=name, book_author=author,
                                                                  book_catalog=catalog, number_of_books=number,
                                                                  time_into=time)
        return redirect('/library/book_manage/allbooks/')
def uSpace(request):
    return render(request,'uSpace.html')