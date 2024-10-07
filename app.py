from flask import Flask, render_template
from flask import url_for
from home import home
from about import about

app = Flask(__name__)

# Load Browser Favorite Icon
@app.route('/favicon.ico')
def favicon(): return url_for('static', filename='images/favicon.ico')

@app.route('/')
def root(): return render_template(
        "root.jinja2",
        title="Base layout",
        subtitle="Base subtitle",
        template="base-template"
    )

app.register_blueprint(home.home_bp, url_prefix='/home', template_folder='templates',static_folder='static')
app.register_blueprint(about.about_bp, url_prefix='/about', template_folder='templates',static_folder='static')
