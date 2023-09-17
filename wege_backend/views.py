from django.shortcuts import render, redirect
from django.views import View
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import UserinfoSerializer
from .models import UserInfoTable
from django.http import JsonResponse
import json



class IndexView(View):
    def get(self, request):
        '''
         This method called when user hit root url
         @params:
            request (object): http GET request object

         @returns:
            render signup.html  page
        '''
        signup_form = {"form": RegistrationForm}
        return render(request, "signup.html", signup_form)


class AddUserView(View):
    def post(self, request):
        '''
        This method allow user to get register on this app
         @params:
            request (object): http POST request object

         @returns:
           redirect on failure of user registration and  render home page in success of user registration
        '''
        input_form_obj = RegistrationForm(request.POST)
        if input_form_obj.is_valid():
            input_form_obj.save()

        else:
            error_string = "<br>".join(
                [error[0] for error in input_form_obj.errors.values()])
            messages.add_message(request, messages.ERROR, error_string)
            return redirect("error_page")

        messages.add_message(request, messages.SUCCESS,
                             "Registration Was Successful!!!")
        return render(request, "home.html")


class ErrorView(View):
    def get(self, request):
        '''
         This method will be call to display custom error message
          @params:
            request (object): http GET request object

          @returns:
            render error_page.html page
        '''
        return render(request, "error_page.html")


class LoginView(View):
    def get(self, request):
        '''
         This method will be call when user hit login endpoint
          @params:
            request (object): http GET request object

          @returns:
            render login_page.html page
        '''
        login_form = {"form": LoginForm}
        return render(request, "login_page.html", login_form)


class Get_UserInfo_API(APIView):
    def post(self, request):
        '''
         This method serves RestAPI endpoint which authenticate valid user using JWT and returns his information
          @params:
            request (object): http POST request object with JWT in the header

          @returns:
             json response which contain user information on successful user based on jwt valdiation else failed validation error
        '''
        permission_classes = [IsAuthenticated,]
        username = json.loads(request.body)["username"]
        data = UserInfoTable.objects.values().get(username=username)
        serializer = UserinfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

        return JsonResponse(serializer.data)


class HomeView(View):
    def get(self, request):
        '''
         This method will be called upon on successful JWT authentication
          @params:
            request (object): http GET request object

           @returns:
             render home.html page
        '''
        if request.COOKIES.get("access_token"):
            messages.add_message(request, messages.SUCCESS,
                                 "Your authenticated via JWT successfully!!!")

        return render(request, "home.html")
