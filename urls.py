from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from members import views

urlpatterns = [
    path('members/abc/',views.abc, name='abc'),
    path('members/', views.members, name='members'),
    path('memberlist/', views.UserList.as_view()),
    path('memberlist/<int:pk>/', views.UserDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)






