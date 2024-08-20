from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Student
from .serializer import StudentSerializer


@csrf_exempt
def StudentApi(request, id=0):
    if request.method == 'GET':
        student = Student.objects.all()
        student_serializer = StudentSerializer(student, many=True)
        return JsonResponse(student_serializer.data, safe=False)

    elif request.method == 'POST':
        student_data = JSONParser().parse(request)
        student_serializer = StudentSerializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse('Added successfully', safe=False)
        return JsonResponse('Failed to add', safe=False)

    elif request.method == 'PUT':
        student_data = JSONParser().parse()
        student = Student.objects.get(studentId=student_data['studentId'])
        student_serializer = StudentSerializer(student, data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse('updated succefully', safe=False)
        return ('Failed to update')

    elif request.method == 'DELETE':
        student = Student.objects.get(studentId=id)
        student.delete()
        return JsonResponse('Deleted successfully', safe=False)


