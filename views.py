from django.shortcuts import render
from .forms import InputForm
from .models import Member
from members.models import Member
from members.serializers import MemberSerializer
from rest_framework import mixins
from rest_framework import generics

def members(request):
    context={}
    context['form']=InputForm()
    return render(request, "print.html", context)

def insert(request):
    if request.method == 'POST':
        if request.POST.get('firstname') and request.POST.get('lastname') and request.POST.get('roll_number') and request.POST.get('age') and request.POST.get('subject') and request.POST.get('city'):
            post=Member()
            post.firstname= request.POST.get('firstname')
            post.lastname= request.POST.get('lastname')
            post.roll_number= request.POST.get('roll_number')
            post.age= request.POST.get('age')
            post.subject= request.POST.get('subject')
            post.city= request.POST.get('city')
            post.save()

            return render(request, 'tabel.html')
        else:
            return render(request,'print.html')
        
class MemberList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class MemberDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)