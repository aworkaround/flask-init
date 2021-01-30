from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def home():
    author_name = 'kamal'
    author_name = author_name.title()
    return render_template('main/index.html', author_name=author_name)
