"""App entry point."""

import flask_login
from flask import request
from flask import url_for
from flask import redirect
from flask import Blueprint, render_template

from movie import create_app


app = create_app()
app.debug = True


@app.route("/org_chart", methods=["GET", "POST"])
def org_chart():
    charts = []
    return render_template(
        'org_chart.html',
        charts=charts,
        
    )


if __name__ == "__main__":
    app.run(host='localhost', port=5000, threaded=False)

