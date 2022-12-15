from django.http import JsonResponse
from django.http.request import HttpRequest
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from rest_framework import viewsets,request
from rest_framework.views import APIView
from .sender import MemberSerializer, RecordSerializer
from .models import Member, Record
from django.views.decorators.csrf import csrf_exempt,csrf_protect

# Create your views here.

class MemberView(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()

class RecordView(viewsets.ModelViewSet):
    serializer_class = RecordSerializer
    queryset = Record.objects.all()

class LoginView(View):
    # request: http.HttpRequest
    
    def post(self,request:request.HttpRequest):
        # print(request.content_type)
        # print(request.content_params)
        user = request.POST.get('user','') 
        print("Login View: user: ",user)
        password = request.POST.get('password','')
        print("Login View: password: ",password)

        # check if user is in Member list 
        if Member.objects.filter(name=user).exists():
            print("member exists")    
            userAuth = authenticate(request=request,username = user,password= password)
            if userAuth is not None:               
                # login(request, userAuth)
                print(userAuth, " logged in")
                # Return a success response
                
                return JsonResponse({'200': 'success'})

            else:
                # The user is not in database, create a new user
                tempUser = User.objects.create_user(user, password='password')
                tempUser.save()
                print("new user created")
                return JsonResponse({'200': 'success'})

        else:
            print("user not in member list")
            return JsonResponse({'200': 'Not exist'})


# class LogoutView(APIView): # TODO: log a problem: View will throw "not match trusted origins"
#     def log(self,request): # TODO: log a problem occured. should alwasy use 'def post()'
# # def LogoutView(request:request.HttpRequest):
#         print("logout function")
#         logout(request)
#         print("user log out")
#         return JsonResponse({"200":"user logout"})

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        print("user logout")
        # redirect(to="/")
        return JsonResponse({"success": "Successfully logged out."})

# @csrf_exempt
# def logout_view(request):
#     return LogoutView.as_view()(request)

    