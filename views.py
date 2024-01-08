from django.shortcuts import render
from .models import Member
from members.models import Member
from members.serializers import MemberSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from members.permissions import IsOwnerOrReadOnly

def data(request):
        if request.method == 'POST':
            if request.POST.get('username') and request.POST.get('password'):
                post=Member()
                post.username= request.POST.get('username')
                post.password= request.POST.get('password')
                post.save()
                
                return render(request, 'insert.html')
        else:
             return render(request,'data.html')

class MemberList(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
         serializer.save(owner=self.request.user)

class MemberDetail(generics.RetrieveAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]

'''class UserList(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserDetail(generics.RetrieveAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]'''