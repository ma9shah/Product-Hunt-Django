from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

# def loginpage(req):
#     return render(req, 'login.html')


def login_or_signup(req):

    if req.method == "POST":
        # ? LOG IN
        if(req.POST['submit'] == 'submit'):
            user = auth.authenticate(
                req, password=req.POST['InputPassword3'], username=req.POST['username2'])
            if user is not None:
                auth.login(req, user)
                return redirect('home')
            else:
                try:
                    user = User.objects.get(username=req.POST['username2'])
                    return render(req, 'login.html', {'Error': "Wrong password!"})

                except User.DoesNotExist:
                    return render(req, 'login.html', {'Error': "User does not exist"})
                    # try:
                    #     ? I tried getting the user's password and validating the entered password myself,
                    #     ? django doesn't allow that apparently...have to use auth.authenticate to validate
                    #     user = User.objects.get(username=req.POST['username2'])
                    #     if(user.password == req.POST['InputPassword3']):
                    #         auth.login(req, user)
                    #         redirect('home')
                    #     else:
                    #         return render(req, 'login.html', {'Error': "Wrong password!"})

                    # except User.DoesNotExist:
                    #     return render(req, 'login.html', {'Error': "Username not registered!"})

                    # ? SIGN UP
        elif((req.POST['submit'] == 'Create an account')):
            if (req.POST.get('InputPassword2', '') != req.POST.get('InputPassword1', '')):
                Error = 'Passwords do not match'
                return render(req, 'login.html', {'Error': Error})
            else:
                try:
                    user = User.objects.get(username=req.POST['username1'])
                    return render(req, 'login.html', {'Error': "Username has been taken"})
                except User.DoesNotExist:
                    user = User.objects.create_user(
                        username=req.POST['username1'],  password=req.POST['InputPassword1'])  # Name=req.POST['name'],
                    auth.login(req, user)
                    return redirect('home')

                # Error = 'Account Created!'
                # return render(req, 'login.html', {'Error': Error})
    else:
        return render(req, 'login.html')
def logout(req):
    if req.method == "POST":
        auth.logout(req)
        return redirect('home')