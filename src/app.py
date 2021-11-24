from flask import Flask
from .routes import main, results, projections


# App init
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
app.register_blueprint(main)
app.register_blueprint(results)
app.register_blueprint(projections)
