from .models import Course
from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Course
    # fields = ['id','name','category_name','subcategory_name','level','username','real_price','price','discount','course_score','users']
    fields = '__all__'