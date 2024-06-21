from modules import database
from modules import analysis

db_path = r'C:\Users\Eleus Ahammad\PycharmProjects\student-info-system\db\student_info_system.db'
database.initialize_database(db_path)
db = database.Database(db_path)
analyzer = analysis.Analysis(db_path)

def Analysis_dashboard():
    students_per_major, gender_ratio_per_major = analyzer.analyze_students_per_major()
    analyzer.plot_students_per_major(students_per_major)
    analyzer.plot_gender_ratio_per_major(gender_ratio_per_major)

    results_comparison = analyzer.analyze_results_comparison()
    print("\nComparison of results in different majors:")
    print(results_comparison)

    age_test_score_corr = analyzer.analyze_age_vs_test_scores()
    print(f"\nCorrelation between student age and test scores: {age_test_score_corr:.2f}")

    region_test_scores = analyzer.analyze_regional_distribution_vs_test_scores()
    print("\nTest scores by region:")
    print(region_test_scores)

def student_register_dashboard():
    try:
        StudentId = int(input('StudentId:'))
        Name = input('Name:')
        EnrollmentYear = int(input('EnrollmentYear:'))
        Major = input('Major:')
        Gender = input('Gender:')
        Age = int(input('Age:'))
        Region = input('Region:')
        test_score = int(input('Test_score:'))

        db.add_student(StudentId, Name, EnrollmentYear, Major, Gender, Age, Region, test_score)
        print('Student registered successfully.')
    except Exception as e:
        print(f'Error occured while adding new student: {e}')

def student_update_dashboard():
    try:
        StudentId = int(input('StudentId:'))
        print('''
            Select option to update:
            1. Name
            2. EnrollmentYear
            3. Major
            4. Gender
            5. Age
            6. Region
            7. test_score
        ''')
        command = int(input('Enter an integer between 1 to 7:'))
        if command == 1:
            Name = input('Name:')
            db.update_student(StudentId, Name=Name)
        elif command == 2:
            EnrollmentYear = int(input('EnrollmentYear:'))
            db.update_student(StudentId, EnrollmentYear=EnrollmentYear)
        elif command == 3:
            Major = input('Major:')
            db.update_student(StudentId, Major=Major)
        elif command == 4:
            Gender = input('Gender:')
            db.update_student(StudentId, Gender=Gender)
        elif command == 5:
            Age = int(input('Age:'))
            db.update_student(StudentId, Age=Age)
        elif command == 6:
            Region = input('Region:')
            db.update_student(StudentId, Region=Region)
        elif command == 7:
            test_score = int(input('Test Score:'))
            db.update_student(StudentId, test_score=test_score)
        else:
            print('Invalid option selected.')
            return
        print('Information updated successfully.')
    except Exception as e:
        print(f'Error occurred while updating student info: {e}')

def student_delete_dashboard():
    try:
        StudentId = int(input('Enter StudentId to delete:'))
        confirm = input('Are you sure you want to delete this student? (yes/no): ')
        if confirm.lower() == 'yes':
            db.delete_student(StudentId)
            print('Student deleted successfully.')
        elif confirm.lower() == 'no':
            print('Deletion cancelled.')
        else:
            print('Invalid input. Deletion cancelled.')
    except Exception as e:
        print(f'Error occurred while deleting student: {e}')

def show_student_list():
    try:
        students = db.query_students()
        print("\nStudent List:\n")
        print("StudentId\tName\tEnrollmentYear\tMajor\tGender\tAge\tRegion\ttest_score")

        for student in students:
            print(f"{student[0]}\t\t{student[1]}\t{student[2]}\t\t{student[3]}\t{student[4]}\t{student[5]}\t{student[6]}\t{student[7]}")

    except Exception as e:
        print(f'Error occurred while fetching student list: {e}')


def student_main_dashboard():
    print(f'''
        Welcome to Student Dashboard!
        Type a number and hit enter to select an option:
        1. Register as student
        2. Update student information
        3. Delete student information
        4. Show student list
    ''')
    option = input('Enter your choice: ')

    if option == '1':
        student_register_dashboard()
    elif option == '2':
        student_update_dashboard()
    elif option == '3':
        student_delete_dashboard()
    elif option == '4':
        show_student_list()
    else:
        print('Invalid option selected. Please try again.')

def course_add_dashboard():
    try:
        CourseId = input('CourseId: ')
        CourseTitle = input('Course Title: ')
        Credit = float(input('Credit: '))
        StartDate = input('Start Date: ')
        EndDate = input('End Date: ')

        db.add_course(CourseId, CourseTitle, Credit, StartDate, EndDate)
        print('Course added successfully.')
    except Exception as e:
        print(f'Error occurred while adding a new course: {e}')

def course_update_dashboard():
    try:
        CourseId = input('Enter CourseId to update: ')
        print('''
            Select option to update:
            1. Course Title
            2. Credit
            3. Start Date
            4. End Date
        ''')
        command = int(input('Enter an integer between 1 to 4: '))
        if command == 1:
            CourseTitle = input('Course Title: ')
            db.update_course(CourseId, course_title=CourseTitle)
        elif command == 2:
            Credit = float(input('Credit: '))
            db.update_course(CourseId, credit=Credit)
        elif command == 3:
            StartDate = input('Start Date: ')
            db.update_course(CourseId, start_date=StartDate)
        elif command == 4:
            EndDate = input('End Date: ')
            db.update_course(CourseId, end_date=EndDate)
        else:
            print('Invalid option selected.')
            return
        print('Information Updated successfully')
    except Exception as e:
        print(f'Error occurred while updating course info: {e}')

def course_delete_dashboard():
    try:
        CourseId = input('Enter CourseId to delete: ')
        confirm = input('Are you sure you want to delete this course? (yes/no): ')
        if confirm.lower() == 'yes':
            db.delete_course(CourseId)
            print('Course deleted successfully.')
        elif confirm.lower() == 'no':
            print('Deletion cancelled.')
        else:
            print('Invalid input. Deletion cancelled.')
    except Exception as e:
        print(f'Error occurred while deleting course: {e}')

def show_course_list():
    try:
        courses = db.query_course()
        if courses:
            print("\nCourse List:\n")
            print("CourseId\tCourse Title\tCredit\tStart Date\tEnd Date")
            for course in courses:
                print(f"{course[0]}\t\t{course[1]}\t\t{course[2]}\t{course[3]}\t{course[4]}")
        else:
            print("No courses found.")
    except Exception as e:
        print(f'Error occurred while fetching course list: {e}')

def course_main_dashboard():
    print('''
        Course Dashboard
        Type a number and hit enter to select an option:
        1. Add Course
        2. Update Course
        3. Delete Course
        4. Show Course List
    ''')
    option = input('Enter your choice: ')

    if option == '1':
        course_add_dashboard()
    elif option == '2':
        course_update_dashboard()
    elif option == '3':
        course_delete_dashboard()
    elif option == '4':
        show_course_list()
    else:
        print('Invalid option selected. Please try again.')

def course_enrollment_add_dashboard():
    try:
        student_id = int(input('StudentId: '))
        db.check_student(student_id)
        course_id = input('CourseId: ')
        db.add_course_enrollment(student_id, course_id)
        print('Course enrollment added successfully.')
    except Exception as e:
        print(f'Error occurred while adding course enrollment: {e}')

def course_enrollment_delete_dashboard():
    try:
        student_id = int(input('Enter StudentId: '))
        course_id = input('Enter CourseId to delete enrollment: ')
        confirm = input('Are you sure you want to delete this enrollment? (yes/no): ')
        if confirm.lower() == 'yes':
            db.delete_course_enrollment(student_id, course_id)
            print('Course enrollment deleted successfully.')
        elif confirm.lower() == 'no':
            print('Deletion cancelled.')
        else:
            print('Invalid input. Deletion cancelled.')
    except Exception as e:
        print(f'Error occurred while deleting course enrollment: {e}')

def show_enrolled_courses_dashboard():
    try:
        student_id = int(input('Enter StudentId to view enrolled courses: '))
        courses = db.get_course_enrollment(student_id)
        if courses:
            print("\nEnrolled Courses:\n")
            print("CourseId")
            for course in courses:
                print(f"{course[1]}")
        else:
            print("No courses found for this student.")
    except Exception as e:
        print(f'Error occurred while fetching enrolled courses: {e}')

def course_enrollment_main_dashboard():
    print('''
        Course Enrollment Dashboard
        Type a number and hit enter to select an option:
        1. Add Course Enrollment
        2. Delete Course Enrollment
        3. Show Enrolled Courses
    ''')
    option = input('Enter your choice: ')

    if option == '1':
        course_enrollment_add_dashboard()
    elif option == '2':
        course_enrollment_delete_dashboard()
    elif option == '3':
        show_enrolled_courses_dashboard()
    else:
        print('Invalid option selected. Please try again.')

def add_accommodation_dashboard():
    try:
        accommodation_id = db.get_min_excluded_id('accommodation')
        student_id = int(input('StudentId: '))
        db.check_student(student_id)
        room_no = int(input('RoomNo: '))
        start_date = input('StartDate (YYYY-MM-DD): ')
        end_date = input('EndDate (YYYY-MM-DD): ')
        db.add_accommodation(accommodation_id, student_id, room_no, start_date, end_date)
        print('accommodation added successfully.')
    except Exception as e:
        print(f'Error occurred while adding accommodation: {e}')

def update_accommodation_dashboard():
    try:
        accommodation_id = int(input('Enter accommodationId to update: '))
        print('''
            Select option to update:
            1. StudentId
            2. RoomNo
            3. StartDate
            4. EndDate
        ''')
        command = int(input('Enter an integer between 1 to 4: '))
        if command == 1:
            student_id = int(input('New StudentId: '))
            db.update_accommodation(accommodation_id, student_id=student_id)
        elif command == 2:
            room_no = int(input('New RoomNo: '))
            db.update_accommodation(accommodation_id, room_no=room_no)
        elif command == 3:
            start_date = input('New StartDate (YYYY-MM-DD): ')
            db.update_accommodation(accommodation_id, start_date=start_date)
        elif command == 4:
            end_date = input('New EndDate (YYYY-MM-DD): ')
            db.update_accommodation(accommodation_id, end_date=end_date)
        else:
            print('Invalid option selected.')
            return
        print('Information Updated successfully.')
    except Exception as e:
        print(f'Error occurred while updating accommodation: {e}')

def delete_accommodation_dashboard():
    try:
        accommodation_id = int(input('Enter accommodationId to delete: '))
        confirm = input('Are you sure you want to delete this accommodation? (yes/no): ')
        if confirm.lower() == 'yes':
            db.delete_accommodation(accommodation_id)
            print('accommodation deleted successfully.')
        elif confirm.lower() == 'no':
            print('Deletion cancelled.')
        else:
            print('Invalid input. Deletion cancelled.')
    except Exception as e:
        print(f'Error occurred while deleting accommodation: {e}')

def show_accommodation_list():
    try:
        student_id = int(input('StudentId:'))
        accommodations = db.get_accommodation(student_id)
        print("\naccommodation List:\n")
        print("accommodationId\tStudentId\tRoomNo\tStartDate\tEndDate")

        for accommodation in accommodations:
            print(f"{accommodation[0]}\t\t{accommodation[1]}\t\t{accommodation[2]}\t{accommodation[3]}\t{accommodation[4]}")
    except Exception as e:
        print(f'Error occurred while fetching accommodation list: {e}')

def accommodation_main_dashboard():
    print('''
        accommodation Dashboard
        Type a number and hit enter to select an option:
        1. Add accommodation
        2. Update accommodation
        3. Delete accommodation
        4. Show accommodation List
    ''')
    option = input('Enter your choice: ')

    if option == '1':
        add_accommodation_dashboard()
    elif option == '2':
        update_accommodation_dashboard()
    elif option == '3':
        delete_accommodation_dashboard()
    elif option == '4':
        show_accommodation_list()
    else:
        print('Invalid option selected. Please try again.')

def add_advisor_dashboard():
    try:
        advisor_id = db.get_min_excluded_id('AdvisorList')
        advisor_name = input('AdvisorName: ')
        student_id = int(input('StudentId: '))
        db.check_student(student_id)
        db.add_advisor(advisor_id, advisor_name, student_id)
        print('Advisor added successfully.')
    except Exception as e:
        print(f'Error occurred while adding advisor: {e}')

def find_advisor_dashboard():
    try:
        student_id = int(input('Enter StudentId to find advisor: '))
        advisor = db.get_advisor(student_id)
        if advisor:
            print(f'AdvisorId: {advisor[0]}, AdvisorName: {advisor[1]}, StudentId: {advisor[2]}')
        else:
            print('Advisor not found for the given StudentId.')
    except Exception as e:
        print(f'Error occurred while finding advisor: {e}')

def update_advisor_dashboard():
    try:
        advisor_id = int(input('Enter AdvisorId to update: '))
        advisor_name = input('New AdvisorName: ')
        db.update_advisor(advisor_id, advisor_name=advisor_name)
        print('Advisor updated successfully.')
    except Exception as e:
        print(f'Error occurred while updating advisor: {e}')

def show_advisor_list():
    try:
        advisors = db.query_advisor()
        print("\nAdvisor List:\n")
        print("AdvisorId\tAdvisorName\tStudentId")

        for advisor in advisors:
            print(f"{advisor[0]}\t\t{advisor[1]}\t\t{advisor[2]}")
    except Exception as e:
        print(f'Error occurred while fetching advisor list: {e}')

def delete_advisor_dashboard():
    try:
        advisor_id = int(input('Enter AdvisorId to delete: '))
        confirm = input('Are you sure you want to delete this advisor? (yes/no): ')
        if confirm.lower() == 'yes':
            db.delete_advisor(advisor_id)
            print('Advisor deleted successfully.')
        elif confirm.lower() == 'no':
            print('Deletion cancelled.')
        else:
            print('Invalid input. Deletion cancelled.')
    except Exception as e:
        print(f'Error occurred while deleting advisor: {e}')


def advisor_dashboard():
    print('''
        Advisor Dashboard
        Type a number and hit enter to select an option:
        1. Add your advisor
        2. Find your advisor
        3. Update your advisor name
        4. Delete your advisor
        5. Show advisor list
    ''')
    option = input('Enter your choice: ')

    if option == '1':
        add_advisor_dashboard()
    elif option == '2':
        find_advisor_dashboard()
    elif option == '3':
        update_advisor_dashboard()
    elif option == '4':
        delete_advisor_dashboard()
    elif option == '5':
        show_advisor_list()
    else:
        print('Invalid option selected. Please try again.')

def add_book_dashboard():
    try:
        book_id = db.get_min_excluded_id('Books')
        book_name = input('BookName: ')
        price = input('Price:')
        db.add_book(book_id, book_name, price)
        print('Book added successfully.')
    except Exception as e:
        print(f'Error occurred while adding book: {e}')

def delete_book_dashboard():
    try:
        book_id = int(input('Enter BookId to delete: '))
        confirm = input('Are you sure you want to delete this book? (yes/no): ')
        if confirm.lower() == 'yes':
            db.delete_book(book_id)
            print('Book deleted successfully.')
        elif confirm.lower() == 'no':
            print('Deletion cancelled.')
        else:
            print('Invalid input. Deletion cancelled.')
    except Exception as e:
        print(f'Error occurred while deleting book: {e}')

def update_book_dashboard():
    try:
        book_id = int(input('Enter BookId to update: '))
        book_name = input('New BookName: ')
        db.update_book(book_id, book_name=book_name)
        print('Book updated successfully.')
    except Exception as e:
        print(f'Error occurred while updating book: {e}')

def update_price_dashboard():
    try:
        book_id = int(input('Enter BookId to update: '))
        price = input('New price: ')
        db.update_book(book_id, price=price)
        print('Book updated successfully.')
    except Exception as e:
        print(f'Error occurred while updating book: {e}')

def show_book_list_dashboard():
    try:
        books = db.query_book()
        print("\nBook List:\n")
        print("BookId\tBookName\tPrice")

        for book in books:
            print(f"{book[0]}\t{book[1]}\t{book[2]}")
    except Exception as e:
        print(f'Error occurred while fetching book list: {e}')


def books_dashboard():
    print('''
        Books Dashboard
        Type a number and hit enter to select an option:
        1. Add a book
        2. Delete a book
        3. Update a book title
        4. Update a book price
        5. Show book list
    ''')
    option = input('Enter your choice: ')

    if option == '1':
        add_book_dashboard()
    elif option == '2':
        delete_book_dashboard()
    elif option == '3':
        update_book_dashboard()
    elif option == '4':
        update_price_dashboard()
    elif option == '5':
        show_book_list_dashboard()
    else:
        print('Invalid option selected. Please try again.')

def buy_a_book_dashboard():
    try:
        student_id = int(input('StudentId: '))
        db.check_student(student_id)
        book_id = int(input('BookId: '))
        db.check_book(book_id)
        db.add_buy_book(student_id, book_id)
        print('Book purchased successfully.')
    except Exception as e:
        print(f'Error occurred while buying book: {e}')

def show_bought_books_dashboard():
    try:
        student_id = int(input('Enter StudentId to show bought books: '))
        books = db.get_buy_book(student_id)
        print("\nBought Books List:\n")
        print("StudentId\tBookId")

        for book in books:
            print(f"{book[0]}\t\t{book[1]}")
    except Exception as e:
        print(f'Error occurred while fetching bought books: {e}')

def undo_buying_dashboard():
    try:
        student_id = int(input('Enter StudentId to undo book purchase: '))
        db.check_student(student_id)
        book_id = int(input('Enter BookId to undo book purchase: '))
        db.check_book(book_id)
        confirm = input('Are you sure you want to undo this book purchase? (yes/no): ')
        if confirm.lower() == 'yes':
            db.delete_buy_book(student_id, book_id)
            print('Book purchase undone successfully.')
        elif confirm.lower() == 'no':
            print('Undo cancelled.')
        else:
            print('Invalid input. Undo cancelled.')
    except Exception as e:
        print(f'Error occurred while undoing book purchase: {e}')

def buybooks_dashboard():
    print('''
        Buy Books Dashboard
        Type a number and hit enter to select an option:
        1. Buy a book
        2. Show bought books for a student
        3. Undo a book purchase
    ''')
    option = input('Enter your choice: ')

    if option == '1':
        buy_a_book_dashboard()
    elif option == '2':
        show_bought_books_dashboard()
    elif option == '3':
        undo_buying_dashboard()
    else:
        print('Invalid option selected. Please try again.')

def main_dashboard():
    while True:
        print('''
        Welcome to Student Information Management System
            Main Dashboard
            Type a number and hit enter to select an option:
            1. Student Dashboard
            2. Courses Dashboard
            3. Course Enrollment Dashboard
            4. Advisor Dashboard
            5. Accommodations Dashboard
            6. Books Dashboard
            7. Buy Books Dashboard
            8. Generate Analysis report
            9. Exit
        ''')
        option = input('Enter your choice: ')

        if option == '1':
            student_main_dashboard()
        elif option == '2':
            course_main_dashboard()
        elif option == '3':
            print('\nAvailable', end=' ')
            show_course_list()
            course_enrollment_main_dashboard()
        elif option == '4':
            advisor_dashboard()
        elif option == '5':
            accommodation_main_dashboard()
        elif option == '6':
            books_dashboard()
        elif option == '7':
            print('\nAvailable', end=' ')
            show_book_list_dashboard()
            buybooks_dashboard()
        elif option == '8':
            Analysis_dashboard()
        elif option == '9':
            print("Exiting the program. Goodbye!")
            break
        else:
            print('Invalid option selected. Please try again.')

if __name__ == '__main__':
    main_dashboard()