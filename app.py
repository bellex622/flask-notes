"""Flask app for notes"""

from flask import Flask, redirect, render_template, request, session, flash
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, User
from forms import RegistrationForm, LoginForm, CSRFProtectForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///notes_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!" #put in a separate file

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

SESSION_KEY = 'username'

@app.get("/")
def root():
    """redirect to register form"""

    return redirect('/register')


@app.route("/register", methods=["GET", "POST"])
def register():
    """display registration form; handle user registration"""

    if SESSION_KEY in session:
        return redirect(f'/users/{session[SESSION_KEY]}')

    form = RegistrationForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data

        user = User.register(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email
        )

        db.session.commit()#moving in to register method

        session[SESSION_KEY] = user.username #make a global variable for "username"

        return redirect(f'/users/{user.username}')

    else:

        return render_template('registration_form.html', form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    """display login form; handle user login"""

    #check if a user already in session
    if SESSION_KEY in session:
        return redirect(f'/users/{session[SESSION_KEY]}')

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)
        print("\n\n\nuser is ---------->", user)

        if user:
            session[SESSION_KEY] = user.username

            print('*****session', session)
            return redirect(f'/users/{user.username}')

        else:
            form.username.errors = ["Bad name/password"]

    return render_template('login_form.html', form=form)


@app.get('/users/<username>')
def display_user(username):
    """Show information about a user"""

    user = User.query.get_or_404(username)
    form = CSRFProtectForm()

    #if session.get("username")==username

    if "username" not in session or session.get(SESSION_KEY) != username:
        flash("You must be logged in to view!")
        return redirect('/login')

    return render_template('user_details.html', user=user, form=form)


@app.post('/logout')
def logout():
    """logout user and redirect to homepage"""

    form = CSRFProtectForm()

    if form.validate_on_submit():
        session.pop(SESSION_KEY)
        print("----->after logout session", session)

    #else, flash message


    return redirect('/')
