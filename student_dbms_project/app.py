
from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
host="localhost",
user="root",
password="Root@123",
database="student_dbms"
)

cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/students')
def students():
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    return render_template('students.html', students=data)


@app.route('/add_student', methods=['GET','POST'])
def add_student():
    if request.method == 'POST':
        name=request.form['name']
        email=request.form['email']
        phone=request.form['phone']
        address=request.form['address']
        course=request.form['course']
        year=request.form['year']

        sql="INSERT INTO students(name,email,phone,address,course,admission_year) VALUES(%s,%s,%s,%s,%s,%s)"
        val=(name,email,phone,address,course,year)

        cursor.execute(sql,val)
        db.commit()
        return redirect('/students')

    return render_template('add_student.html')

@app.route('/edit_student/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        course = request.form['course']
        year = request.form['year']

        cursor.execute("""
            UPDATE students 
            SET name=%s, email=%s, phone=%s, address=%s, course=%s, admission_year=%s
            WHERE student_id=%s
        """, (name, email, phone, address, course, year, id))

        db.commit()
        return redirect('/students')

    
    cursor.execute("SELECT * FROM students WHERE student_id=%s", (id,))
    student = cursor.fetchone()

    return render_template('edit_student.html', student=student)

@app.route('/delete_student/<int:id>')
def delete_student(id):

    cursor.execute("DELETE FROM attendance WHERE student_id=%s",(id,))
    cursor.execute("DELETE FROM results WHERE student_id=%s",(id,))
    cursor.execute("DELETE FROM fees WHERE student_id=%s",(id,))

    cursor.execute("DELETE FROM students WHERE student_id=%s",(id,))

    db.commit()
    return redirect('/students')

@app.route('/search', methods=['POST'])
def search():
    keyword=request.form['keyword']
    cursor.execute("SELECT * FROM students WHERE name LIKE %s",('%'+keyword+'%',))
    result=cursor.fetchall()
    return render_template('students.html', students=result)


@app.route('/attendance')
def attendance():
    cursor.execute("""
    SELECT students.name, attendance.percentage
    FROM attendance
    JOIN students ON students.student_id=attendance.student_id
    """)
    data=cursor.fetchall()
    return render_template('attendance.html', records=data)


@app.route('/add_attendance', methods=['POST'])
def add_attendance():
    student_id=request.form['student_id']
    percentage=request.form['percentage']
    sql="INSERT INTO attendance(student_id,percentage) VALUES(%s,%s)"
    cursor.execute(sql,(student_id,percentage))
    db.commit()
    return redirect('/attendance')


@app.route('/results')
def results():
    cursor.execute("""
    SELECT students.name, results.subject, results.marks, results.grade
    FROM results
    JOIN students ON students.student_id=results.student_id
    """)
    data=cursor.fetchall()
    return render_template('results.html', records=data)


@app.route('/add_result', methods=['POST'])
def add_result():
    student_id=request.form['student_id']
    subject=request.form['subject']
    marks=request.form['marks']
    grade=request.form['grade']
    sql="INSERT INTO results(student_id,subject,marks,grade) VALUES(%s,%s,%s,%s)"
    cursor.execute(sql,(student_id,subject,marks,grade))
    db.commit()
    return redirect('/results')


@app.route('/fees')
def fees():
    cursor.execute("""
    SELECT students.name, fees.amount, fees.status, fees.payment_date
    FROM fees
    JOIN students ON students.student_id=fees.student_id
    """)
    data=cursor.fetchall()
    return render_template('fees.html', records=data)


@app.route('/add_fee', methods=['POST'])
def add_fee():
    student_id=request.form['student_id']
    amount=request.form['amount']
    status=request.form['status']
    date=request.form['date']
    sql="INSERT INTO fees(student_id,amount,status,payment_date) VALUES(%s,%s,%s,%s)"
    cursor.execute(sql,(student_id,amount,status,date))
    db.commit()
    return redirect('/fees')


if __name__ == '__main__':
    app.run(debug=True)
