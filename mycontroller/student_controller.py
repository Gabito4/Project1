from flask import jsonify
from flask import request, jsonify
from werkzeug.exceptions import abort

from exceptions.resource_not_found import ResourceNotFound
from exceptions.ressource_unavailable import ResourceUnavailable
from Models.student import Student
from Models.users import Users
from Models.tempdb import Tempdb
from repos.student_repo_impl import StudentRepoImpl
from services.student_service import StudentService

sr = StudentRepoImpl()
ss = StudentService(sr)


def route(app):
    @app.route("/classrooms/<classroom_id>/students", methods=["GET"])
    def get_students_from_classroom(classroom_id):

        return jsonify([students.json() for students in ss.all_students_in_classroom(classroom_id)])

    @app.route("/students", methods=['GET'])
    def all_students():

        return jsonify([students.json() for students in ss.get_all_students()])

    @app.route("/loging_info", methods=['GET'])
    def all_users():

        return jsonify([users.json() for users in ss.get_all_users()])

    @app.route("/students/<student_id>", methods=['GET'])
    def get_student(student_id):
        try:
            return ss.get_student_by_id(int(student_id)).json(), 200
        except ValueError as e:
            return "Not a valid ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/loging_info/<user_id>", methods=['GET'])
    def get_user(user_id):
        try:
            return ss.get_user_by_id(int(user_id)).json(), 200
        except ValueError as e:
            return "Not a valid ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/students", methods=["POST"])
    def post_students():
        body = request.json

        student = Student(name=body["name"], age=body["age"], grade=body["grade"], administrator=body["administrator"])
        student = ss.create_student(student)

        return student.json()

    @app.route("/tempdatabase", methods=['GET'])
    def all_tempdata():

        return jsonify([users.json() for users in ss.get_all_tempdata()])

    @app.route("/tempdatabase/<temp_id>", methods=['GET'])
    def get_tempdata(temp_id):
        try:
            return ss.get_tempdata_by_id(int(temp_id)).json(), 200
        except ValueError as e:
            return "Not a valid ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/tempdatabase", methods=["POST"])
    def post_tempdatabase():
        body = request.json

        tempdata = Tempdb(tempid=body["tempId"], rmbavailable=body["rmbAvailable"], rmbavailable2=body["rmbAvailable2"],
                           submission=body["submission"], usersubmissionid=body["userSubmissionId"], alreadysubmitted=body["alreadySubmitted"])
        tempdata = ss.create_tempdb(tempdata)

        return tempdata.json()

    #@app.route("/students/<student_id>", methods=["PUT"])
    #def put_classroom(student_id):
    #    body = request.json
    #    student = Student(student_id=student_id, name=body["name"], age=body["age"],
    #                      grade=body["grade"], administrator=body["administrator"])

    #    student = ss.update_student(student)

     #   return student.json()

    @app.route("/students/<student_id>", methods=["DELETE"])
    def del_student(student_id):
        ss.delete_student(student_id)
        return '', 204  # No Content

   # @app.route("/students/<student_id>", methods=["PATCH"])
    #def patch_student(student_id):
     #   a = request.json['A']
      #  if a == "checkout" or a == "checkin":
       #    try:
        #     classroom = ss.checkout_classroom(int(student_id)) if a == "checkout" else ss.checkin_classroom(
         #    int(student_id))
          #   return f"Successfully Checked {'out' if a == 'checkout' else 'in'} movie: {classroom.title}"
          # except ResourceUnavailable as e:
          #   return e.message, 422
          # except ValueError:
         #    return "Not a valid ID", 400
        #else:
        # abort(400, "Body must contain a JSON with an action property and a value of 'checkin' or 'checkout'")
