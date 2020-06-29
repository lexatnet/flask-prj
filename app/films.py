import functools

from flask import (
    Blueprint, 
    flash,
    render_template, 
    request, 
    url_for
)
import os
import sys

from app import auth
    

bp = Blueprint('films', __name__, url_prefix='/films')

@bp.route('/')
def list():
    from app import films_data
    
    return render_template(
        'films/list.html', 
        films = films_data.data
    )
    
@bp.route('/<int:id>')
def details(id):
    from app import films_data
    
    return render_template(
        'films/film-details.html', 
        film = films_data.data[id-1]
    )
    
def get_static_root():
    file_path = os.path.realpath(__file__)
    dir_path = os.path.dirname(file_path)
    return dir_path
    
    
def get_films_images_root():
    dir_path = get_static_root()
    path = os.path.join(dir_path, 'static', 'files', 'films')
    return path
    
@bp.route('/new', methods=['GET', 'POST'])
@auth.login_required
def new():
    from app import films_data
    if request.method == 'POST':
        f = request.files['film-image']
        path = os.path.join(get_films_images_root(), f.filename)
        f.save(path)
        
        film = {
            'name': request.form['name'],
            'tags': [s.strip() for s in request.form['tags'].split()],
            'description': request.form['description'],
            'image': '/'.join(('files', 'films', f.filename))
        }
        films_data.data.append(film)
    
    return render_template(
        'films/film-new.html'
    )

























