"""LibraryManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Views
from Livraria import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page),
    path('register/', views.register_page),
    path('/home/', views.home_page_redirect),
    path('login/', views.login_page),
    path('register/registration', views.register_submit),
    path('login/submit', views.login_submit),
    path('books/', views.list_books_page),
    path('logout', views.logout_view),
    path('books/delete/<int:id_book>', views.delete_book),
    path('create', views.create_book),
    path('creation', views.create_book_submit),
    path('books/update/',views.update_book),
    path('books/update/new/<int:id_book>', views.update_book_submit)
]
