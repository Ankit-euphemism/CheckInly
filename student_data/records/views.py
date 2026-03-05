from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student, Attendance
from django.utils import timezone


def mark_attendance(request):
    if request.method == "POST":
        try:
            students = Student.objects.all()
            if not students.exists():
                messages.warning(request, "No students found. Please add students first.")
                return redirect('mark_attendance')

            today = timezone.now().date()
            for student in students:
                status = request.POST.get(f'student_{student.id}') == 'on'
                Attendance.objects.update_or_create(
                    student=student,
                    date=today,
                    defaults={'status': status}
                )

            messages.success(request, "Attendance submitted successfully.")
        except Exception:
            messages.error(request, "Unable to save attendance right now. Please try again.")

        return redirect('mark_attendance')

    try:
        students = Student.objects.all()
    except Exception:
        students = []
        messages.error(request, "Unable to load students at the moment.")

    return render(request, 'mark_attendance.html', {'students': students})


def view_attendance(request):
    context = {'students': []}

    try:
        context['students'] = Student.objects.all()
    except Exception:
        messages.error(request, "Unable to load students at the moment.")

    if request.method == "POST":
        student_id = request.POST.get('student_id')
        if not student_id:
            messages.warning(request, "Please select a student first.")
            return render(request, 'view_attendance.html', context)

        try:
            student = Student.objects.filter(id=student_id).first()
            if not student:
                messages.error(request, "Selected student does not exist.")
                return render(request, 'view_attendance.html', context)

            records = Attendance.objects.filter(student_id=student_id).order_by('date')
            context['records'] = records
            context['student_name'] = student.name

            if not records.exists():
                messages.info(request, f"No attendance records found for {student.name}.")
        except Exception:
            messages.error(request, "Unable to fetch attendance records right now.")

        return render(request, 'view_attendance.html', context)

    return render(request, 'view_attendance.html', context)