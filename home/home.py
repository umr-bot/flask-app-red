from flask import Blueprint, render_template

home_bp = Blueprint('home_bp', __name__,
    template_folder='templates/home',
    static_folder='static',
    static_url_path='/static')

# Load Browser Favorite Icon
#@home_bp.route('/favicon.ico')
#def favicon(): return url_for('static', filename='images/favicon.ico')

@home_bp.route('/')
def list():
    return render_template(
        "home.jinja2",
        title="Home page",
        subtitle="Home page subtitle",
        template="home-page-template"
    )
    #return "<h1 style='color:blue'>You are on the home page!</h1>"
@home_bp.route('/view/<int:home_id>')
def view(home_id):
    if home_id==1:
        return render_template(
        "index.jinja2",
        title="Flask Blueprint Demo",
        subtitle="Demonstration of Flask blueprints in action.",
        template="view-template"
        )
    else: return "<h1 style='color:blue'>Home page with id 1!</h1>"

