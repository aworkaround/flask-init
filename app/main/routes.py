from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def home():
    country_name = 'India'
    return render_template('main/index.html', country_name=country_name)
