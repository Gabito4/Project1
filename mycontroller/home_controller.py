
def route(app):
    @app.route("/")
    def hello():
        return "Hello, World!"

    @app.route("/contact")
    def contact():
        return "Contact Us via Email: RevatureUniversity@email.com or by Phone: (555) 555-5555"
