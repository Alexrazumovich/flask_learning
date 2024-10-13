import flask
from flask import Flask,render_template
app=Flask(__name__)


# @app.route('/')
# def films():
#     context={
#         'caption': 'Фильмы',
#         'number':1,
#         'list':['Nina','Alex','Anton','Nikita']
#
#     }
#     return render_template('shablon.html',**context)

@app.route('/')
def films2():
    context={
        'link':'Фильмы'
    }
    return render_template('index2.html',**context)
@app.route('/person/')
def person():
    context={
        'link':'Герои фильмов'
    }
    return render_template('main.html',**context)

if __name__ == '__main__':
    app.run()
