from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/ladder.html')
def ladder():
    return render_template('ladder.html')

@main.route('/matches.html', methods=['GET', 'POST'])
def matches():
    if request.method == 'POST':
        return render_template('matches.html')  # or redirect as needed
    
    return render_template('matches.html')


@main.route('/profile.html')
def profile():
    return render_template('profile.html')