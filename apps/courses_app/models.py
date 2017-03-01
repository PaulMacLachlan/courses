from __future__ import unicode_literals

from django.db import models


class CourseManager(models.Manager):
    def create_course(self, name):
        course = Course(course_name=name)
        course.save()
        return course

    def add_description(self, description):
        print description, "<<<-Description"
        description = Description.objects.create(description=description)
        return description

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

    def __str__(self):
        return self.course_name

class Description(models.Model):
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

    def __str__(self):
        return self.description





















# PW_REGEX = re.compile(r'[A-Z]+[a-z]+[A-Z]+')
# class UserManager(models.Model):
#     if len(data['password']) < 8:
#         errors.append("Password is too short, must be at least 8 characters")
#
#     elif not re.match(data['password'], PW,REGEX):
#         errors.append("Password must contain lower and upper case letters")
#
#         if errors:
#             return (False, errors)
#
#
#
#         else:
#             house_obj = House.objects.get(name=data['house'])
#             pw = data['password'].encode()
#             pw_hash = bcrypt.hashpw(pw, bcrypt.gensalt())
#             #Needs `errors`
