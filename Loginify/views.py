from django.shortcuts import render, redirect,  get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import UserDetails
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserDetailsSerializer


# Create your views here.
def hello_world():
    return HttpResponse("Hello World")


@api_view(['POST'])
def create_user(request):
    serializer = UserDetailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User created successfully!", "user": serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 📌 Get All Users (GET)

@api_view(['GET'])
def get_all_users(request):
    users = UserDetails.objects.all()
    serializer = UserDetailsSerializer(users, many=True)
    return Response(serializer.data)

# Update User (PUT)
@api_view(['PUT'])
def update_user(request, email):
    try:
        user = UserDetails.objects.get(email=email)
    except UserDetails.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserDetailsSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User updated successfully!", "user": serializer.data})
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Delete User (DELETE)
@api_view(['DELETE'])
def delete_user(request, email):
    try:
        user = UserDetails.objects.get(email=email)
    except UserDetails.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    user.delete()
    return Response({"message": "User deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)

# Get User by Email (GET
@api_view(['GET'])
def get_user_by_email(request, email):
    try:
        user = UserDetails.objects.get(email=email)
    except UserDetails.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserDetailsSerializer(user)
    return Response(serializer.data)



def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if UserDetails.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('signup')
        user = UserDetails(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Signup successful! Please login.")
        return render(request, 'Loginify/login.html')
        

    return render(request, 'Loginify/signup.html')


def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        if UserDetails.objects.filter(email=email, password=password).exists():
            messages.success(request, "Login successful!")
            return HttpResponse("Login successful")
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('login')
    return render(request, 'Loginify/login.html')


    
