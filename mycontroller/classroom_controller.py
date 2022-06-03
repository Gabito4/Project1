from flask import request, jsonify
from werkzeug.exceptions import abort

from exceptions.resource_not_found import ResourceNotFound
from exceptions.ressource_unavailable import ResourceUnavailable
from Models.classroom import Classroom
from repos.classroom_repo_impl import ClassroomRepoImpl
from services.classroom_service import ClassroomService

cr = ClassroomRepoImpl()
cs = ClassroomService(cr)


def route(app):
    @app.route("/classrooms", methods=['GET'])
    def get_all_classrooms():
        return jsonify([classroom.json() for classroom in cs.get_all_classrooms()])

    @app.route("/classrooms/<classroom_id>", methods=['GET'])
    def get_classroom(classroom_id):
        try:
            return cs.get_classroom_by_id(int(classroom_id)).json(), 200
        except ValueError as e:
            return "Not a valid ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/classrooms", methods=["POST"])
    def post_classroom():
        body = request.json

        classroom = Classroom(title=body["title"], price=body["price"])
        classroom = cs.create_classroom(classroom)

        return classroom.json()

    @app.route("/classrooms/<classroom_id>", methods=["PUT"])
    def put_classroom(classroom_id):
        body = request.json
        classroom = Classroom(classroom_id=classroom_id, title=body["title"], price=body["price"],
                              start_date=body["startDate"], grade=body["grade"])

        classroom = cs.update_classroom(classroom)

        return classroom.json()

    @app.route("/classrooms/<classroom_id>", methods=["DELETE"])
    def del_classroom(classroom_id):
        cs.delete_classroom(classroom_id)
        return '', 204  # No Content

    @app.route("/classrooms/<classroom_id>", methods=["PATCH"])
    def patch_classroom(classroom_id):
        # # For P0
        # body = request.json
        # if "deposit" in body:
        #     # Call your AccountService deposit func.
        # elif "withdraw" in body:
        #     # Call your AccountService withdraw func.
        # else:
        #     # Return 400, Bad Request

        a = request.json['A']  # Action will have a value of 'checkin' or 'checkout'

        # if action == 'checkout':
        #     try:
        #         movie = ms.checkout_movie(int(movie_id))
        #         return f"Successfully Checked out: {movie.title}", 200
        #     except ResourceUnavailable as e:
        #         return e.message, 422
        #     except ValueError:
        #         return "Not a valid ID", 400
        # elif action == 'checkin':
        #     try:
        #         movie = ms.checkin_movie(int(movie_id))
        #         return f"Successfully Checked in: {movie.title}", 200
        #     except ResourceUnavailable as e:
        #         return e.message, 422
        #     except ValueError:
        #         return "Not a valid ID", 400

        #if a == "checkout" or a == "checkin":
        #    try:
        #        classroom = cs.checkout_classroom(int(classroom_id)) if a == "checkout" else cs.checkin_classroom(
         #           int(classroom_id))
         #       return f"Successfully Checked {'out' if a == 'checkout' else 'in'} movie: {classroom.title}"
         #   except ResourceUnavailable as e:
         #       return e.message, 422
         #   except ValueError:
        #        return "Not a valid ID", 400
        #else:
         #   abort(400, "Body must contain a JSON with an action property and a value of 'checkin' or 'checkout'")
