from mycontroller import classroom_controller, home_controller, student_controller


def route(app):
    home_controller.route(app)
    classroom_controller.route(app)
    student_controller.route(app)
