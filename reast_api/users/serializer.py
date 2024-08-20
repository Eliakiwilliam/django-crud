from rest_framework import serializers
from users.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


# class TeacherSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Teacher
#         fields = '__all__'
