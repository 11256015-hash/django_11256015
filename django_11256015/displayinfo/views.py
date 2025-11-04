from django.shortcuts import render


def display_info(request):
    student_id = "11256015" 
    student_name = "吳采欣"  

    context = {
        'student_id': student_id,
        'student_name': student_name,
    }

    return render(request, 'displayinfo/info.html', context)


def whoami(request):
    student_id = "11256015"
    student_name = "吳采欣"
    
    context = {
        'student_id': student_id,
        'student_name': student_name,
    }
    
    return render(request, 'displayinfo/info.html', context)
