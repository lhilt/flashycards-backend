import json

from django.contrib import auth
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

# Create your views here.

@require_http_methods(['POST'])
@csrf_exempt
def signup(request):
    new_user_info = json.loads(request.body)
    new_user_info.pop('password2')
    user = User.objects.create_user(
        **new_user_info,
        first_name='',
        last_name=''
    )
    user.save()
    auth.login(request, user)
    return JsonResponse({}, status=200)
