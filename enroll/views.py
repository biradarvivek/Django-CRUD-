from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
# Create your views here.


def dashboard(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
        stud = User.objects.all()

    return render(request, 'enroll/dashboard.html', {'form': fm, 'stu': stud})
