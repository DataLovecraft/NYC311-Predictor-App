
from functools import lru_cache

from flask import Flask, render_template, request

from ml_editor.ml_editor import get_recommendations_from_input
import ml_editor.model_v2 as v2_model
import ml_editor.model_v3 as v3_model

app = Flask(__name__)


@app.route("/")
def landing_page():
    """
    Renders landing page
    """
    return render_template("landing.html")
