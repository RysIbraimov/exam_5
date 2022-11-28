from django.db import models
import datetime

class Language(models.Model):
    name = models.CharField(max_length=30)
    month_to_learn = models.IntegerField(default=6)

    def save(self,*args,**kwargs):
        super().save(*args, **kwargs)

        if self.name == self.name.lower():
            self.name = self.name.title()

        print(f'{self.name} saved')


class AbstractPerson (models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=14)

    class Meta:
        abstract = True

    def save(self,*args,**kwargs):
        super().save(*args, **kwargs)
        proper_number = ''
        if self.phone_number[0] == '0':
            proper_number = '+996' + self.phone_number[1:]
            self.phone_number = proper_number
        print(f'{self.phone_number} saved as {proper_number}')


class Student(AbstractPerson):
    os_choices = ((1,'linux'),(2,'windows'),(3,'mac'))
    work_study_place = models.CharField(max_length=40,null=True, blank=True)
    has_own_notebook = models.BooleanField()
    preferred_os = models.CharField(max_length=20,choices=os_choices)

class Mentor(AbstractPerson):
    main_work = models.CharField(max_length=40, null=True, blank=True)
    experience  = models.DateField()
    student = models.ManyToManyField(Student, through="Course")

    def __str__(self):
        return self.name

class Course(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    date_started = models.DateField()

    def __str__(self):
        return f'{self.student.name} - {self.mentor.name}'

    def get_end_date(self):
        end_date = self.date_started + datetime.timedelta(self.student.month_to_learn)
        return f'{end_date}'
