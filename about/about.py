from flask import Blueprint, render_template

about_bp = Blueprint('about_bp', __name__,
    template_folder='templates/about',
    static_folder='static',
    static_url_path='/static')

# Load Browser Favorite Icon
#@home_bp.route('/favicon.ico')
#def favicon(): return url_for('static', filename='images/favicon.ico')

@about_bp.route('/')
def list():
    return render_template(
        "about.jinja2",
        title="About page",
        subtitle="About page subtitle",
        template="home-page-template"
    )

