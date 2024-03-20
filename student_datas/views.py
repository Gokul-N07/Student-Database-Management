from django.shortcuts import render,redirect
from student_datas.models import Student
from student_datas.forms import StudentForm

# Create your views here.

#Retrieve Student records from Database
def retrieve_data(request):
    student = Student.objects.all()
    return render(request,'student_datas/index.html',{'student':student})

#Add New Student Records
def create_data(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/data')
    return render(request,'student_datas/create.html',{'form':form})


#Update Student Records
def update_data(request,id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance = student)
        if form.is_valid():
            form.save()
            return redirect('/data')
    return render(request,'student_datas/update.html',{'student':student})

#Delete Student Records
def delete_data(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/data') 
    

