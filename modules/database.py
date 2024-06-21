import sqlite3

def initialize_database(path):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    cursor.execute('''
    create table if not exists Students(
        StudentId integer primary key,
        Name text,
        EnrollmentYear integer,
        Major text,
        Gender text,
        Age integer,
        Region text,
        test_score integer
    );''')

    cursor.execute('''
    create table if not exists Courses(
        CourseId text primary key,
        CourseTitle text,
        Credit real,
        StartDate text,
        EndDate text
    );''')

    cursor.execute('''
    create table if not exists CourseEnrollment(
        StudentId integer,
        CourseId text,
        primary key (StudentId, CourseId),
        foreign key (StudentId) references Students(StudentId),
        foreign key (CourseId) references Courses(CourseId)
    );''')

    cursor.execute('''
    create table if not exists AdvisorList(
        AdvisorId integer primary key,
        AdvisorName text,
        StudentId integer,
        foreign key (StudentId) references Students(StudentId)
    );''')

    cursor.execute('''
    create table if not exists accommodation(
        accommodationId integer primary key,
        StudentId integer,
        RoomNo integer,
        StartDate text,
        EndDate text,
        foreign key (StudentId) references Students(StudentId)
    );''')

    cursor.execute('''
    create table if not exists Books(
        BookId integer primary key,
        BookName text,
        Price text
    );''')

    cursor.execute('''
    create table if not exists BuyBooks(
        StudentId integer,
        BookId integer,
        primary key (StudentId, BookId),
        foreign key (StudentId) references Students(StudentId),
        foreign key (BookId) references Books(BookId)
    );''')

    conn.commit()
    conn.close()

class Database:
    def __init__(self, path):
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()

    def add_student(self, StudentId, Name, EnrollmentYear, Major, Gender, Age, Region, test_Score):
        self.cursor.execute('''
        insert into Students (StudentId, Name, EnrollmentYear, Major, Gender, Age, Region, test_score)
        values(?, ?, ?, ?, ?, ?, ?, ?)
        ''', (StudentId, Name, EnrollmentYear, Major, Gender, Age, Region, test_Score))
        self.conn.commit()

    def update_student(self,  StudentId, Name=None, EnrollmentYear=None, Major=None, Gender=None, Age=None, Region=None, test_Score=None):
        updates = []
        params = []
        if Name:
            updates.append('Name = ?')
            params.append(Name)
        if EnrollmentYear:
            updates.append('EnrollmentYear = ?')
            params.append(EnrollmentYear)
        if Major:
            updates.append('Major = ?')
            params.append(Major)
        if Gender:
            updates.append('Gender = ?')
            params.append(Gender)
        if Age:
            updates.append('Age = ?')
            params.append(Age)
        if Region:
            updates.append('Region = ?')
            params.append(Region)
        if test_Score:
            updates.append('test_score = ?')
            params.append(test_Score)
        params.append(StudentId)
        self.cursor.execute(f'''
            update Students set {', '.join(updates)} where StudentId = ?
        ''', params)
        self.conn.commit()

    def delete_student(self, StudentId):
        self.cursor.execute('''
        delete from Students where StudentID = ?
        ''', (StudentId,))
        self.conn.commit()

    def query_students(self):
        self.cursor.execute('''select * from Students''')
        return self.cursor.fetchall()

    def find_student(self, StudentId):
        self.cursor.execute(f'''select * from Students where StudentId = ?''', (StudentId,))
        return self.cursor.fetchone()

    def check_student(self, StudentId):
        if self.find_student(StudentId) is None:
            raise ValueError('''Student isn't registered''')

    def add_course(self, course_id, course_title, credit, start_date, end_date):
        self.cursor.execute('''
        insert into Courses (CourseId, CourseTitle, Credit, StartDate, EndDate)
        values (?, ?, ?, ?, ?)
        ''', (course_id, course_title, credit, start_date, end_date))
        self.conn.commit()

    def get_course(self, course_id):
        self.cursor.execute('select * from Courses where CourseId = ?', (course_id,))
        return self.cursor.fetchone()

    def query_course(self):
        self.cursor.execute('select * from Courses')
        return self.cursor.fetchall()

    def update_course(self, course_id, course_title=None, credit=None, start_date=None, end_date=None):
        fields = []
        values = []

        if course_title is not None:
            fields.append("CourseTitle = ?")
            values.append(course_title)
        if credit is not None:
            fields.append("Credit = ?")
            values.append(credit)
        if start_date is not None:
            fields.append("StartDate = ?")
            values.append(start_date)
        if end_date is not None:
            fields.append("EndDate = ?")
            values.append(end_date)

        values.append(course_id)
        sql = f'update Courses set {", ".join(fields)} where CourseId = ?'
        self.cursor.execute(sql, values)
        self.conn.commit()

    def delete_course(self, course_id):
        self.cursor.execute('delete from Courses where CourseId = ?', (course_id,))
        self.conn.commit()

    def add_course_enrollment(self, student_id, course_id):
        self.cursor.execute('''
        insert into CourseEnrollment (StudentId, CourseId)
        values (?, ?)
        ''', (student_id, course_id))
        self.conn.commit()

    def get_course_enrollment(self, student_id):
        self.cursor.execute('select * from CourseEnrollment where StudentId = ?',
                            (student_id,))
        return self.cursor.fetchall()

    def delete_course_enrollment(self, student_id, course_id):
        self.cursor.execute('delete from CourseEnrollment where StudentId = ? and CourseId = ?',
                            (student_id, course_id))
        self.conn.commit()

    def add_advisor(self, advisor_id, advisor_name, student_id):
        self.cursor.execute('''
        insert into AdvisorList (AdvisorId, AdvisorName, StudentId)
        values (?, ?, ?)
        ''', (advisor_id, advisor_name, student_id))
        self.conn.commit()

    def get_advisor(self, student_id):
        self.cursor.execute('select * from AdvisorList where StudentId = ?', (student_id,))
        return self.cursor.fetchone()

    def query_advisor(self):
        self.cursor.execute('select * from AdvisorList')
        return self.cursor.fetchall()

    def update_advisor(self, advisor_id, advisor_name=None, student_id=None):
        fields = []
        values = []

        if advisor_name is not None:
            fields.append("AdvisorName = ?")
            values.append(advisor_name)
        if student_id is not None:
            fields.append("StudentId = ?")
            values.append(student_id)

        values.append(advisor_id)
        sql = f'update AdvisorList set {", ".join(fields)} where AdvisorId = ?'
        self.cursor.execute(sql, values)
        self.conn.commit()

    def delete_advisor(self, advisor_id):
        self.cursor.execute('delete from AdvisorList where AdvisorId = ?', (advisor_id,))
        self.conn.commit()

    def add_accommodation(self, accommodation_id, student_id, room_no, start_date, end_date):
        self.cursor.execute('''
        insert into Accommodation (AccommodationId, StudentId, RoomNo, StartDate, EndDate)
        values (?, ?, ?, ?, ?)
        ''', (accommodation_id, student_id, room_no, start_date, end_date))
        self.conn.commit()

    def get_accommodation(self, student_id):
        self.cursor.execute('select * from Accommodation where StudentId = ?', (student_id,))
        return self.cursor.fetchall()

    def query_accommodation(self):
        self.cursor.execute('select * from Accommodation')
        return self.cursor.fetchall()

    def update_accommodation(self, accommodation_id, student_id=None, room_no=None, start_date=None, end_date=None):
        fields = []
        values = []

        if student_id is not None:
            fields.append("StudentId = ?")
            values.append(student_id)
        if room_no is not None:
            fields.append("RoomNo = ?")
            values.append(room_no)
        if start_date is not None:
            fields.append("StartDate = ?")
            values.append(start_date)
        if end_date is not None:
            fields.append("EndDate = ?")
            values.append(end_date)

        values.append(accommodation_id)
        sql = f'update Accommodation set {", ".join(fields)} where AccommodationId = ?'
        self.cursor.execute(sql, values)
        self.conn.commit()

    def delete_accommodation(self, accommodation_id):
        self.cursor.execute('delete from Accommodation where AccommodationId = ?', (accommodation_id,))
        self.conn.commit()

    def add_book(self, book_id, book_name, price):
        self.cursor.execute('''
        insert into Books (BookId, BookName, Price)
        values (?, ?, ?)
        ''', (book_id, book_name, price))
        self.conn.commit()

    def get_book(self, book_id):
        self.cursor.execute('select * from Books where BookId = ?', (book_id,))
        return self.cursor.fetchone()

    def check_book(self, book_id):
        if self.get_book(book_id) is None:
            raise ValueError('This book is unavailable')

    def query_book(self):
        self.cursor.execute('select * from Books')
        return self.cursor.fetchall()

    def update_book(self, book_id, book_name=None, price=None):
        fields = []
        values = []

        if book_name is not None:
            fields.append("BookName = ?")
            values.append(book_name)
        if price is not None:
            fields.append('price = ?')
            values.append(price)

        values.append(book_id)
        sql = f'update Books set {", ".join(fields)} where BookId = ?'
        self.cursor.execute(sql, values)
        self.conn.commit()

    def delete_book(self, book_id):
        self.cursor.execute('delete from Books where BookId = ?', (book_id,))
        self.conn.commit()

    def add_buy_book(self, student_id, book_id):
        self.cursor.execute('''
        insert into BuyBooks (StudentId, BookId)
        values (?, ?)
        ''', (student_id, book_id))
        self.conn.commit()

    def get_buy_book(self, student_id):
        self.cursor.execute('select * from BuyBooks where StudentId = ?', (student_id,))
        return self.cursor.fetchall()

    def delete_buy_book(self, student_id, book_id):
        self.cursor.execute('delete from BuyBooks where StudentId = ? and BookId = ?', (student_id, book_id))
        self.conn.commit()

    def get_min_excluded_id(self, table_name):
        self.cursor.execute(f'PRAGMA table_info({table_name})')
        columns = self.cursor.fetchall()

        if not columns:
            raise ValueError("Table does not exist or has no columns.")

        id_field = columns[0][1]

        self.cursor.execute(f'select {id_field} from {table_name}')
        ids = [row[0] for row in self.cursor.fetchall()]

        mex = 0
        ids_set = set(ids)
        while mex in ids_set:
            mex += 1

        return mex

    def close(self):
        self.conn.close()