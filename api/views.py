from students.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET', 'POST'])
def studentView(request):
    if request.method == 'GET':
        #Get all the data from the Student model
        students = Student.objects.all()
        #Serialize the data
        serializer = StudentSerializer(students, many=True)
        #Return the serialized data as a Response
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        #Create a new student record 
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        #Return the errors if the data is not valid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)