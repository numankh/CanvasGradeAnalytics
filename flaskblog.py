from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'c17de30fdb329e7f6146b718efbc9f02'

posts = [
    {
        'author' : 'Numan Khan',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'June 25, 2019'
    },
    {
        'author' : 'Aiza Khan',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'June 25, 2019'
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
