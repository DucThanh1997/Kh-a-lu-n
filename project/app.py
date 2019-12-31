from flask import Flask
from flask_restful import Api


from config import Config



app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)


# @app.before_first_request



# api.add_resource(Classs, "/class", "/class/<int:id>")
# api.add_resource(User, "/user", "/user/<string:ma>")

# api.add_resource(
#     Student_And_Class, "/danhsach",
#                        "/danhsach/<int:id_lop>",
#                        "/danhsach/<int:id_lop>",
#                        "/danhsach/<int:id_lop>/<string:ma>"
# )

# api.add_resource(Teacher_And_Class, "/teach", "/teach/<int:id_lop>/<string:ma>", "/teach/<int:id_lop>")
# api.add_resource(UploadAva, "/upload/<string:ma>", "/upload/<string:ma>/<string:filename>")

if __name__ == "__main__":
    app.run(port=5000, debug=True)