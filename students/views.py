from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def students(request):
    student_info = {'id': 1, 'name': 'Tabong', 'Age': 20}
    return JsonResponse(student_info)
