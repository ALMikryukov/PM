from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import Profile, Account, Transaction
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from .forms import CastomUserCreationForm, ProfileForm, TransactionForm

from django.contrib.auth.decorators import user_passes_test


def home(request):
    return render(request, 'users/home.html')


def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('user-profile', request.user.profile.id )
        else:
            messages.error(request, 'Username or password is incorrect')
        
    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out')
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CastomUserCreationForm()
    
    if request.method == 'POST':
        form = CastomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')

            login(request, user)
            return redirect('user-profile', request.user.profile.id )
        
        else:
            messages.success(request, 'An Error has occurred during registration!')



    context = {'page':page, 'form':form}
    return render(request, 'users/login_register.html', context)






@login_required(login_url='login')
def profiles(request):
    qrs = Profile.objects.all()
    context = { }
    

    return render(request, 'users/profiles.html', context)

@login_required(login_url='login')
def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = { 'profile' : profile}
    return render(request, 'users/user-profile.html', context)

@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user-profile', request.user.profile.id )

    context = {'form': form}
    return render(request, 'users/profile-form.html', context)



def admin_only(view_func):
    # Функция-обертка, принимает view_func (функцию-обработчик запроса)
    decorated_view_func = user_passes_test(
        lambda user: user.is_authenticated and user.is_superuser,
        login_url='login' # URL для редиректа, если пользователь не прошел проверку
    )(view_func)
    # Функция-обертка возвращает декорированную view_func, которая будет проверять права доступа
    return decorated_view_func

@admin_only
def editProfileBalance(request, pk):
    profile = Profile.objects.get(id=pk)
    form = TransactionForm()
    transactions = profile.user.transaction_set.all()
    balance = 0
 

    # if request.method == 'POST':
    #     form = TransactionForm(request.POST)
    #     newTransaction = form.save(commit=False)
    #     newTransaction.owner = profile.user
    #     newTransaction.save()
    #     return redirect ('edit-balance', profile.id)
    if request.method == 'POST':
        Transaction.objects.create(owner= profile.user, amount=request.POST["input-numeric"] )

    for x in transactions:
        if x.is_deposit:
            balance += x.amount
        else:
            balance -= x.amount
    # input_ = request.POST["input-numeric"]
    print(request.POST)
 
    context = { 'profile' : profile,'form':form, 'transactions': transactions, 'balance':balance,  }
    return render(request, 'users/edit-balance.html', context, )

def balance(request):
    page = 'balance'
    profile = request.user.profile
    transactions = request.user.transaction_set.all()
    balance = 0
    for x in transactions:
        if x.is_deposit:
            balance += x.amount
        else:
            balance -= x.amount
    context = {'profile': profile, 'transactions':transactions, 'balance':balance, 'page':page}

    return render(request, 'users/balance.html',context )
