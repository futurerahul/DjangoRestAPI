from django.urls import path
from . import views

app_name='snippets'

urlpatterns = [
    path('snippets/', views.SnippetList.as_view() , name='SnippetList'),
    path('snippets/<int:pk>', views.SnippetDetail.as_view(), name='SnippetDetail'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
]