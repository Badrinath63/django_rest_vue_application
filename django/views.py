from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

from .models import Person
from .serializers import PersonSerializer, PersonSerializer_Without_PWD
import requests

@csrf_exempt
def signup(request):
    """
    User signup endpoint
    """
    if request.method == 'POST':

        data = JSONParser().parse(request)
        serializer = PersonSerializer(data=data)
        print("data",data)
        email = data["email"]
        full_name=data["full_name"]
        if Person.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already registered'}, status=400)
        if(serializer.is_valid()):
            serializer.save()
            send_mail(request,email,full_name)
            return JsonResponse({'message': 'Signup successful'}, status=200)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

def send_mail(request,email,fullname):
    key = '2eadc4ccd551239ad6f0beb862a7ec3b-6d1c649a-f67f0bba'
    msg = 'Thanks for signup and welcome to '+fullname
    request_url = 'https://api.mailgun.net/v3/sandbox20833315b09f4024a8e2eefd952ad3b6.mailgun.org/messages'
    request = requests.post(request_url, auth=('api', key), data={
        'from': 'badrinath63037984@gmail.com',
        'to': [email],
        'subject': 'Welcome Mail',
        'text': msg
    })

    print('Status: {0}'.format(request.status_code))



@csrf_exempt
def login(request):
    """
    User login endpoint
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        print("data", data)
        email = data["email"]
        password = data["password"]

        # Authenticate the person
        try:
            persons = Person.objects.filter(email=email,password=password)
            if len(persons)==1:
                return JsonResponse({'message': 'Login successful'},status=200)
        except Exception as e:
            print(e)


        return JsonResponse({'error': 'Invalid credentials'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


def view_profile(request, person_email):
    try:
        person = Person.objects.get(email=person_email)
        serializer = PersonSerializer_Without_PWD(person)
        return JsonResponse(serializer.data)
    except Person.DoesNotExist:
        return JsonResponse({'error': 'Person not found'}, status=404)
