from flask import Flask
from Application.Controllers.countries_controller import countries_controller_api


app = Flask(__name__)

app.register_blueprint(countries_controller_api)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()







