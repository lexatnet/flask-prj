cd %HOMEPATH%\Desktop\prj
CALL venv\Scripts\activate
set FLASK_APP=app
set FLASK_ENV=development
set FLASK_DEBUG=1
python -m flask run

