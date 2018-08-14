from flask import Flask, render_template, request, flash, url_for, redirect, session, g, json,jsonify
from flask_mysqldb import MySQL

# dbconfig
app = Flask(__name__)
app.secret_key = 'hari om tathsath'
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'peasecTIP'
mysql = MySQL(app)

# first page


@app.route('/')
def index():
    return render_template('index.html')

# User  Registration

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


# Authentication


@app.before_request
def before_req():
    g.user = None
    if 'user' in session:
        g.user = session['user']


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
# End of Authentication


# post successful authentication -- Home page
@app.route('/home',methods=['GET','POST'])
def home():
    if g.user:
        user = g.user
        cur = mysql.connection.cursor()
        cur.execute("select * from `attack-pattern`  where created_by='" + user + "'")  # query to be updated in future
        rows = cur.fetchall()
        rowList =[]
        for row in rows:
            rowdict = {
                'id': row[0],
                'type': row[1],
                'name': row[2],
                'description': row[3],
                'created_by': row[4]
            }
            rowList.append(rowdict)
        output = json.dumps(rowList,sort_keys=True, indent=4)
        resp = json.loads(output)
        return render_template('home.html', data=resp)
    else:
        flash("You are not allowed to access without authorization. Kindly enter your credentials and login!! ",
              'error')
        return redirect(url_for('index'))


# Home->View-> View object - route for a new page to view additional info that displays all the corresponding contextual
# information related to the selected SDO(entry)
@app.route('/home/view/<objtype>/<id>', methods=['GET','POST'])
def view_additionalinfo(objtype, id):
    if g.user:
        if objtype == "attack-pattern":
            url = 'view_templates/' + objtype + '.html'
            obj_id = id
            createdBy = g.user
            # Main Attack pattern SDO
            cur = mysql.connection.cursor()
            cur.execute("select * from `" + objtype + "` where sno=%s and created_by=%s", (obj_id, createdBy))
            row_main = cur.fetchone()
            main_SDO = {
                'id': row_main[0],
                'type': row_main[1],
                'name': row_main[2],
                'description': row_main[3]
            }
            output = json.dumps(main_SDO, sort_keys=True, indent=4)
            resp_main = json.loads(output)
            # kill chain
            cur = mysql.connection.cursor()
            query1 = "SELECT KC.sno, KC.obj_id, KC.killchain_name, KC.phase_name, KC.created_by \
                      FROM `killchainphase` AS KC \
                      INNER JOIN `attack-pattern` AS AP on KC.obj_id = AP.sno AND KC.obj_id = %s AND KC.created_by=%s"
            cur.execute(query1, (obj_id, createdBy))
            row_kc = cur.fetchall()
            row_kcList = []
            for row in row_kc:
                rowdict = {
                    'id': row[0],
                    'ref_id': row[1],
                    'killchain_name': row[2],
                    'phase_name': row[3],
                    'created_by': row[4]
                }
                row_kcList.append(rowdict)
            output = json.dumps(row_kcList, sort_keys=True, indent=4)
            resp_kc = json.loads(output)
            # External_references
            cur = mysql.connection.cursor()
            query2 = "SELECT ER.sno, ER.obj_id, ER.src_name, ER.description, ER.url, ER.hash_type, ER.hash_value, ER.external_id, ER.created_by \
                      FROM `external_references` AS ER \
                      INNER JOIN `attack-pattern` AS AP on ER.obj_id = AP.sno AND ER.obj_id = %s AND ER.created_by=%s"
            cur.execute(query2, (obj_id, createdBy))
            row_extref = cur.fetchall()
            row_extrefList = []
            for row in row_extref:
                rowdict = {
                    'id': row[0],
                    'ref_id': row[1],
                    'src_name': row[2],
                    'description': row[3],
                    'url': row[4],
                    'hash_type': row[5],
                    'hash_value': row[6],
                    'external_id': row[7],
                    'created_by': row[8]

                }
                row_extrefList.append(rowdict)
            output = json.dumps(row_extrefList, sort_keys=True, indent=4)
            resp_extref = json.loads(output)
            return render_template(url, main=resp_main, kclist = resp_kc ,extreflist = resp_extref )
    return redirect(url_for('index'))


# Home->View-> update object - route for a new page to add additional info to  a particular selected SDO
@app.route('/home/update/<objtype>/<id>', methods=['GET','POST'])
def update_entry(objtype, id):
    if g.user:
        if objtype:
            url = 'update_templates/' + objtype + '.html'
            obj_id = id
            createdBy= g.user
            cur = mysql.connection.cursor()
            cur.execute("select * from `" + objtype + "` where sno=%s and created_by=%s", (obj_id, createdBy))
            row = cur.fetchone()
            rowdict = {
                 'id': row[0],
                 'type': row[1],
                 'name': row[2],
                 'description': row[3],
                 'created_by': row[4]
            }

            output = json.dumps(rowdict, sort_keys=True, indent=4)
            resp = json.loads(output)
            return render_template(url, data=resp)
    else:
        return redirect(url_for('index'))


# Home->View->additionalinfo-> Delete main obj   ( Deletes the entry from parent table and also the child table)
@app.route('/home/delete', methods=['POST'])
def delete_all_entry():
    if g.user:
        if request.method == 'POST':
            id = request.form['id']
            obj_type = request.form['obj_type']
            createdBy = g.user
            cur = mysql.connection.cursor()
            cur.execute("Delete from `" + obj_type + "` where sno=%s and created_by=%s", (id, createdBy))
            mysql.connection.commit()
            print "Entries deleted successfully"
            return redirect(url_for('home'))
    return redirect(url_for('index'))

# logout
@app.route('/logout')
def logout():

    session.pop('user', None)
    g.user = None
    return redirect(url_for('index'))


#########################

# Attack pattern - Basic SDO creation - Insert

@app.route('/attackpattern',methods=['GET', 'POST'])
def attk_pattern():
    if g.user:
        if request.method == 'POST':
            type = request.form['type']
            name = request.form['nm']
            desc = request.form['desc']
            created_by = request.form['created_by']
            cur = mysql.connection.cursor()
            cur.execute('''INSERT INTO `attack-pattern` (type, name, description, created_by) values (%s, %s, %s, %s)''',
                        (type, name, desc, created_by))
            mysql.connection.commit()
            print('success input data')
        return redirect(url_for('home'))
    else:
        return redirect(url_for('index'))




# kill chain - Insert (Ajax post query)
@app.route('/killchain',methods=['POST'])
def kill_chain_submit():
    if g.user:
        if request.method == 'POST':
            kc_name=request.form['kcName']
            ph_name = request.form['phase_name']
            ref_id = request.form['obj_id']
            created_by = request.form['created_by']
            cur = mysql.connection.cursor()
            cur.execute('''INSERT INTO killchainphase (obj_id, killchain_name, phase_name, created_by) values (%s , %s, %s, %s)''',
                        (ref_id , kc_name, ph_name, created_by))
            mysql.connection.commit()
            print('Successfully entered killchain data')
            return jsonify({'result': 'success'})


# kill chain - update(ajax post query)
@app.route('/updatekillchaindata',methods=['POST'])
def update_killchaindata():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            kc_name = request.json['kc_name']
            phase_name = request.json['kc_phase']
            cur = mysql.connection.cursor()
            cur.execute("UPDATE killchainphase SET killchain_name=%s, phase_name=%s where sno=%s ",(kc_name,phase_name,id))
            mysql.connection.commit()
            print "Successfully update kill chain data"
            return jsonify({'result': 'success'})


# kill chain - delete(ajax post query)
@app.route('/deletekillchaindata', methods=['POST'])
def delete_killchaindata():
    id = request.json['id']
    query = "delete from killchainphase where sno=%s"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()
    print "successfully deleted"
    return jsonify({'result': 'success'})


# External References - Insert (Ajax post query)
@app.route('/insertextref',methods=['POST'])
def insert_extref():
    if g.user:
        if request.method == 'POST':
            src_name = request.form['extref_srcname']
            ref_id = request.form['ref_id']
            description = request.form['extref_desc']
            ext_url = request.form['extref_url']
            hash_type = request.form['hash_type']
            hash_val = request.form['hash_value']
            ext_id = request.form['extref_extid']
            created_by = request.form['created_by']

            cur = mysql.connection.cursor()
            cur.execute('''INSERT INTO external_references (obj_id, src_name, description, url, hash_type, hash_value, external_id, created_by) values (%s, %s, %s, %s, %s, %s, %s, %s)''',
                        (int(ref_id), src_name, description, ext_url, hash_type, hash_val, ext_id, created_by))
            mysql.connection.commit()
            print('Successfully entered External References!!')
            return jsonify({'result': 'success'})

# External references - update (Ajax post query)
@app.route('/updateextrefdata', methods=['POST'])
def update_extref():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            src_name = request.json['src_name']
            description = request.json['description']
            ext_id = request.json['ext_id']
            query = "UPDATE external_references SET src_name=%s, description=%s, external_id=%s where sno=%s"
            cur = mysql.connection.cursor()
            cur.execute(query, (src_name,description,ext_id,id))
            mysql.connection.commit()
            print "successfully Updated"
            return jsonify({'result': 'success'})

# External references - update (Ajax post query)
@app.route('/deleteextrefdata', methods=['POST'])
def delete_extrefdata():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            query = "delete from external_references where sno=%s"
            cur = mysql.connection.cursor()
            cur.execute(query, (id,))
            mysql.connection.commit()
            print "successfully deleted"
            return jsonify({'result': 'success'})


# Attack pattern -update (Ajax post query)
@app.route('/update_attk_pattern', methods=['POST'])
def update_attkpattern():
    if g.user:
        if request.method == 'POST':
            name = request.form['nm']
            desc = request.form['desc']
            id = request.form['id']
            created_by = request.form['created_by']
            cur = mysql.connection.cursor()
            cur.execute('''UPDATE `attack-pattern` SET name=%s, description=%s WHERE sno=%s and created_by=%s''', (name, desc, id, created_by))
            mysql.connection.commit()
            print('Successfully updated!!')
            return jsonify({'result': 'success'})

################ End of Attack pattern #####################


# ********* Campaign ********************

# Campaign - Main object creation - Insert operation








if __name__ == '__main__':
    app.run(debug=True)
