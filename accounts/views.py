import json

from django.contrib import auth
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

# Create your views here.

def sendToken(request):
    return JsonResponse({'message': 'welcome'}, status=200)


@require_http_methods(['POST'])
@csrf_exempt
def signup(request):
    new_user_info = json.loads(request.body)
    username = new_user_info['username']
    email = new_user_info['email']

    errors = {}
    if User.objects.filter(username=username).exists():
        errors['username'] = 'Username is taken'
    if User.objects.filter(email=email).exists():
        errors['email'] = 'Invalid email'

    if not errors:
        new_user_info.pop('password2')
        user = User.objects.create_user(
            **new_user_info,
            first_name='',
            last_name=''
        )
        user.save()
        auth.login(request, user)
        return JsonResponse({}, status=200)
    else:
        return JsonResponse(errors, status=400)


@require_http_methods(['POST'])
@csrf_exempt
def login(request):
    user_info = json.loads(request.body)
    username = user_info['username']
    password = user_info['password']

    user = auth.authenticate(
        username=username,
        password=password
    )
    if user is not None:
        auth.login(request, user)
        return JsonResponse({'username': username}, status=200)
    else:
        error = {'error': 'Invalid credentials'}
        return JsonResponse(error, status=400)


def logout(request):
    auth.logout(request)
    return JsonResponse({'message': 'logout successful'}, status=200)
