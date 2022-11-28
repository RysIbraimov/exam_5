from user.models import  *
import datetime


python = Language.objects.create(name='Python',month_to_learn=6)
js = Language.objects.create(name='Java Script',month_to_learn=6)
ux_ui = Language.objects.create(name='Ux-Ui', month_to_learn=2)

student_1 = Student.objects.create(name='Amanov Aman',email='aman@mail.ru',
     phone_number='+996700989898',work_study_place='School №13', has_own_notebook=True,preferred_os='windows')
student_2 = Student.objects.create(name='Apina Alena',email='aapina@bk.ru',
     phone_number='0550888888',work_study_place='TV', has_own_notebook=True,preferred_os='mac')
student_3 = Student.objects.create(name='Phil Spencer',email='spencer@microsoft.com',
     phone_number='0508312312',work_study_place='Microsoft Gaming', has_own_notebook=False,preferred_os='linux')

mentor_1 = Mentor.objects.create(name='Ilona Maskova',email='imask@gmail.com',phone_number='0500545454',
                                 main_work=None,experience=datetime.date(year=2021, month=10, day=23))
mentor_2 = Mentor.objects.create(name='Halil Nurmuhametov',email='halil@gmail.com',phone_number='0709989876',
                                 main_work='University of Fort Collins',experience=datetime.date(year=2010, month=9, day=18))

course_1 = Course.objects.create(name='Python-21',mentor=mentor_2,student=student_1,date_started='2022-08-01',language=python)
course_2 = Course.objects.create(name='Python-21',mentor=mentor_2,student=student_2,date_started='2022-08-01',language=python)
course_3 = Course.objects.create(name='UX-UI',mentor=mentor_1,student=student_3,date_started='2022-08-22',language=ux_ui)


