from django.shortcuts import render, HttpResponse, redirect
import pickle
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile
# from .forms import QuestionForm

# Create your views here.

with open('C:/Users/shrinidhi/Downloads/prediction.pkl', 'rb') as f:
    model = pickle.load(f)


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')  # Redirect to the home page after successful login
        else:
            return render(request, 'test/signin.html', {'error': 'Invalid credentials'})

    return render(request, 'test/signin.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = User.objects.create_user(username=username, email=email, password=password)
        introvert_extrovert_result = 'Extrovert' #default le lega 
        UserProfile.objects.create(user=user, introvert_extrovert_result=introvert_extrovert_result,
                                   user_name=username, email=email)



        login(request, user)

        return redirect('main')  

    return render(request, 'test/register.html')

def signout(request):
    logout(request)
    return redirect('main')

def home(request):
    return render(request, 'test/home.html')

def main(request):
    if request.method == 'POST':
        question1 = int(request.POST.get('question1'))
        question2 = int(request.POST.get('question2'))
        question3 = int(request.POST.get('question3'))
        question4 = int(request.POST.get('question4'))
        question5 = int(request.POST.get('question5'))
        question6 = int(request.POST.get('question6'))
        question7 = int(request.POST.get('question7'))
        question8 = int(request.POST.get('question8'))
        question9 = int(request.POST.get('question9'))
        question10 = int(request.POST.get('question10'))

        user_input = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10]  

        prediction = model.predict([user_input])[0]

        result = 'Extrovert' if prediction == 'Extrovert' else 'Introvert'

        is_vegetarian = request.POST.get('vegetarian', 'No')
        music = request.POST.get('music','No')
        smoke = request.POST.get('smoke','No')
        riser = request.POST.get('riser','No')
        tidy = request.POST.get('tidy','No')

        user_profile = UserProfile.objects.get_or_create(user=request.user)[0]
        user_profile.introvert_extrovert_result = result
        user_profile.user_name = request.user.username
        user_profile.email = request.user.email
        user_profile.save()

        other_users = UserProfile.objects.filter(introvert_extrovert_result=result).exclude(user=request.user)
        return render(request, 'test/result.html', {
            'result': result,
            'other_users': other_users,
            'is_vegetarian': 'Is a vegetarian' if is_vegetarian == 'Yes' else 'Is a Non-Vegetarian',
            'music':"Plays music instruments or doesn't mind if you play musical instruments" if music == 'Yes' else "Doesn't like musical instruments",
            'smoke' :'Smokes' if smoke == 'Yes' else "Doesn't smoke",
            'riser' :'Likes to wake up early' if riser == 'Yes' else "Doesn't wake up early",
            'tidy' :'Likes to organise' if tidy == 'Yes' else "Isn't organised"
            })

    
    if request.user.is_authenticated:
        show_card = False
    else:
        show_card = True

    return render(request, 'test/questions.html',{'show_card': show_card})

    
    