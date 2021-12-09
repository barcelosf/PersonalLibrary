from django import http
import django
from django.contrib import auth, messages
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .models import Book

# Home Page View
def home_page(request):
    return render(request, 'Home.html')

# Registration View
def register_page(request):
    return render(request, 'Registration.html')

# Login View
def login_page(request):
    return render(request, 'Login.html')

# User Registration Logic
def register_submit(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username =  request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user  = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        user.save()

        try:
            print("entrou no try")
            send_mail(subject="Confirmação de cadastro", message="Cadastro realizado com sucesso", from_email="personalibrary071@gmail.com", recipient_list=[email], fail_silently=False)
            print("Deu certo")
        except:
            print('Deu errado')

    return redirect(login_page)

# Login Logic
def login_submit(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect(list_books_page)
        else:
            return redirect(login_page)

# View for redirecting to the home page
def home_page_redirect(request):
    return redirect(home_page)

# Logout View
def logout_view(request):
    logout(request)
    return redirect(home_page_redirect)

# View that will list the books of the user
@login_required(login_url='/login/')
def list_books_page(request):
    usuario = request.user
    books = Book.objects.filter(Usuario=usuario)
    dados = {"books": books, "usuario": usuario}
    return render(request, 'BookList.html', dados)

# View that will delete the book
@login_required(login_url='/login/')
def delete_book(request, id_book):
    book = Book.objects.filter(id=id_book)
    book.delete()
    return redirect(list_books_page)

# View that will direct to the create page
@login_required(login_url='/login/')
def create_book(request):
    usuario = request.user
    dados = {"usuario": usuario}
    return render(request, 'CreateBook.html', dados)

# Book Creation
@login_required(login_url='/login/')
def create_book_submit(request):
    title = request.POST['title']
    presser = request.POST['presser']
    author = request.POST['author']
    pages = request.POST['pages']
    price = request.POST['price']
    description = request.POST['description']
    usuario = request.user
    Book.objects.create(Title=title,Presser=presser, Author=author, Pages=pages, Description=description, Price=price, Usuario=usuario)
    messages.success(request, 'Your Book was saved Successfully!!!!')
    return redirect(list_books_page)

# View that will direct to the update page
@login_required(login_url='/login/')
def update_book(request):
    id_book = request.GET.get('id')
    book = Book.objects.get(id=id_book)
    usuario = request.user
    dados = {"book": book, "usuario": usuario}
    return render(request,'UpdateBook.html',dados)

@login_required(login_url='/login/')
def update_book_submit(request, id_book):
    title = request.POST['title']
    presser = request.POST['presser']
    author = request.POST['author']
    pages = request.POST['pages']
    price = request.POST['price']
    description = request.POST['description']
    usuario = request.user
    id = id_book
    book = Book.objects.filter(id=id_book)
    book.update(Title=title,Presser=presser, Author=author, Pages=pages, Description=description, Price=price, Usuario=usuario)
    messages.success(request, 'Your Book was Updated Successfully!')
    return redirect(list_books_page)
