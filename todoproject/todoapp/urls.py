from django.contrib import admin
from django.urls import path

from . import views
app_name='todoapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.task, name='task'),
    path('delet/<int:tid>/', views.delete, name='delet'),
    path('update/<int:id>/', views.updatetask, name='update'),

    path('home/', views.Tasklist.as_view(), name='homes'),
    path('detail/<int:pk>/', views.Taskdetail.as_view(), name='detail'),
    path('updates/<int:pk>/', views.Taskupdate.as_view(), name='updates'),
    path('deleter/<int:pk>/', views.Taskdelete.as_view(), name='deleter')
]
