from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from members import views


urlpatterns = [
    path('members/', views.members, name='members'),
    path('members/insert', views.insert, name='insert'),
    path('memberlist/', views.MemberList.as_view()),
    path('memberlist/<int:pk>/', views.MemberDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)