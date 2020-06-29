import functools

from flask import (
    Blueprint, 
	flash,
	render_template, 
	request, 
	url_for,
	redirect,
    session,
    g
)

users = [
    {
        'name': 'admin',
        'pass': 'admin'
    }
]

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['pass']
    
        ul = list(
            filter(
                lambda o: o['name'] == name, 
                users
            )
        )
        
        if len(ul) > 0:
            u = ul[0]
            if u['pass'] == password:
                session['user_name'] = u['name']
                return redirect(url_for('index.root'))
        flash('Not valid user credentials.')
    
    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index.root'))



@bp.before_app_request
def load_logged_in_user():
    username = session.get('user_name')
    
    if username is None:
        g.user = None
    else:
        g.user = username
     
    
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            flash('Login required.')
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view



























    