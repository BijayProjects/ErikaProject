from django.urls import path
from .import views

urlpatterns =[
    path('',views.index,name='index'),
    path('blog/',views.blog, name='blogpage'),
    path('Blog=showBlog/<int:id>',views.showBlog,name='showblog'),
    path('booking=?Erika/',views.Book.book,name='books'),
    path('News_mail_Receive=?/',views.Book.info_Email,name='info_email'),
    path('about/',views.About.about,name='about'),
    path('tools/',views.Tools.tools,name='tools'),
    path('books/',views.Books.books,name='books'),
]