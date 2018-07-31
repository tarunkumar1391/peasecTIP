from flask import Flask, render_template, request, flash, url_for, redirect, session, g
from flask_mysqldb import MySQL
from stix2 import AttackPattern



app = Flask(__name__)
app.secret_key = 'hari om tathsath'
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'peasecTIP'
mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        session.pop('user', None)

        username = request.form['uname']
        password = request.form['passwd']
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * from users where username='" + username + "' and password='" + password + "'")
        data = cursor.fetchone()
        if data is None:
            flash("Username or Password is wrong, please check credentials and try again!!", 'error')
            return redirect(url_for('index'))
        else:
            session['user'] = username
            return redirect(url_for('home'))


@app.before_request
def before_req():
    g.user = None
    if 'user' in session:
        g.user = session['user']


# post successful auth
@app.route('/home')
def home():
    if g.user:
        return render_template('home.html')
    else:
        flash("You are not allowed to access without authorization. Kindly enter your credentials and login!! ",
              'error')
        return redirect(url_for('index'))


@app.route('/logout')
def logout():

    session.pop('user', None)
    g.user = None
    return redirect(url_for('index'))


@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
            fname = request.form['fname']
            lname = request.form['lname']
            email = request.form['email']
            username = request.form['uname']
            passwd = request.form['passwd1']
            cur = mysql.connection.cursor()
            cur.execute('''INSERT INTO users (fname, lname, email, username, password) values (%s, %s, %s, %s, %s)''',
                        (fname, lname, email, username, passwd))
            mysql.connection.commit()
            print('success input data')
            flash("User has been registered successfully", category='info')
    return redirect(url_for('home'))


@app.route('/attackpattern',methods=['GET', 'POST'])
def attk_pattern():
    if g.user:
        if request.method == 'POST':
            type = request.form['type']
            name = request.form['nm']
            desc = request.form['desc']
            kc_phases = request.form['kcp']
            ext_ref = request.form['exref']
            attk_pat = AttackPattern(name=name, description=desc)
        return render_template("response.html",resp = attk_pat)
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
