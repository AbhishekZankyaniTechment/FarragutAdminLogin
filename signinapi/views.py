# from django.shortcuts import render , redirect
# from django.http import HttpResponse
# from .models import Test
# from .serializers import TestSerializer
# from django.contrib import messages


# Create your views here.

from django.contrib.auth import get_user_model

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    UserModel View.
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


# def login(request):

    # if request.method == 'POST':
    #     email = request.POST['email']
    #     password = request.POST['password']
    # return HttpResponse("DONE FOR NOW")
        # user = Test.authenticate(email = email, password =password  )

        # if user is not None:
            # auth.login(request , user)
            # return redirect('/home')
        # else:
            # messages.info(request, 'invalid username or password')
            # return redirect("/")
    # else:
        # return render(request,'index.html')
