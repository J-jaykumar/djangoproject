from django.shortcuts import render , HttpResponse , redirect
from .models import Student
from django.contrib import messages
from .forms import studentform

# Create your views here.
def home(request):
    return render(request ,"home.html")
    # return HttpResponse("home page coming soon")

def about(request):
    return render (request , "about.html")

def contact(request):
    return render(request , "contact.html")

def add_student(request):
    if request.method =="POST":
        studentname = request.POST["stu_name"]
        collagename = request.POST["collage_name"]
        mobilenum = request.POST["mobile"]
        branch = request.POST["branch"]

        student_data = Student(studentname=studentname , collagename =collagename , mobilenum=mobilenum ,branch=branch)

        print(studentname , collagename , mobilenum , branch)
        student_data.save()
        messages.success(request , "student data added")
        return redirect("home")
    messages.error(request , "test message")
    return render(request , "add_student.html")

def view_studend(request):
    student_info = Student.objects.all()
    context = {
        "student_data" : student_info,
    }
    return render (request , "view_student.html" , context)

def edit_info(request , id):
    context = {
        "edit_info" : Student.objects.get(id=id)
    }
    return render( request , "edit_info.html" , context)

def update(request , id):
    studentinfo = Student.objects.get(id = id)
    form = studentform(request.POST ,instance = studentinfo)
    if form.is_valid():  
        form.save()
        messages.success(request ,"stutent information updated")
        return redirect ("/home")
    
    return render(request , "edit_info.html" , {"student":studentinfo})

def delete(request , id):
    deletestu = Student.objects.get(id= id)
    deletestu.delete()
    messages.error(request ,"student data deleted")

    return redirect("home")