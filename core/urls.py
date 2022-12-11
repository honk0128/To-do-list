from operator import index
from django.urls import path, include
from . import views

from core.views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView


urlpatterns = [
  path('', views.index, name='index'),
  path('settings', views.settings, name='settings'),
  path('upload', views.upload, name='upload'),
  path('follow', views.follow, name='follow'),
  path('search', views.search, name='search'),
  path('like-post', views.like_post, name='like-post'),
  path('profile/<str:pk>', views.profile, name='profile'),
  path('signup', views.signup, name='signup'),
  path('signin', views.signin, name='signin'),
  path('logout', views.logout, name='logout'),
  path('about', views.about, name='about'),

  # tasks 추가
  path('tasks', TaskList.as_view(), name='tasks'),
  path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
  path('task-create/', TaskCreate.as_view(), name='task-create'),
  path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
  path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),

  # Calendar 추가
  path("calendar/", views.calendar, name="calendar"),
  path("create-template/", views.create_template, name="create-template"),
  path("delete-template/", views.delete_template, name="delete-template"),
  path("create-event/", views.create_event, name="create-event"),
  path("get-events/", views.get_events, name="get-events"),
  path("delete-event/", views.delete_event, name="delete-event"),
  path("day-plan/", views.day_plan, name="day-plan"),

  # chatting
  path('chat/', views.home, name='home'),
  path('chat/<str:room>/', views.room, name='room'),
  path('chat/checkview', views.checkview, name='checkview'),
  path('send', views.send, name='send'),
  path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
  ]