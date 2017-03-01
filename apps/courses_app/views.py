from django.shortcuts import render, redirect, HttpResponse

from django.contrib import messages

from .models import Course, Description

def index(request):
    #initial route, should display the form, take input from that form, and display the existing courses in the table below.
    context = {
    'courses': Course.objects.all(),
    'descriptions': Description.objects.all(),
    # 'timestamps': Course.objects.all()
    }
    print "This is the index Route!"
    return render(request, "index.html", context)

# def process(request):
#     # if request.method == "POST":
#     print request.POST
#     print Course.objects.all()
#     print "This is the process route!"
#     print "and were FINISHED!"
#     return render(request, "index.html", context)


def create_course(request):
    #if the request is POST, create a course entry in the db
    context = {
    'courses': Course.objects.all(),
    'description': Description.objects.all(),
    # 'created': Course.objects.created_at(),
    }
    if request.method == "POST":
        print "were in the create_course method!"
        print("-"*20)
        Course.objects.create(course_name=request.POST['course_name'])
        Description.objects.create(description=request.POST['description'])
        print("-"*20, "^Heres the creation steps!")
        print request.POST
        print("-"*20)
        print context, "<<< CONTEXT"
        print("-"*20)
        print (Course.objects.all())
        print("-"*20)
        return render(request, "index.html", context)
    else:
        return redirect('/')


def destroy(request, id):
        #  contains Course with primary key = id
    context = {
        'course': Course.objects.get(pk=id)
    }
    return render(request, 'destroy.html', context)

#
# def confirm_delete(request):
#     print "NAME OF ENTRY WE WANT TO DELETE BASED ON NUMERIC ID TIED TO REMOVE BUTTON"
#     print "DESCRIPTION FORM SAME ITEM"
#     return render(request, "destroy.html")

def destroy_confirm(request, id):
    if request.method == 'POST':
        course = Course.objects.get(pk=id)
        # description = Description.objects.get(pk=id)
        course.delete()
        # description.delete()
        # pass
        messages.add_message(request, messages.SUCCESS, 'Course {} was removed'.format(course.course_name))
    else:
        messages.add_message(request, message.ERROR, 'There was an error, please try again.')
        # pass

    return redirect('/')
#
# def no_delete(request):
#     return redirect('/')
#
# def yes_delete(request):
#     return redirect('/')


    # request.session['course_name'] = request.POST['name']
