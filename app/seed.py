from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import Student, Group, Teacher, Subject, Grade
from sqlalchemy.orm import configure_mappers

fake = Faker()

engine = create_engine('postgresql://postgres:mysecretpassword@localhost:5432/postgres')
Session = sessionmaker(bind=engine)
session = Session()
configure_mappers()
# Генерація студентів
students = [Student(fullname=fake.name()) for _ in range(50)]
session.add_all(students)
session.commit()
# Генерація груп
groups = [Group(name=fake.word()) for _ in range(3)]
session.add_all(groups)
session.commit()
# Генерація викладачів
teachers = [Teacher(name=fake.name()) for _ in range(5)]
session.add_all(teachers)
session.commit()
# Генерація предметів
subjects = [Subject(name=fake.word(), teacher_id=fake.random_element(teachers).id) for _ in range(8)]
session.add_all(subjects)
session.commit()
# Генерація оцінок для студентів
for student in students:
    for _ in range(fake.random_int(min=1, max=20)):
        grade = Grade(student_id=student.id, subject_id=fake.random_element(subjects).id, grade=fake.random_int(min=1, max=100))
        session.add(grade)
session.commit()
session.close()