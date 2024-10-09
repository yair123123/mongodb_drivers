from flask import Flask
from controllers.driver_controller import driver_blueprints

app = Flask(__name__)
app.register_blueprint(driver_blueprints)
if __name__ == '__main__':
    app.run(debug=True)
