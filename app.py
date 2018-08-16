from flask import Flask, render_template, request, flash, url_for, redirect, session, g, json,jsonify
from flask_mysqldb import MySQL
from flask_moment import Moment
import datetime

# dbconfig
app = Flask(__name__)
app.secret_key = 'hari om tathsath'
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'peasecTIP'
mysql = MySQL(app)

moment = Moment(app)
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
        mainList = []
        # query for attack pattern
        query_attkpat = "select * from `attack-pattern`  where created_by='" + user + "'"
        cur = mysql.connection.cursor()
        cur.execute(query_attkpat)
        rows_attkpat = cur.fetchall()
        for row in rows_attkpat:
            rowdict = {
                'id': row[0],
                'type': row[1],
                'name': row[2],
                'description': row[3],
                'created_by': row[4]
            }
            mainList.append(rowdict)
        # query for campaign
        query_campaign = "select * from `campaign`  where created_by='" + user + "'"
        cur = mysql.connection.cursor()
        cur.execute(query_campaign)
        rows_campaign = cur.fetchall()
        for row in rows_campaign:
            rowdict = {
                'id': row[0],
                'type': row[1],
                'name': row[2],
                'description': row[3],
                'created_by': row[4]
            }
            mainList.append(rowdict)
        # query for identity
        query_campaign = "select * from `identity`  where created_by='" + user + "'"
        cur = mysql.connection.cursor()
        cur.execute(query_campaign)
        rows_identity = cur.fetchall()
        for row in rows_identity:
            rowdict = {
                'id': row[0],
                'type': row[1],
                'name': row[2],
                'description': row[4],
                'created_by': row[8]
            }
            mainList.append(rowdict)
        # query for indicator
        query_indicator = "select * from `indicator`  where created_by='" + user + "'"
        cur = mysql.connection.cursor()
        cur.execute(query_indicator)
        rows_indicator = cur.fetchall()
        for row in rows_indicator:
              rowdict = {
                   'id': row[0],
                   'type': row[1],
                   'name': row[2],
                   'description': row[4],
                   'created_by': row[8]
               }
              mainList.append(rowdict)
        # query for intrusion-set
        query_indicator = "select * from `intrusion-set`  where created_by='" + user + "'"
        cur = mysql.connection.cursor()
        cur.execute(query_indicator)
        rows_indicator = cur.fetchall()
        for row in rows_indicator:
                rowdict = {
                  'id': row[0],
                  'type': row[1],
                  'name': row[2],
                  'description': row[4],
                  'created_by': row[11]
                }
                mainList.append(rowdict)
        # query for malware
        query_malware = "select * from `malware`  where created_by='" + user + "'"
        cur = mysql.connection.cursor()
        cur.execute(query_malware)
        rows_malware = cur.fetchall()
        for row in rows_malware:
                    rowdict = {
                        'id': row[0],
                        'type': row[1],
                        'name': row[2],
                        'description': row[4],
                        'created_by': row[5]
                    }
                    mainList.append(rowdict)
        output = json.dumps(mainList, sort_keys=True, indent=4)
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
        elif objtype == "campaign":
            url = 'view_templates/' + objtype + '.html'
            obj_id = id
            createdBy = g.user
            # Main campaign SDO
            cur = mysql.connection.cursor()
            cur.execute("select * from `" + objtype + "` where sno=%s and created_by=%s", (obj_id, createdBy))
            row_main = cur.fetchone()
            main_SDO = {
                'id': row_main[0],
                'type': row_main[1],
                'name': row_main[2],
                'description': row_main[3],
                'aliases': row_main[4],
                'first_seen': row_main[5],
                'last_seen': row_main[6],
                'objective': row_main[7]

            }
            output = json.dumps(main_SDO, sort_keys=True, indent=4)
            resp_main = json.loads(output)
            return render_template(url, main=resp_main)
        elif objtype == "identity":
            url = 'view_templates/' + objtype + '.html'
            obj_id = id
            createdBy = g.user
            # Main campaign SDO
            cur = mysql.connection.cursor()
            cur.execute("select * from `" + objtype + "` where sno=%s and created_by=%s", (obj_id, createdBy))
            row_main = cur.fetchone()
            main_SDO = {
                'id': row_main[0],
                'type':row_main[1],
                'name': row_main[2],
                'labels': row_main[3],
                'description': row_main[4],
                'identity_class': row_main[5],
                'sectors': row_main[6],
                'contact_info': row_main[7]
            }
            output = json.dumps(main_SDO, sort_keys=True, indent=4)
            resp_main = json.loads(output)
            return render_template(url, main=resp_main)
        elif objtype == "indicator":
            url = 'view_templates/' + objtype + '.html'
            obj_id = id
            createdBy = g.user
            # Main campaign SDO
            cur = mysql.connection.cursor()
            cur.execute("select * from `" + objtype + "` where sno=%s and created_by=%s", (obj_id, createdBy))
            row_main = cur.fetchone()
            main_SDO = {
                'id': row_main[0],
                'type':row_main[1],
                'name': row_main[2],
                'labels': row_main[3],
                'description': row_main[4],
                'pattern': row_main[5],
                'valid_from': row_main[6],
                'valid_untill': row_main[7]
            }
            output = json.dumps(main_SDO, sort_keys=True, indent=4)
            resp_main = json.loads(output)
            # kill chain
            cur = mysql.connection.cursor()
            query1 = "SELECT KC.sno, KC.obj_id, KC.killchain_name, KC.phase_name, KC.created_by \
                                  FROM `killchainphase` AS KC \
                                  INNER JOIN `indicator` AS IND on KC.obj_id = IND.sno AND KC.obj_id = %s AND KC.created_by=%s"
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
            return render_template(url, main=resp_main, kclist=resp_kc)
        elif objtype == "intrusion-set":
            url = 'view_templates/' + objtype + '.html'
            obj_id = id
            createdBy = g.user
            # Main campaign SDO
            cur = mysql.connection.cursor()
            cur.execute("select * from `" + objtype + "` where sno=%s and created_by=%s", (obj_id, createdBy))
            row_main = cur.fetchone()
            main_SDO = {
                'id': row_main[0],
                'type':row_main[1],
                'name': row_main[2],
                'aliases': row_main[3],
                'description': row_main[4],
                'first_seen': row_main[5],
                'last_seen': row_main[6],
                'goals': row_main[7],
                'resource_level': row_main[8],
                'primary_motive': row_main[9],
                'secondary_motive': row_main[10]

            }
            output = json.dumps(main_SDO, sort_keys=True, indent=4)
            resp_main = json.loads(output)
            return render_template(url, main=resp_main)
        elif objtype == "malware":
            url = 'view_templates/' + objtype + '.html'
            obj_id = id
            createdBy = g.user
            # Main campaign SDO
            cur = mysql.connection.cursor()
            cur.execute("select * from `" + objtype + "` where sno=%s and created_by=%s", (obj_id, createdBy))
            row_main = cur.fetchone()
            main_SDO = {
                'id': row_main[0],
                'type':row_main[1],
                'name': row_main[2],
                'labels': row_main[3],
                'description': row_main[4]
            }
            output = json.dumps(main_SDO, sort_keys=True, indent=4)
            resp_main = json.loads(output)
            # kill chain
            cur = mysql.connection.cursor()
            query1 = "SELECT KC.sno, KC.obj_id, KC.killchain_name, KC.phase_name, KC.created_by \
                                  FROM `killchainphase` AS KC \
                                  INNER JOIN `malware` AS MAL on KC.obj_id = MAL.sno AND KC.obj_id = %s AND KC.created_by=%s"
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
            return render_template(url, main=resp_main, kclist=resp_kc)

    return redirect(url_for('index'))


# Home->View-> update object - route for a new page to add additional info to  a particular selected SDO
@app.route('/home/update/<objtype>/<id>', methods=['GET','POST'])
def update_entry(objtype, id):
    if g.user:
        if objtype == "attack-pattern":
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
        elif objtype == "campaign":
            url = 'update_templates/' + objtype + '.html'
            obj_id = id
            createdBy = g.user
            cur = mysql.connection.cursor()
            cur.execute("select * from `" + objtype + "` where sno=%s and created_by=%s", (obj_id, createdBy))
            row = cur.fetchone()
            rowdict = {
                'id': row[0],
                'type': row[1],
                'name': row[2],
                'description': row[3],
                'aliases': row[4],
                'first_seen': row[5].strftime('%Y-%m-%dT%H:%M'),
                'last_seen': row[6].strftime('%Y-%m-%dT%H:%M'),
                'objective': row[7]
            }

            output = json.dumps(rowdict, sort_keys=True, indent=4)
            resp = json.loads(output)
            return render_template(url, data=resp)
        elif objtype == "identity":
            url = 'update_templates/' + objtype + '.html'
            obj_id = id
            createdBy = g.user
            cur = mysql.connection.cursor()
            cur.execute("select * from `" + objtype + "` where sno=%s and created_by=%s", (obj_id, createdBy))
            row = cur.fetchone()
            rowdict = {
                'id': row[0],
                'type': row[1],
                'name': row[2],
                'labels': row[3],
                'description': row[4],
                'identity_class': row[5],
                'sectors': row[6],
                'contact_info': row[7]
            }

            output = json.dumps(rowdict, sort_keys=True, indent=4)
            resp = json.loads(output)
            return render_template(url, data=resp)
        elif objtype == "indicator":
            url = 'update_templates/' + objtype + '.html'
            obj_id = id
            createdBy = g.user
            cur = mysql.connection.cursor()
            cur.execute("select * from `" + objtype + "` where sno=%s and created_by=%s", (obj_id, createdBy))
            row = cur.fetchone()
            rowdict = {
                'id': row[0],
                'type': row[1],
                'name': row[2],
                'labels': row[3],
                'description': row[4],
                'pattern': row[5],
                'valid_from': row[6].strftime('%Y-%m-%dT%H:%M'),
                'valid_untill': row[7].strftime('%Y-%m-%dT%H:%M')
            }

            output = json.dumps(rowdict, sort_keys=True, indent=4)
            resp = json.loads(output)
            return render_template(url, data=resp)
        elif objtype == "intrusion-set":
            url = 'update_templates/' + objtype + '.html'
            obj_id = id
            createdBy = g.user
            cur = mysql.connection.cursor()
            cur.execute("select * from `" + objtype + "` where sno=%s and created_by=%s", (obj_id, createdBy))
            row = cur.fetchone()
            rowdict = {
                'id': row[0],
                'type':row[1],
                'name': row[2],
                'aliases': row[3],
                'description': row[4],
                'first_seen': row[5].strftime('%Y-%m-%dT%H:%M'),
                'last_seen': row[6].strftime('%Y-%m-%dT%H:%M'),
                'goals': row[7],
                'resource_level': row[8],
                'primary_motive': row[9],
                'secondary_motive': row[10]

            }

            output = json.dumps(rowdict, sort_keys=True, indent=4)
            resp = json.loads(output)
            return render_template(url, data=resp)
        elif objtype == "malware":
            url = 'update_templates/' + objtype + '.html'
            obj_id = id
            createdBy = g.user
            cur = mysql.connection.cursor()
            cur.execute("select * from `" + objtype + "` where sno=%s and created_by=%s", (obj_id, createdBy))
            row = cur.fetchone()
            rowdict = {
                'id': row[0],
                'type': row[1],
                'name': row[2],
                'labels': row[3],
                'description': row[4]
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
            if obj_type == 'attack-pattern':
                # deleting main SDO
                cur = mysql.connection.cursor()
                cur.execute("Delete from `" + obj_type + "` where sno=%s and created_by=%s", (id, createdBy))
                mysql.connection.commit()
                # deleting entries from child table: kill chain phase
                cur = mysql.connection.cursor()
                cur.execute("Delete from killchainphase where obj_id=%s and obj_type = %s and created_by=%s",
                            (id, obj_type, createdBy))
                mysql.connection.commit()
                # deleting entries from child table: External references
                cur = mysql.connection.cursor()
                cur.execute("Delete from external_references where obj_id=%s and obj_type = %s and created_by=%s",
                            (id, obj_type, createdBy))
                mysql.connection.commit()
                print "Entries deleted successfully"
                return redirect(url_for('home'))
            elif obj_type == 'campaign':
                # deleting main SDO
                cur = mysql.connection.cursor()
                cur.execute("Delete from `" + obj_type + "` where sno=%s and created_by=%s", (id, createdBy))
                mysql.connection.commit()
                print "Entries deleted successfully"
                return redirect(url_for('home'))
            elif obj_type == 'identity':
                # deleting main SDO
                cur = mysql.connection.cursor()
                cur.execute("Delete from `" + obj_type + "` where sno=%s and created_by=%s", (id, createdBy))
                mysql.connection.commit()
                print "Entries deleted successfully"
                return redirect(url_for('home'))
            elif obj_type == 'indicator':
                # deleting main SDO
                cur = mysql.connection.cursor()
                cur.execute("Delete from `" + obj_type + "` where sno=%s and created_by=%s", (id, createdBy))
                mysql.connection.commit()
                # deleting entries from child table: kill chain phase
                cur = mysql.connection.cursor()
                cur.execute("Delete from killchainphase where obj_id=%s and obj_type = %s and created_by=%s",
                            (id, obj_type, createdBy))
                mysql.connection.commit()
                print "Entries deleted successfully"
                return redirect(url_for('home'))
            elif obj_type == 'intrusion-set':
                # deleting main SDO
                cur = mysql.connection.cursor()
                cur.execute("Delete from `" + obj_type + "` where sno=%s and created_by=%s", (id, createdBy))
                mysql.connection.commit()
                print "Entries deleted successfully"
                return redirect(url_for('home'))
            elif obj_type == 'malware':
                # deleting main SDO
                cur = mysql.connection.cursor()
                cur.execute("Delete from `" + obj_type + "` where sno=%s and created_by=%s", (id, createdBy))
                mysql.connection.commit()
                # deleting entries from child table: kill chain phase
                cur = mysql.connection.cursor()
                cur.execute("Delete from killchainphase where obj_id=%s and obj_type = %s and created_by=%s",
                            (id, obj_type, createdBy))
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

# Generally used routes for child tables and their respective operation


# kill chain - Insert (Ajax post query)
@app.route('/killchain',methods=['POST'])
def kill_chain_submit():
    if g.user:
        if request.method == 'POST':
            kc_name=request.form['kcName']
            ph_name = request.form['phase_name']
            ref_id = request.form['obj_id']
            ref_type = request.form['obj_type']
            created_by = request.form['created_by']
            cur = mysql.connection.cursor()
            cur.execute('''INSERT INTO killchainphase (obj_id, obj_type, killchain_name, phase_name, created_by) values (%s , %s, %s, %s, %s)''',
                        (ref_id, ref_type, kc_name, ph_name, created_by))
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
            ref_type = request.form['obj_type']
            description = request.form['extref_desc']
            ext_url = request.form['extref_url']
            hash_type = request.form['hash_type']
            hash_val = request.form['hash_value']
            ext_id = request.form['extref_extid']
            created_by = request.form['created_by']

            cur = mysql.connection.cursor()
            cur.execute('''INSERT INTO external_references (obj_id, obj_type, src_name, description, url, hash_type, hash_value, external_id, created_by) values (%s, %s, %s, %s, %s, %s, %s, %s)''',
                        (int(ref_id),ref_type, src_name, description, ext_url, hash_type, hash_val, ext_id, created_by))
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
@app.route('/create_campaign', methods=['POST'])
def create_campaign():
    if g.user:
        if request.method == 'POST':
            type = request.form['type']
            name = request.form['nm']
            description = request.form['desc']
            aliases = request.form['aliases']
            fseen = request.form['first_seen']
            lseen = request.form['last_seen']
            objective = request.form['objective']
            created_by = g.user

            cur = mysql.connection.cursor()
            cur.execute(
                '''INSERT INTO campaign (type, name, description, aliases, first_seen, last_seen, objective, created_by) values (%s, %s, %s, %s, %s, %s, %s, %s)''',
                (type, name, description, aliases, fseen, lseen, objective, created_by))
            mysql.connection.commit()
            print('success input data')
        return redirect(url_for('home'))
    else:
        return redirect(url_for('index'))

@app.route('/update_campaign',methods=['POST'])
def update_campaign():
    if g.user:
        if request.method == 'POST':
            id = request.form['id']
            name = request.form['nm']
            description = request.form['desc']
            aliases = request.form['aliases']
            objective = request.form['objective']
            created_by = g.user
            query = "UPDATE campaign SET name=%s, description=%s, aliases=%s, objective=%s where sno=%s"
            cur = mysql.connection.cursor()
            cur.execute(query, (name, description, aliases,objective, id))
            mysql.connection.commit()
            print "successfully Updated"
            return jsonify({'result': 'success'})
    else:
        return redirect(url_for('index'))


################ End of Campaign #####################

# ********* Identity ********************

# Identity - Main object creation - Insert operation
@app.route('/create_identity', methods=['POST'])
def create_identity():
    if g.user:
        if request.method == 'POST':
            type = request.form['type']
            name = request.form['nm']
            labels = request.form['labels']
            description = request.form['desc']
            id_class = request.form['id_class']
            sectors = request.form['sectors']
            contactinfo = request.form['contactinfo']
            created_by = g.user
            cur = mysql.connection.cursor()
            cur.execute(
                '''INSERT INTO identity (type, name, labels, description, identity_class, sectors, contact_info, created_by) values (%s, %s, %s, %s, %s, %s, %s, %s)''',
                (type, name, labels, description, id_class, sectors, contactinfo, created_by))
            mysql.connection.commit()
            print('success input data')
        return redirect(url_for('home'))
    else:
        return redirect(url_for('index'))


@app.route('/update_identity',methods=['POST'])
def update_identity():
    if g.user:
        if request.method == 'POST':
            id = request.form['id']
            name = request.form['nm']
            labels = request.form['labels']
            description = request.form['desc']
            id_class = request.form['id_class']
            sectors = request.form['sectors']
            contactinfo = request.form['contact_info']
            query = "UPDATE identity SET name=%s, labels=%s, description=%s, identity_class=%s, sectors=%s, contact_info=%s where sno=%s"
            cur = mysql.connection.cursor()
            cur.execute(query, (name, labels, description, id_class, sectors, contactinfo, id))
            mysql.connection.commit()
            print "successfully Updated"
            return redirect(url_for('home'))
    else:
        return redirect(url_for('index'))


################ End of Identity #####################
# ********* Indicator ********************
# Indicator - Main object creation - Insert operation
@app.route('/create_indicator', methods=['POST'])
def create_indicator():
    if g.user:
        if request.method == 'POST':
            type = request.form['type']
            name = request.form['nm']
            labels = request.form['labels']
            description = request.form['desc']
            pattern = request.form['pattern']
            valid_from = request.form['valid_from']
            valid_untill = request.form['valid_untill']
            created_by = g.user
            cur = mysql.connection.cursor()
            cur.execute(
                '''INSERT INTO indicator (type, name, labels, description, pattern, valid_from, valid_untill, created_by) values (%s, %s, %s, %s, %s, %s, %s, %s)''',
                (type, name, labels, description, pattern, valid_from, valid_untill, created_by))
            mysql.connection.commit()
            print('success input data')
        return redirect(url_for('home'))
    else:
        return redirect(url_for('index'))


@app.route('/update_indicator',methods=['POST'])
def update_indicator():
    if g.user:
        if request.method == 'POST':
            id = request.form['id']
            name = request.form['nm']
            labels = request.form['labels']
            description = request.form['desc']
            pattern = request.form['pattern']
            valid_from = request.form['valid_from']
            valid_untill = request.form['valid_untill']
            query = "UPDATE indicator SET name=%s, labels=%s, description=%s, pattern=%s, valid_from=%s, valid_untill=%s where sno=%s"
            cur = mysql.connection.cursor()
            cur.execute(query, (name, labels, description, pattern, valid_from, valid_untill, id))
            mysql.connection.commit()
            print "successfully Updated"
        return redirect(url_for('home'))
    else:
        return redirect(url_for('index'))

################ End of Indicator #####################


# ********* Intrusion set ********************
# Intrusion set - Main object creation - Insert operation
@app.route('/create_intrusion-set', methods=['POST'])
def create_intrusionset():
    if g.user:
        if request.method == 'POST':
            type = request.form['type']
            name = request.form['nm']
            aliases = request.form['aliases']
            description = request.form['desc']
            first_seen = request.form['first_seen']
            last_seen = request.form['last_seen']
            goals = request.form['goals']
            res_level = request.form['res_level']
            prim_motiv = request.form['prim_motiv']
            sec_motiv = request.form['sec_motiv']
            created_by = g.user
            cur = mysql.connection.cursor()
            cur.execute(
                '''INSERT INTO `intrusion-set` (type, name, aliases, description, first_seen, last_seen, goals,
                 resource_level, primary_motive, secondary_motive, created_by) 
                 values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                (type, name, aliases, description, first_seen, last_seen, goals, res_level, prim_motiv, sec_motiv, created_by))
            mysql.connection.commit()
            print('success input data')
        return redirect(url_for('home'))
    else:
        return redirect(url_for('index'))


@app.route('/update_intrusionset', methods=['POST'])
def update_intrusionset():
    if g.user:
        if request.method == 'POST':
            id = request.form['id']
            name = request.form['nm']
            aliases = request.form['aliases']
            description = request.form['desc']
            first_seen = request.form['first_seen']
            last_seen = request.form['last_seen']
            goals = request.form['goals']
            res_level = request.form['res_level']
            prim_motiv = request.form['prim_motiv']
            sec_motiv = request.form['sec_motiv']
            cur = mysql.connection.cursor()
            cur.execute(
                '''UPDATE `intrusion-set` SET name=%s, aliases=%s, description=%s, first_seen=%s, last_seen=%s, goals=%s, resource_level=%s, primary_motive=%s, secondary_motive=%s WHERE sno=%s ''',
                (name, aliases, description, first_seen, last_seen, goals, res_level, prim_motiv, sec_motiv, id))
            mysql.connection.commit()
            print "successfully Updated"
        return redirect(url_for('home'))
    else:
        return redirect(url_for('index'))


################ End of Intrusion set #####################

# ********* Malware ********************
# Malware- Main object creation - Insert operation
@app.route('/create_malware', methods=['POST'])
def create_malware():
    if g.user:
        if request.method == 'POST':
            type = request.form['type']
            name = request.form['nm']
            labels = request.form['labels']
            description = request.form['desc']
            created_by = g.user
            cur = mysql.connection.cursor()
            cur.execute(
                '''INSERT INTO `malware` (type, name, labels, description, created_by) 
                 values (%s, %s, %s, %s, %s)''',
                (type, name, labels, description, created_by))
            mysql.connection.commit()
            print('success input data')
        return redirect(url_for('home'))
    else:
        return redirect(url_for('index'))


@app.route('/update_malware', methods=['POST'])
def update_malware():
    if g.user:
        if request.method == 'POST':
            id = request.form['id']
            name = request.form['nm']
            labels = request.form['labels']
            description = request.form['desc']
            cur = mysql.connection.cursor()
            cur.execute(
                '''UPDATE `malware` SET name=%s, labels=%s, description=%s WHERE sno=%s ''',
                (name, labels, description, id))
            mysql.connection.commit()
            print "successfully Updated"
        return redirect(url_for('home'))
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
