from django.shortcuts import render, redirect
from web_app.forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


# -- Home page --
def home(request):
    return render(request, 'web_app/index.html')


# -- Login a user --
def user_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(f"Username: {username}, Password: {password}")  # Debugging statement
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print("User authenticated successfully")
                login(request, user)
                if username == 'user' and password == 'user_employee':
                    print("Redirecting to employee dashboard")
                    return redirect('employee_dashboard')
                elif username == 'coordinator' and password == 'test_app':
                    print("Redirecting to coordinator dashboard")
                    return redirect('coordinator_dashboard')
            else:
                form.add_error(None, "Invalid username or password")
                print("User authentication failed")
    else:
        form = LoginForm()

    return render(request, 'web_app/login.html', {'form':form})


@login_required(login_url="login")
def employee_dashboard(request):
    return render(request, "web_app/employee_dashboard.html")


@login_required(login_url="login")
def coordinator_dashboard(request):
    return render(request, "web_app/coordinator_dashboard.html")


def user_logout(request):
    auth.logout(request)
    return redirect("login")
