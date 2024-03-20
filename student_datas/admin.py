from django.contrib import admin
from student_datas.models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    Student_list = ['Student_No','Student_Name','Student_Year',"Student_Dept"]
    
admin.site.register(Student,StudentAdmin)
