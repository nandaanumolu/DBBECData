from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/students/reg/<reg_id>', methods=['GET'])
def get_electives_by_registration_number(reg_id):
    try:
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Gmk@2324",
        database="student"
    )
        cursor = connection.cursor()
        query = f"SELECT SUB_CODE, SUB_NAME, Sem FROM student_details2 WHERE Reg_Id = '{reg_id}'"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        electives = []
        for row in results:
            elective = {
                'SUB_CODE': row[0],
                'SUB_NAME': row[1],
                'Sem': row[2]
            }
            electives.append(elective)

        return jsonify({'electives': electives}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/students/branch/<branch>', methods=['GET'])
def get_students_by_branch(branch):
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Gmk@2324",
        database="student"
    )
        cursor = connection.cursor()
        query = f"SELECT Name, Reg_Id, SUB_NAME FROM student_details2 WHERE Dept = '{branch}'"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        students = []
        for row in results:
            student = {
                'Name': row[0],
                'Reg_Id': row[1],
                'Elective': row[2]
            }
            students.append(student)

        return jsonify({'students': students}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/students/elective/<elective>', methods=['GET'])
def get_students_by_elective(elective):
    try:
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Gmk@2324",
        database="student"
    )
        cursor = connection.cursor()
        query = f"SELECT Name, Reg_Id FROM student_details2 WHERE SUB_NAME = '{elective}'"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        students = []
        for row in results:
            student = {
                'Name': row[0],
                'Reg_Id': row[1]
            }
            students.append(student)

        return jsonify({'students': students}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/students/add_record', methods=['POST'])
def add_elective():
    try:
        data = request.json
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Gmk@2324",
        database="student"
    )
        cursor = connection.cursor()
        insert_query = f"""
            INSERT INTO student_details2 (Reg_Id, Name, SUB_CODE, SUB_NAME, Dept, Sem, Year)
            VALUES ('{data['Reg_Id']}', '{data['Name']}', '{data['SUB_CODE']}', '{data['SUB_NAME']}',
                    '{data['Dept']}', '{data['Sem']}', '{data['Year']}')
        """
        cursor.execute(insert_query)
        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({'message': 'Elective added successfully.'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True)
