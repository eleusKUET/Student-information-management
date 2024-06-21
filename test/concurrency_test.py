import sqlite3
import concurrent.futures
import random
import time
from modules.database import initialize_database
import os

database_file_path = r'C:\Users\Eleus Ahammad\PycharmProjects\student-info-system\db\student_info_system_test.db'
if os.path.exists(database_file_path):
    os.remove(database_file_path)

initialize_database(database_file_path)

def add_student(student_id, name, year, major, gender, age, region, test_score):
    conn = sqlite3.connect(database_file_path)
    cursor = conn.cursor()
    cursor.execute('''
    insert into Students (StudentId, Name, EnrollmentYear, Major, Gender, Age, Region, test_score)
    values (?, ?, ?, ?, ?, ?, ?, ?)''', (student_id, name, year, major, gender, age, region, test_score))
    conn.commit()
    conn.close()

def query_students():
    conn = sqlite3.connect(database_file_path)
    cursor = conn.cursor()
    cursor.execute('select * from Students')
    students = cursor.fetchall()
    conn.close()
    return students

def concurrent_write(student_id):
    add_student(student_id, f"Student {student_id}", 2024, "CS", "M", random.randint(18, 25), "Region X",
                random.randint(0, 100))
    print(f"Added student {student_id}")

def concurrent_read():
    students = query_students()
    print(f"Queried {len(students)} students")
    return len(students)

def concurrency_test():
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for i in range(10):
            futures.append(executor.submit(concurrent_write, i + 1))
        for _ in range(5):
            futures.append(executor.submit(concurrent_read))
        concurrent.futures.wait(futures)
        for future in futures:
            try:
                future.result()
            except Exception as e:
                print(f"Exception occurred: {e}")

if __name__ == "__main__":
    concurrency_test()
