from django.db import models
class Student(models.Model):
    """Model representing a student."""
    name = models.CharField(max_length=100, verbose_name="Student Name")
    roll_number = models.CharField(max_length=20, unique=True, verbose_name="Roll Number")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ['roll_number']  # Order students by name


class Attendance(models.Model):
    """Model representing attendance record for a student."""
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField(verbose_name="Attendance Date")
    status = models.BooleanField(default=False, verbose_name="Attendance Status")  # True for present, False for absent

    class Meta:
        unique_together = ('student', 'date')
        verbose_name = "Attendance Record"
        verbose_name_plural = "Attendance Records"
        ordering = ['date']  # Order attendance by date

    def __str__(self):
        return f"{self.student.name} - {self.date} - {'Present' if self.status else 'Absent'}"
