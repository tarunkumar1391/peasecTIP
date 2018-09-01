from flask import Flask, render_template, request, flash, url_for, redirect, session, g, json, jsonify
from flask_mysqldb import MySQL
from flask_moment import Moment


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
@app.route('/home', methods=['GET', 'POST'])
def home():
    if g.user:
        user = g.user
        mainlist = []
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
            mainlist.append(rowdict)
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
            mainlist.append(rowdict)
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
            mainlist.append(rowdict)
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
                mainlist.append(rowdict)
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
                mainlist.append(rowdict)
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
                    mainlist.append(rowdict)
        # query for report
        query_report = "select * from `report`  where created_by='" + user + "'"
        cur = mysql.connection.cursor()
        cur.execute(query_report)
        rows_report = cur.fetchall()
        for row in rows_report:
            rowdict = {
                'id': row[0],
                'type': row[1],
                'name': row[2],
                'description': row[4],
                'created_by': row[5]
            }
            mainlist.append(rowdict)
        # query for threat-actor
        query_report = "select * from `threat-actor`  where created_by='" + user + "'"
        cur = mysql.connection.cursor()
        cur.execute(query_report)
        rows_report= cur.fetchall()
        for row in rows_report:
            rowdict = {
                'id': row[0],
                'type': row[1],
                'name': row[2],
                'description': row[5],
                'created_by': row[13]
            }
            mainlist.append(rowdict)
        # query for tool
        query_tool = "select * from `tool`  where created_by='" + user + "'"
        cur = mysql.connection.cursor()
        cur.execute(query_tool)
        rows_tool= cur.fetchall()
        for row in rows_tool:
            rowdict = {
                'id': row[0],
                'type': row[1],
                'name': row[2],
                'description': row[4],
                'created_by': row[5]
            }
            mainlist.append(rowdict)
        # query for vulnerability
        query_vul = "select * from `vulnerability`  where created_by='" + user + "'"
        cur = mysql.connection.cursor()
        cur.execute(query_vul)
        rows_vul= cur.fetchall()
        for row in rows_vul:
            rowdict = {
                'id': row[0],
                'type': row[1],
                'name': row[2],
                'description': row[3],
                'created_by': row[4]
            }
            mainlist.append(rowdict)
        # query for MAEC - Behavior
        query_beh = "select * from `behavior`  where created_by='" + user + "'"
        cur = mysql.connection.cursor()
        cur.execute(query_beh)
        rows_beh= cur.fetchall()
        for row in rows_beh:
            rowdict = {
                'id': row[0],
                'type': row[1],
                'name': row[2],
                'description': row[3],
                'created_by': row[4]
            }
            mainlist.append(rowdict)
        # query for MAEC - Collection
        query_coll = "select * from `collection`  where created_by='" + user + "'"
        cur = mysql.connection.cursor()
        cur.execute(query_coll)
        rows_coll= cur.fetchall()
        for row in rows_coll:
            rowdict = {
                'id': row[0],
                'type': row[1],
                'description': row[2],
                'created_by': row[4]
            }
            mainlist.append(rowdict)
        # query for MAEC - Malware action
        query_malaction = "select * from `malware-action`  where created_by='" + user + "'"
        cur = mysql.connection.cursor()
        cur.execute(query_malaction)
        rows_malaction= cur.fetchall()
        for row in rows_malaction:
            rowdict = {
                'id': row[0],
                'type': row[1],
                'name': row[2],
                'description': row[3],
                'created_by': row[8]
            }
            mainlist.append(rowdict)
        # query for MAEC - Malware family
        query_malfamily = "select * from `malware-family`  where created_by='" + user + "'"
        cur = mysql.connection.cursor()
        cur.execute(query_malfamily)
        rows_malfamily= cur.fetchall()
        for row in rows_malfamily:
            rowdict = {
                'id': row[0],
                'type': row[1],
                'name': row[2],
                'description': row[3],
                'created_by': row[8]
            }
            mainlist.append(rowdict)
        output = json.dumps(mainlist, sort_keys=True, indent=4)
        resp = json.loads(output)
        return render_template('home.html', data=resp)
    else:
        flash("You are not allowed to access without authorization. Kindly enter your credentials and login!! ",
              'error')
        return redirect(url_for('index'))


# Home->View-> View object - route for a new page to view additional info that displays all the corresponding contextual
# information related to the selected SDO(entry)
@app.route('/home/view/<objtype>/<id>', methods=['GET', 'POST'])
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
                      FROM `kill_chain_phase` AS KC \
                      INNER JOIN `attack-pattern` AS AP on KC.obj_id = AP.sno AND KC.obj_type = AP.type AND  KC.obj_id = %s AND KC.obj_type = %s AND KC.created_by=%s"
            cur.execute(query1, (obj_id, objtype, createdBy))
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
                      INNER JOIN `attack-pattern` AS AP on ER.obj_id = AP.sno AND ER.obj_type = AP.type AND ER.obj_id = %s AND ER.obj_type = %s AND ER.created_by=%s"
            cur.execute(query2, (obj_id, objtype, createdBy))
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
            response_extref = json.loads(output)
            return render_template(url, main=resp_main, kclist = resp_kc ,extreflist = response_extref )
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
                                  FROM `kill_chain_phase` AS KC \
                                  INNER JOIN `indicator` AS IND on KC.obj_id = IND.sno AND KC.obj_type = IND.type AND KC.obj_id = %s AND KC.obj_type = %s AND KC.created_by=%s"
            cur.execute(query1, (obj_id, objtype, createdBy))
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
                                  FROM `kill_chain_phase` AS KC \
                                  INNER JOIN `malware` AS MAL on KC.obj_id = MAL.sno AND KC.obj_type = MAL.type AND KC.obj_id = %s AND KC.obj_type = %s AND KC.created_by=%s"
            cur.execute(query1, (obj_id, objtype, createdBy))
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
        elif objtype == "report":
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
                'labels': row_main[4],
                'published': row_main[5],
                'obj_references': row_main[6]

            }
            output = json.dumps(main_SDO, sort_keys=True, indent=4)
            resp_main = json.loads(output)
            return render_template(url, main=resp_main)
        elif objtype == "threat-actor":
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
                'labels': row_main[3],
                'aliases': row_main[4],
                'description': row_main[5],
                'roles': row_main[6],
                'goals': row_main[7],
                'sophistication': row_main[8],
                'resource_level': row_main[9],
                'primary_motivation': row_main[10],
                'secondary_motivations': row_main[11],
                'personal_motivations': row_main[12]
            }
            output = json.dumps(main_SDO, sort_keys=True, indent=4)
            resp_main = json.loads(output)
            return render_template(url, main=resp_main)
        elif objtype == "tool":
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
                'labels': row_main[3],
                'description': row_main[4],
                'tool_version': row_main[5]

            }
            output = json.dumps(main_SDO, sort_keys=True, indent=4)
            resp_main = json.loads(output)
            # kill chain
            cur = mysql.connection.cursor()
            query1 = "SELECT KC.sno, KC.obj_id, KC.killchain_name, KC.phase_name, KC.created_by \
                                              FROM `kill_chain_phase` AS KC \
                                              INNER JOIN `tool` AS TOO on KC.obj_id = TOO.sno AND KC.obj_type= TOO.type AND KC.obj_id = %s AND KC.obj_type = %s AND KC.created_by=%s"
            cur.execute(query1, (obj_id, objtype, createdBy))
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
        elif objtype == "vulnerability":
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
                'description': row_main[3]
            }
            output = json.dumps(main_SDO, sort_keys=True, indent=4)
            resp_main = json.loads(output)
            # External_references
            cur = mysql.connection.cursor()
            query2 = "SELECT ER.sno, ER.obj_id, ER.src_name, ER.description, ER.url, ER.hash_type, ER.hash_value, ER.external_id, ER.created_by \
                      FROM `external_references` AS ER \
                      INNER JOIN `vulnerability` AS VU on ER.obj_id = VU.sno AND  ER.obj_type = VU.type AND ER.obj_id = %s AND ER.obj_type = %s AND ER.created_by=%s"
            cur.execute(query2, (obj_id, objtype, createdBy))
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
            response_extref = json.loads(output)
            return render_template(url, main=resp_main, extreflist = response_extref)
        elif objtype == "behavior":
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
                'timestamp': row_main[4],
                'attributes': row_main[5],
                'action_refs': row_main[6]


            }
            output = json.dumps(main_SDO, sort_keys=True, indent=4)
            resp_main = json.loads(output)
            # External_references
            cur = mysql.connection.cursor()
            query2 = "SELECT ER.sno, ER.obj_id, ER.src_name, ER.description, ER.url, ER.hash_type, ER.hash_value, ER.external_id, ER.created_by \
                      FROM `external_references` AS ER \
                      INNER JOIN `behavior` AS BE on ER.obj_id = BE.sno AND  ER.obj_type = BE.type AND ER.obj_id = %s AND ER.obj_type = %s AND ER.created_by=%s"
            cur.execute(query2, (obj_id, objtype, createdBy))
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
            response_extref = json.loads(output)
            return render_template(url, main=resp_main, extreflist=response_extref)
        elif objtype == "collection":
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
                'description': row_main[2],
                'association_type': row_main[3],
                'entity_refs': row_main[4],
                'observable_refs': row_main[5]

            }
            output = json.dumps(main_SDO, sort_keys=True, indent=4)
            resp_main = json.loads(output)
            return render_template(url, main=resp_main)
        elif objtype == "malware-action":
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
                'is_successful': row_main[4],
                'timestamp': row_main[5]
            }
            output = json.dumps(main_SDO, sort_keys=True, indent=4)
            resp_main = json.loads(output)
            # API call
            cur = mysql.connection.cursor()
            query1 = "SELECT API.sno, API.obj_id, API.obj_type, API.address, API.return_value, API.parameters, " \
                     "API.function_name, API.created_by \
                      FROM `api-call` AS API \
                      INNER JOIN `malware-action` AS MACT on API.obj_id = MACT.sno AND API.obj_type= MACT.type " \
                     "AND API.obj_id = %s AND API.obj_type = %s AND API.created_by=%s"
            cur.execute(query1, (obj_id, objtype, createdBy))
            row_apicall = cur.fetchall()
            row_apicall_list = []
            for row in row_apicall:
                rowdict = {
                    'id': row[0],
                    'address': row[3],
                    'return_value': row[4],
                    'parameters': row[5],
                    'function_name': row[6]
                }
                row_apicall_list.append(rowdict)
            output = json.dumps(row_apicall_list, sort_keys=True, indent=4)
            resp_apicall = json.loads(output)
            return render_template(url, main=resp_main, apidata=resp_apicall)
    return redirect(url_for('index'))


# Home->View-> update object - route for a new page to add additional info to  a particular selected SDO
@app.route('/home/update/<objtype>/<id>', methods=['GET','POST'])
def update_entry(objtype, id):
    if g.user:
        # stix objects
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
        elif objtype == "report":
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
                'labels': row[4],
                'published': row[5].strftime('%Y-%m-%dT%H:%M'),
                'obj_references': row[6]
            }

            output = json.dumps(rowdict, sort_keys=True, indent=4)
            resp = json.loads(output)
            return render_template(url, data=resp)
        elif objtype == "threat-actor":
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
                'aliases': row[4],
                'description': row[5],
                'roles': row[6],
                'goals': row[7],
                'sophistication': row[8],
                'resource_level': row[9],
                'primary_motivation': row[10],
                'secondary_motivations': row[11],
                'personal_motivations': row[12]
            }

            output = json.dumps(rowdict, sort_keys=True, indent=4)
            resp = json.loads(output)
            return render_template(url, data=resp)
        elif objtype == "tool":
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
                'tool_version': row[5]
            }

            output = json.dumps(rowdict, sort_keys=True, indent=4)
            resp = json.loads(output)
            return render_template(url, data=resp)
        elif objtype == "vulnerability":
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
                'description': row[3]
            }
            output = json.dumps(rowdict, sort_keys=True, indent=4)
            resp = json.loads(output)
            return render_template(url, data=resp)
        # MAEC objects
        elif objtype == "behavior":
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
                'timestamp': row[4].strftime('%Y-%m-%dT%H:%M'),
                'attributes': row[5],
                'action_refs': row[6]

            }
            output = json.dumps(rowdict, sort_keys=True, indent=4)
            resp = json.loads(output)
            return render_template(url, data=resp)
        elif objtype == "collection":
            url = 'update_templates/' + objtype + '.html'
            obj_id = id
            createdBy = g.user
            cur = mysql.connection.cursor()
            cur.execute("select * from `" + objtype + "` where sno=%s and created_by=%s", (obj_id, createdBy))
            row = cur.fetchone()
            rowdict = {
                'id': row[0],
                'type': row[1],
                'description': row[2],
                'association_type': row[3],
                'entity_refs': row[4],
                'observable_refs': row[5]
            }
            output = json.dumps(rowdict, sort_keys=True, indent=4)
            resp = json.loads(output)
            return render_template(url, data=resp)
        elif objtype == "malware-action":
            url = 'update_templates/' + objtype + '.html'
            obj_id = id
            createdBy = g.user
            # main
            cur = mysql.connection.cursor()
            cur.execute("select * from `" + objtype + "` where sno=%s and created_by=%s", (obj_id, createdBy))
            row = cur.fetchone()
            rowdict = {
                'id': row[0],
                'type': row[1],
                'name': row[2],
                'description': row[3],
                'is_successful': row[4],
                'timestamp': row[5].strftime('%Y-%m-%dT%H:%M')
            }
            output = json.dumps(rowdict, sort_keys=True, indent=4)
            resp = json.loads(output)

            # input_refs for main object
            input_full_list = []
            # input_artifact
            cur = mysql.connection.cursor()
            cur.execute("select sno, type from `artifact` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s",
                (obj_id, objtype, createdBy))
            artifact_main = cur.fetchall()
            for row in artifact_main:
                mainrowdict = {
                    'id': row[0],
                    'type': row[1]
                }
                input_full_list.append(mainrowdict)

            # input_AS
            cur = mysql.connection.cursor()
            cur.execute("select sno, type from `autonomous-system` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s",
                (obj_id, objtype, createdBy))
            as_main = cur.fetchall()
            for row in as_main:
                mainrowdict = {
                    'id': row[0],
                    'type': row[1]
                }
                input_full_list.append(mainrowdict)
            # input_directory
            cur = mysql.connection.cursor()
            cur.execute("select sno, type from `directory` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s",
                (obj_id, objtype, createdBy))
            directory_main = cur.fetchall()
            for row in directory_main:
                mainrowdict = {
                    'id': row[0],
                    'type': row[1]
                }
                input_full_list.append(mainrowdict)
            # input_domainname
            cur = mysql.connection.cursor()
            cur.execute("select sno, type from `domain-name` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s",
                (obj_id, objtype, createdBy))
            domainname_main = cur.fetchall()
            for row in domainname_main:
                mainrowdict = {
                    'id': row[0],
                    'type': row[1]
                }
                input_full_list.append(mainrowdict)
            # input_emailaddr
            cur = mysql.connection.cursor()
            cur.execute("select sno, type from `email-addr` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s",
                (obj_id, objtype, createdBy))
            emailaddr_main = cur.fetchall()
            for row in emailaddr_main:
                mainrowdict = {
                    'id': row[0],
                    'type': row[1]
                }
                input_full_list.append(mainrowdict)
            # input_emailmsg
            cur = mysql.connection.cursor()
            cur.execute("select sno, type from `email-message` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s",
                        (obj_id, objtype, createdBy))
            emailmsg_main = cur.fetchall()
            for row in emailmsg_main:
                mainrowdict = {
                    'id': row[0],
                    'type': row[1]
                }
                input_full_list.append(mainrowdict)
            # input_file
            cur = mysql.connection.cursor()
            cur.execute("select sno, type from `file` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s",
                        (obj_id, objtype, createdBy))
            file_main = cur.fetchall()
            for row in file_main:
                mainrowdict = {
                    'id': row[0],
                    'type': row[1]
                }
                input_full_list.append(mainrowdict)
            # input_ipv4
            cur = mysql.connection.cursor()
            cur.execute("select sno, type from `ipv4-addr` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s",
                        (obj_id, objtype, createdBy))
            ipv4_main = cur.fetchall()
            for row in ipv4_main:
                mainrowdict = {
                    'id': row[0],
                    'type': row[1]
                }
                input_full_list.append(mainrowdict)
            # input_ipv6
            cur = mysql.connection.cursor()
            cur.execute("select sno, type from `ipv6-addr` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s",
                        (obj_id, objtype, createdBy))
            ipv4_main = cur.fetchall()
            for row in ipv4_main:
                mainrowdict = {
                    'id': row[0],
                    'type': row[1]
                }
                input_full_list.append(mainrowdict)
            # input_macaddr
            cur = mysql.connection.cursor()
            cur.execute("select sno, type from `mac-addr` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s",
                        (obj_id, objtype, createdBy))
            macaddr_main = cur.fetchall()
            for row in macaddr_main:
                mainrowdict = {
                    'id': row[0],
                    'type': row[1]
                }
                input_full_list.append(mainrowdict)
            # input_networktraffic
            cur = mysql.connection.cursor()
            cur.execute("select sno, type from `network-traffic` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s",
                        (obj_id, objtype, createdBy))
            networktraffic_main = cur.fetchall()
            for row in networktraffic_main:
                mainrowdict = {
                    'id': row[0],
                    'type': row[1]
                }
                input_full_list.append(mainrowdict)
            # input_ process
            cur = mysql.connection.cursor()
            cur.execute("select sno, type from `process` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s",
                        (obj_id, objtype, createdBy))
            process_main = cur.fetchall()
            for row in process_main:
                mainrowdict = {
                    'id': row[0],
                    'type': row[1]
                }
                input_full_list.append(mainrowdict)
            # input_software
            cur = mysql.connection.cursor()
            cur.execute("select sno, type from `software` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s",
                        (obj_id, objtype, createdBy))
            software_main = cur.fetchall()
            for row in software_main:
                mainrowdict = {
                    'id': row[0],
                    'type': row[1]
                }
                input_full_list.append(mainrowdict)
            # input_ url
            cur = mysql.connection.cursor()
            cur.execute("select sno, type from `url` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s",
                        (obj_id, objtype, createdBy))
            url_main = cur.fetchall()
            for row in url_main:
                mainrowdict = {
                    'id': row[0],
                    'type': row[1]
                }
                input_full_list.append(mainrowdict)
            # input_ useraccount
            cur = mysql.connection.cursor()
            cur.execute("select sno, type from `user-account` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s",
                        (obj_id, objtype, createdBy))
            useracc_main = cur.fetchall()
            for row in useracc_main:
                mainrowdict = {
                    'id': row[0],
                    'type': row[1]
                }
                input_full_list.append(mainrowdict)
            # input windows reg key
            cur = mysql.connection.cursor()
            cur.execute("select sno, type from `windows-registry-key` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s",
                        (obj_id, objtype, createdBy))
            winregkey_main = cur.fetchall()
            for row in winregkey_main:
                mainrowdict = {
                    'id': row[0],
                    'type': row[1]
                }
                input_full_list.append(mainrowdict)
            # input_x509
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type from `x509-certificate` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s",
                (obj_id, objtype, createdBy))
            x509_main = cur.fetchall()
            for row in x509_main:
                mainrowdict = {
                    'id': row[0],
                    'type': row[1]
                }
                input_full_list.append(mainrowdict)
            # final result set for input_refs
            output_inputrefs = json.dumps(input_full_list, sort_keys=True, indent=4)
            final_input_refs = json.loads(output_inputrefs)

            # output_refs for main object
            output_full_list = []
            # output_artifact
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type from `artifact` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            artifact_main = cur.fetchall()
            for row in artifact_main:
                mainrowdict = {
                    'id': row[0],
                    'type': row[1]
                }
                output_full_list.append(mainrowdict)

            # output_AS
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type from `autonomous-system` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            as_main = cur.fetchall()
            for row in as_main:
                mainrowdict = {
                    'id': row[0],
                    'type': row[1]
                }
                output_full_list.append(mainrowdict)
            # output_directory
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type from `directory` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            directory_main = cur.fetchall()
            for row in directory_main:
                mainrowdict = {
                    'id': row[0],
                    'type': row[1]
                }
                output_full_list.append(mainrowdict)
            # output_domainname
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type from `domain-name` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            domainname_main = cur.fetchall()
            for row in domainname_main:
                mainrowdict = {
                    'id': row[0],
                    'type': row[1]
                }
                output_full_list.append(mainrowdict)
            # output_emailaddr
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type from `email-addr` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            emailaddr_main = cur.fetchall()
            for row in emailaddr_main:
                mainrowdict = {
                    'id': row[0],
                    'type': row[1]
                }
                output_full_list.append(mainrowdict)
            # output_emailmsg
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type from `email-message` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            emailmsg_main = cur.fetchall()
            for row in emailmsg_main:
                mainrowdict = {
                    'id': row[0],
                    'type': row[1]
                }
                output_full_list.append(mainrowdict)
            # output_file
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type from `file` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            file_main = cur.fetchall()
            for row in file_main:
                mainrowdict = {
                    'id': row[0],
                    'type': row[1]
                }
                output_full_list.append(mainrowdict)
            # output_ipv4
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type from `ipv4-addr` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            ipv4_main = cur.fetchall()
            for row in ipv4_main:
                mainrowdict = {
                    'id': row[0],
                    'type': row[1]
                }
                output_full_list.append(mainrowdict)
            # output_ipv6
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type from `ipv6-addr` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            ipv4_main = cur.fetchall()
            for row in ipv4_main:
                mainrowdict = {
                    'id': row[0],
                    'type': row[1]
                }
                output_full_list.append(mainrowdict)
            # output_macaddr
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type from `mac-addr` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            macaddr_main = cur.fetchall()
            for row in macaddr_main:
                mainrowdict = {
                    'id': row[0],
                    'type': row[1]
                }
                output_full_list.append(mainrowdict)
            # output_networktraffic
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type from `network-traffic` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            networktraffic_main = cur.fetchall()
            for row in networktraffic_main:
                mainrowdict = {
                    'id': row[0],
                    'type': row[1]
                }
                output_full_list.append(mainrowdict)
            # output_ process
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type from `process` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            process_main = cur.fetchall()
            for row in process_main:
                mainrowdict = {
                    'id': row[0],
                    'type': row[1]
                }
                output_full_list.append(mainrowdict)
            # output_software
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type from `software` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            software_main = cur.fetchall()
            for row in software_main:
                mainrowdict = {
                    'id': row[0],
                    'type': row[1]
                }
                output_full_list.append(mainrowdict)
            # output_ url
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type from `url` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            url_main = cur.fetchall()
            for row in url_main:
                mainrowdict = {
                    'id': row[0],
                    'type': row[1]
                }
                output_full_list.append(mainrowdict)
            # output_ useraccount
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type from `user-account` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            useracc_main = cur.fetchall()
            for row in useracc_main:
                mainrowdict = {
                    'id': row[0],
                    'type': row[1]
                }
                output_full_list.append(mainrowdict)
            # output windows reg key
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type from `windows-registry-key` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            winregkey_main = cur.fetchall()
            for row in winregkey_main:
                mainrowdict = {
                    'id': row[0],
                    'type': row[1]
                }
                output_full_list.append(mainrowdict)
            # output_x509
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type from `x509-certificate` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            x509_main = cur.fetchall()
            for row in x509_main:
                mainrowdict = {
                    'id': row[0],
                    'type': row[1]
                }
                output_full_list.append(mainrowdict)
            # final result set for output_refs - main
            output_outputrefs = json.dumps(output_full_list, sort_keys=True, indent=4)
            final_output_refs = json.loads(output_outputrefs)
            # input ref's for directory
            # ------------------------
            artdir_input_list = []
            cur = mysql.connection.cursor()
            cur.execute("select sno, type, name from `file` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s", (obj_id,objtype, createdBy))
            artifact_input_results = cur.fetchall()
            for row in artifact_input_results:
                rowdict2={
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]
                }
                artdir_input_list.append(rowdict2)
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type, path from `directory` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s",
                (obj_id, objtype, createdBy))
            directory_input_results = cur.fetchall()
            for row in directory_input_results:
                rowdict2={
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]
                }
                artdir_input_list.append(rowdict2)
            output_dirinput = json.dumps(artdir_input_list, sort_keys=True, indent=4)
            artdir_input_response = json.loads(output_dirinput)
            # ---------------------------
            # output ref's for directory
            # --------------------------
            artdir_output_list = []
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type, name from `file` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            artifact_output_results = cur.fetchall()
            for row in artifact_output_results:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]
                }
                artdir_output_list.append(rowdict2)
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type, path from `directory` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            directory_output_results = cur.fetchall()
            for row in directory_output_results:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]
                }
                artdir_output_list.append(rowdict2)
            output_diroutput = json.dumps(artdir_output_list, sort_keys=True, indent=4)
            artdir_output_response = json.loads(output_diroutput)
            # input ref's for domain name
            domainrefs_input_list = []
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type, value from `ipv4-addr` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s",
                (obj_id, objtype, createdBy))
            ipv4_input_results = cur.fetchall()
            for row in ipv4_input_results:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]
                }
                domainrefs_input_list.append(rowdict2)
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type, value from `ipv6-addr` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s",
                (obj_id, objtype, createdBy))
            ipv6_input_results = cur.fetchall()
            for row in ipv6_input_results:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]
                }
                domainrefs_input_list.append(rowdict2)
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type, value from `domain-name` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s",
                (obj_id, objtype, createdBy))
            dn_input_results = cur.fetchall()
            for row in dn_input_results:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]
                }
                domainrefs_input_list.append(rowdict2)
            domain_input = json.dumps(domainrefs_input_list, sort_keys=True, indent=4)
            dn_input_response = json.loads(domain_input)
            # ------------------------------------------
            # output refs for domain name
            domainrefs_output_list = []
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type, value from `ipv4-addr` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            ipv4_output_results = cur.fetchall()
            for row in ipv4_output_results:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]
                }
                domainrefs_output_list.append(rowdict2)
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type, value from `ipv6-addr` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            ipv6_output_results = cur.fetchall()
            for row in ipv6_output_results:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]
                }
                domainrefs_output_list.append(rowdict2)
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type, value from `domain-name` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            dn_output_results = cur.fetchall()
            for row in dn_output_results:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]
                }
                domainrefs_output_list.append(rowdict2)
            domain_output = json.dumps(domainrefs_output_list, sort_keys=True, indent=4)
            dn_output_response = json.loads(domain_output)
            # ---------------------------------------------------------------------
            # input refs for email -addr
            emailaddrrefs_input_list = []
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type, account_login from `user-account` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s",
                (obj_id, objtype, createdBy))
            emaddr_input_results = cur.fetchall()
            for row in emaddr_input_results:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]
                }
                emailaddrrefs_input_list.append(rowdict2)
            output_inputemaddr = json.dumps(emailaddrrefs_input_list, sort_keys=True, indent=4)
            emaddr_input_response = json.loads(output_inputemaddr)
            # -----------------------------------------------------------------
            # output refs for email -addr
            emailaddrrefs_output_list = []
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type, account_login from `user-account` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            emaddr_output_results = cur.fetchall()
            for row in emaddr_output_results:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]
                }
                emailaddrrefs_output_list.append(rowdict2)
            output_outputemaddr = json.dumps(emailaddrrefs_output_list, sort_keys=True, indent=4)
            emaddr_output_response = json.loads(output_outputemaddr)
            # ------------------------------------------------------------------------------------------
            # input refs for email-message
            emailmsgrefs_input_list = []
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type, value from `email-addr` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s",
                (obj_id, objtype, createdBy))
            emmsg_input_results = cur.fetchall()
            for row in emmsg_input_results:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]
                }
                emailmsgrefs_input_list.append(rowdict2)
            emailmsgrefs_input_list2=[]
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type, mime_type from `artifact` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s",
                (obj_id, objtype, createdBy))
            emmsg_input_results = cur.fetchall()
            for row in emmsg_input_results:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]
                }
                emailmsgrefs_input_list2.append(rowdict2)
            output_inputemmsg = json.dumps(emailmsgrefs_input_list, sort_keys=True, indent=4)
            output_inputemmsg2 = json.dumps(emailmsgrefs_input_list2, sort_keys=True, indent=4)
            emmsg_input_response = json.loads(output_inputemmsg)
            emmsg_input_response2 = json.loads(output_inputemmsg2)
            # ---------------------------------------------------------------------------------------------
            # output refs for email-message
            emailmsgrefs_output_list = []
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type, value from `email-addr` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            emmsg_output_results = cur.fetchall()
            for row in emmsg_output_results:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]
                }
                emailmsgrefs_output_list.append(rowdict2)
            emailmsgrefs_output_list2 = []
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type, mime_type from `artifact` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            emmsg_output_results = cur.fetchall()
            for row in emmsg_output_results:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]
                }
                emailmsgrefs_output_list2.append(rowdict2)
            output_outputemmsg = json.dumps(emailmsgrefs_output_list, sort_keys=True, indent=4)
            output_outputemmsg2 = json.dumps(emailmsgrefs_output_list2, sort_keys=True, indent=4)
            emmsg_output_response = json.loads(output_outputemmsg)
            emmsg_output_response2 = json.loads(output_outputemmsg2)
            # ---------------------------------------------------------------------------------------------
            # input refs for file
            dir_input_list=[]
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type, path from `directory` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s",
                (obj_id, objtype, createdBy))
            directory_input_results = cur.fetchall()
            for row in directory_input_results:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]
                }
                dir_input_list.append(rowdict2)
            output_dirinput = json.dumps(dir_input_list, sort_keys=True, indent=4)
            dir_input_response = json.loads(output_dirinput)
            # ---------------------------------------------------------------------------------------------
            # output refs for file
            dir_output_list = []
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type, path from `directory` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            directory_output_results = cur.fetchall()
            for row in directory_output_results:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]
                }
                dir_output_list.append(rowdict2)
            output_diroutput = json.dumps(dir_output_list, sort_keys=True, indent=4)
            dir_output_response = json.loads(output_diroutput)
            # ---------------------------------------------------------------------------------------------
            # input refs for ipv4-addr
            ip_input_list = []
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type, value from `mac-addr` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s",
                (obj_id, objtype, createdBy))
            ip_input_results = cur.fetchall()
            for row in ip_input_results:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]
                }
                ip_input_list.append(rowdict2)
            output_ipinput = json.dumps(ip_input_list, sort_keys=True, indent=4)
            ip_input_response = json.loads(output_ipinput)

            ip_input_list2 = []
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type, name from `autonomous-system` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s",
                (obj_id, objtype, createdBy))
            ip_input_results2 = cur.fetchall()
            for row in ip_input_results2:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]
                }
                ip_input_list2.append(rowdict2)
            output_ipinput2 = json.dumps(ip_input_list2, sort_keys=True, indent=4)
            ip_input_response2 = json.loads(output_ipinput2)
            # ---------------------------------------------------------------------------------------------
            # output refs for ipv4-addr
            ip_output_list = []
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type, value from `mac-addr` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            ip_output_results = cur.fetchall()
            for row in ip_output_results:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]
                }
                ip_output_list.append(rowdict2)
            output_ipoutput = json.dumps(ip_output_list, sort_keys=True, indent=4)
            ip_output_response = json.loads(output_ipoutput)

            ip_output_list2 = []
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type, name from `autonomous-system` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            ip_output_results2 = cur.fetchall()
            for row in ip_output_results2:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]
                }
                ip_output_list2.append(rowdict2)
            output_ipoutput2 = json.dumps(ip_output_list2, sort_keys=True, indent=4)
            ip_output_response2 = json.loads(output_ipoutput2)
            # ---------------------------------------------------------------------------------------------
            # input refs for network-traffic
            src_input_list = []
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type, value from `ipv4-addr` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s",
                (obj_id, objtype, createdBy))
            srcref_ipv4_results = cur.fetchall()
            for row in srcref_ipv4_results:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]
                }
                src_input_list.append(rowdict2)
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type, value from `ipv6-addr` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s",
                (obj_id, objtype, createdBy))
            srcref_ipv6_results = cur.fetchall()
            for row in srcref_ipv6_results:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]
                }
                src_input_list.append(rowdict2)
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type, value from `mac-addr` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s",
                (obj_id, objtype, createdBy))
            srcref_mac_results = cur.fetchall()
            for row in srcref_mac_results:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]
                }
                src_input_list.append(rowdict2)
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type, value from `domain-name` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s",
                (obj_id, objtype, createdBy))
            srcref_dn_results = cur.fetchall()
            for row in srcref_dn_results:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]
                }
                src_input_list.append(rowdict2)
            output_srcref = json.dumps(src_input_list, sort_keys=True, indent=4)
            srcrefin_output_response = json.loads(output_srcref)

            art_input_list = []
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type, mime_type from `artifact` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s",
                (obj_id, objtype, createdBy))
            srcref_ar_results = cur.fetchall()
            for row in srcref_ar_results:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]
                }
                art_input_list.append(rowdict2)
            output_srcref = json.dumps(art_input_list, sort_keys=True, indent=4)
            artin_output_response = json.loads(output_srcref)

            nettraffic_input_list = []
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type from `network-traffic` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s",
                (obj_id, objtype, createdBy))
            srcref_nt_results = cur.fetchall()
            for row in srcref_nt_results:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1]

                }
                nettraffic_input_list.append(rowdict2)
            output_srcref = json.dumps(nettraffic_input_list, sort_keys=True, indent=4)
            nettrafficin_output_response = json.loads(output_srcref)
            # ---------------------------------------------------------------------------------------------
            # output refs for network-traffic
            src_output_list = []
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type, value from `ipv4-addr` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            srcref_ipv4_results = cur.fetchall()
            for row in srcref_ipv4_results:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]
                }
                src_output_list.append(rowdict2)
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type, value from `ipv6-addr` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            srcref_ipv6_results = cur.fetchall()
            for row in srcref_ipv6_results:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]
                }
                src_output_list.append(rowdict2)
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type, value from `mac-addr` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            srcref_mac_results = cur.fetchall()
            for row in srcref_mac_results:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]
                }
                src_output_list.append(rowdict2)
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type, value from `domain-name` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            srcref_dn_results = cur.fetchall()
            for row in srcref_dn_results:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]
                }
                src_output_list.append(rowdict2)
            output_srcref = json.dumps(src_output_list, sort_keys=True, indent=4)
            srcrefout_output_response = json.loads(output_srcref)

            art_output_list = []
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type, mime_type from `artifact` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            srcref_ar_results = cur.fetchall()
            for row in srcref_ar_results:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]
                }
                art_output_list.append(rowdict2)
            output_srcref = json.dumps(art_output_list, sort_keys=True, indent=4)
            artout_output_response = json.loads(output_srcref)

            nettraffic_output_list = []
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type from `network-traffic` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            srcref_nt_results = cur.fetchall()
            for row in srcref_nt_results:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1]

                }
                nettraffic_output_list.append(rowdict2)
            output_srcref = json.dumps(nettraffic_output_list, sort_keys=True, indent=4)
            nettrafficout_output_response = json.loads(output_srcref)
            # ---------------------------------------------------------------------------------------------
            # input refs for process
            file_input_list = []
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type, name from `file` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s",
                (obj_id, objtype, createdBy))
            ref_file_results = cur.fetchall()
            for row in ref_file_results:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]

                }
                file_input_list.append(rowdict2)
            output_srcref = json.dumps(file_input_list, sort_keys=True, indent=4)
            filein_output_response = json.loads(output_srcref)

            process_input_list = []
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type, name from `process` where obj_id=%s AND obj_type=%s AND ref_type='input' and created_by=%s",
                (obj_id, objtype, createdBy))
            ref_process_results = cur.fetchall()
            for row in ref_process_results:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]

                }
                process_input_list.append(rowdict2)
            output_srcref = json.dumps(process_input_list, sort_keys=True, indent=4)
            processin_output_response = json.loads(output_srcref)
            # ---------------------------------------------------------------------------------------------
            # output refs for process
            file_output_list = []
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type, name from `file` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            ref_file_results = cur.fetchall()
            for row in ref_file_results:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]

                }
                file_output_list.append(rowdict2)
            output_srcref = json.dumps(file_output_list, sort_keys=True, indent=4)
            fileout_output_response = json.loads(output_srcref)

            process_output_list = []
            cur = mysql.connection.cursor()
            cur.execute(
                "select sno, type, name from `process` where obj_id=%s AND obj_type=%s AND ref_type='output' and created_by=%s",
                (obj_id, objtype, createdBy))
            ref_process_results = cur.fetchall()
            for row in ref_process_results:
                rowdict2 = {
                    'id': row[0],
                    'type': row[1],
                    'ref': row[2]

                }
                process_output_list.append(rowdict2)
            output_srcref = json.dumps(process_output_list, sort_keys=True, indent=4)
            processout_output_response = json.loads(output_srcref)
            return render_template(url, data=resp, inputrefs=final_input_refs, outputrefs=final_output_refs,
                                   dirinputdata=artdir_input_response, diroutputdata=artdir_output_response,
                                   domainname_inputrefs=dn_input_response, domainname_outputrefs=dn_output_response,
                                   emaddr_inputrefs=emaddr_input_response, emaddr_outputrefs=emaddr_output_response,
                                   emmsg_inputrefs=emmsg_input_response, emmsg_inputrefs2=emmsg_input_response2,
                                   emmsg_outputrefs=emmsg_output_response, emmsg_outputrefs2=emmsg_output_response2,
                                   file_inputrefs=emmsg_input_response2,file_outputrefs=emmsg_output_response2,
                                   file_input_dirrefs=dir_input_response,file_output_dirrefs=dir_output_response,
                                   ip_input_macrefs=ip_input_response, ip_input_asrefs=ip_input_response2,
                                   ip_output_macrefs=ip_output_response, ip_output_asrefs=ip_output_response2,
                                   nt_input_refs=srcrefin_output_response, nt_output_refs=srcrefout_output_response,
                                   art_input_refs=artin_output_response, art_output_refs=artout_output_response,
                                   nettraffic_input_refs=nettrafficin_output_response, nettraffic_output_refs=nettrafficout_output_response,
                                   file_input_refs=filein_output_response, file_output_refs=fileout_output_response,
                                   process_input_refs=processin_output_response, process_output_refs=processout_output_response)
        elif objtype == "malware-family":
            url = 'update_templates/' + objtype + '.html'
            obj_id = id
            createdBy = g.user
            cur = mysql.connection.cursor()
            cur.execute("select * from `" + objtype + "` where sno=%s and created_by=%s", (obj_id, createdBy))
            row = cur.fetchone()
            rowdict = {
                'id': row[0],
                'type': row[1],
                'labels': row[2],
                'description': row[3],
                'common_strings': row[4],
                'common_capabilities': row[5],
                'common_coderefs': row[6],
                'common_behaviorrefs': row[7],
                'references': row[8]
            }

            output = json.dumps(rowdict, sort_keys=True, indent=4)
            resp = json.loads(output)
            # for Name
            cur = mysql.connection.cursor()
            cur.execute("select * from `external_references` where obj_id=%s and obj_type=%s and created_by=%s", (obj_id, objtype, createdBy))
            row_extref = cur.fetchall()
            extreflist =[]
            for row in row_extref:
                mainrowdict = {
                    'id': row[0],
                    'name': row[3]
                }
                extreflist.append(mainrowdict)
            extref_output = json.dumps(extreflist, sort_keys=True, indent = 4)
            extref_response = json.loads(extref_output)
            # for  display of Aliases
            cur = mysql.connection.cursor()
            cur.execute("select * from `aliases` where obj_id=%s and obj_type=%s and created_by=%s",
                        (obj_id, objtype, createdBy))
            row_aliases = cur.fetchall()
            aliaseslist = []
            for row in row_aliases:
                mainrowdict = {
                    'id': row[0],
                    'value': row[3],
                    'source': row[4]
                }
                aliaseslist.append(mainrowdict)
            aliases_output = json.dumps(aliaseslist, sort_keys=True, indent=4)
            aliases_response = json.loads(aliases_output)
            # for display of Name associated with malware family
            cur = mysql.connection.cursor()
            cur.execute("select * from `name` where obj_id=%s and obj_type=%s and created_by=%s",
                        (obj_id, objtype, createdBy))
            row_name = cur.fetchone()
            mainrowdict = {
                'id': row_name[0],
                'value': row_name[3],
                'source': row_name[4]
            }
            names_output = json.dumps(mainrowdict, sort_keys=True, indent=4)
            name_response = json.loads(names_output)
            # for capability- behavior references
            cur = mysql.connection.cursor()
            cur.execute("select * from `behavior` where created_by=%s",
                        (createdBy,))
            row_behrefs = cur.fetchall()
            behaverefslist = []
            for row in row_behrefs:
                mainrowdict = {
                    'id': row[0],
                    'name': row[2]

                }
                behaverefslist.append(mainrowdict)
            behavrefs_output = json.dumps(behaverefslist, sort_keys=True, indent=4)
            behavrefs_response = json.loads(behavrefs_output)
            # for capability - refined capabilities
            cur = mysql.connection.cursor()
            cur.execute("select * from `refined_capability` where obj_id=%s AND obj_type=%s AND created_by=%s",
                        (obj_id, objtype, createdBy))
            row_refcapability = cur.fetchall()
            refcapabilitylist = []
            for row in row_refcapability:
                mainrowdict = {
                    'id': row[0],
                    'name': row[2]

                }
                refcapabilitylist.append(mainrowdict)
            refcapability_output = json.dumps(refcapabilitylist, sort_keys=True, indent=4)
            refcapability_response = json.loads(refcapability_output)
            # for main object - common code refs(artifact)
            cur = mysql.connection.cursor()
            cur.execute("select * from `artifact` where obj_id=%s AND obj_type=%s AND created_by=%s",
                        (obj_id, objtype, createdBy))
            row_artifact = cur.fetchall()
            refartifactlist = []
            for row in row_artifact:
                mainrowdict = {
                    'id': row[0],
                    'name': row[5]
                }
                refartifactlist.append(mainrowdict)
            refartifact_output = json.dumps(refartifactlist, sort_keys=True, indent=4)
            refartifact_response = json.loads(refartifact_output)
            return render_template(url, data=resp, extrefdata=extref_response, aliasesdata=aliases_response, namedata=name_response,
                                   behavrefsdata=behavrefs_response, refcapabilitydata=refcapability_response,
                                   refartifactdata=refartifact_response)

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
                cur.execute("Delete from kill_chain_phase where obj_id=%s and obj_type = %s and created_by=%s",
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
                cur.execute("Delete from kill_chain_phase where obj_id=%s and obj_type = %s and created_by=%s",
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
                cur.execute("Delete from kill_chain_phase where obj_id=%s and obj_type = %s and created_by=%s",
                            (id, obj_type, createdBy))
                mysql.connection.commit()
                print "Entries deleted successfully"
                return redirect(url_for('home'))
            elif obj_type == 'report':
                # deleting main SDO
                cur = mysql.connection.cursor()
                cur.execute("Delete from `" + obj_type + "` where sno=%s and created_by=%s", (id, createdBy))
                mysql.connection.commit()
                print "Entries deleted successfully"
                return redirect(url_for('home'))
            elif obj_type == 'threat-actor':
                # deleting main SDO
                cur = mysql.connection.cursor()
                cur.execute("Delete from `" + obj_type + "` where sno=%s and created_by=%s", (id, createdBy))
                mysql.connection.commit()
                print "Entry deleted successfully"
                return redirect(url_for('home'))
            elif obj_type == 'tool':
                # deleting main SDO
                cur = mysql.connection.cursor()
                cur.execute("Delete from `" + obj_type + "` where sno=%s and created_by=%s", (id, createdBy))
                mysql.connection.commit()
                # deleting entries from child table: kill chain phase
                cur = mysql.connection.cursor()
                cur.execute("Delete from kill_chain_phase where obj_id=%s and obj_type = %s and created_by=%s",
                            (id, obj_type, createdBy))
                mysql.connection.commit()
                print "Entries deleted successfully"
                return redirect(url_for('home'))
            elif obj_type == 'vulnerability':
                # deleting main SDO
                cur = mysql.connection.cursor()
                cur.execute("Delete from `" + obj_type + "` where sno=%s and created_by=%s", (id, createdBy))
                mysql.connection.commit()
                # deleting entries from child table: External references
                cur = mysql.connection.cursor()
                cur.execute("Delete from external_references where obj_id=%s and obj_type = %s and created_by=%s",
                            (id, obj_type, createdBy))
                mysql.connection.commit()
                print "Entries deleted successfully"
                return redirect(url_for('home'))
            elif obj_type == 'behavior':
                # deleting main SDO
                cur = mysql.connection.cursor()
                cur.execute("Delete from `" + obj_type + "` where sno=%s and created_by=%s", (id, createdBy))
                mysql.connection.commit()
                # deleting entries from child table: External references
                cur = mysql.connection.cursor()
                cur.execute("Delete from external_references where obj_id=%s and obj_type = %s and created_by=%s",
                            (id, obj_type, createdBy))
                mysql.connection.commit()
                print "Entries deleted successfully"
                return redirect(url_for('home'))
            elif obj_type == 'collection':
                # deleting main SDO
                cur = mysql.connection.cursor()
                cur.execute("Delete from `" + obj_type + "` where sno=%s and created_by=%s", (id, createdBy))
                mysql.connection.commit()
                print "Entries deleted successfully"
                return redirect(url_for('home'))
            elif obj_type == 'malware-action':
                # deleting main SDO
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

# Generally used routes for child tables and their respective operation

# Name - Insert (Ajax post query)
@app.route('/insertname', methods=['POST'])
def insert_name():
    if g.user:
        if request.method == 'POST':
            value = request.form['name_value']
            source = request.form['source']
            confidence = request.form['confidence']
            ref_id = request.form['obj_id']
            ref_type = request.form['obj_type']
            created_by = request.form['created_by']
            cur = mysql.connection.cursor()
            cur.execute('''INSERT INTO name (obj_id, obj_type, value, source, confidence, created_by)
                        values (%s , %s, %s, %s, %s, %s)''',(ref_id, ref_type, value, source, confidence, created_by))
            mysql.connection.commit()
            print('Successfully entered Name')
            return jsonify({'result': 'success'})


# Name- update(ajax post query)
@app.route('/updatename',methods=['POST'])
def update_name():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            value = request.json['name_val']
            confidence = request.json['confidence']
            cur = mysql.connection.cursor()
            cur.execute("UPDATE name SET value=%s, confidence=%s where sno=%s ",(kc_name,phase_name,id))
            mysql.connection.commit()
            print "Successfully update kill chain data"
            return jsonify({'result': 'success'})


# Name - delete(ajax post query)
@app.route('/deletename', methods=['POST'])
def delete_name():
    id = request.json['id']
    query = "delete from name where sno=%s"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()
    print "successfully deleted"
    return jsonify({'result': 'success'})

# Aliases - Insert (Ajax post query)
@app.route('/insertaliases', methods=['POST'])
def insert_aliases():
    if g.user:
        if request.method == 'POST':

            ref_id = request.form['obj_id']
            ref_type = request.form['obj_type']
            value = request.form['name_value']
            source = request.form['source']
            confidence = request.form['confidence']
            created_by = request.form['created_by']
            cur = mysql.connection.cursor()
            cur.execute('''INSERT INTO aliases (obj_id, obj_type, value, source, confidence, created_by)
                        values (%s , %s, %s, %s, %s, %s)''',(ref_id, ref_type, value, source, confidence, created_by))
            mysql.connection.commit()
            print('Successfully entered Aliases')
            return jsonify({'result': 'success'})


# Aliases- update(ajax post query) - to be updated
@app.route('/updatealiases',methods=['POST'])
def update_aliases():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            aliases = request.json['aliases']
            cur = mysql.connection.cursor()
            cur.execute("UPDATE aliases SET aliases=%s where sno=%s ",(aliases,id))
            mysql.connection.commit()
            print "Successfully updated aliases"
            return jsonify({'result': 'success'})


# Aliases - delete(ajax post query)
@app.route('/deletealiases', methods=['POST'])
def delete_aliases():
    id = request.json['id']
    query = "delete from aliases where sno=%s"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()
    print "successfully deleted"
    return jsonify({'result': 'success'})

# Field data - Insert (Ajax post query)
@app.route('/insertfielddata', methods=['POST'])
def insert_fielddata():
    if g.user:
        if request.method == 'POST':
            delivery_vectors = request.form['delivery_vectors']
            first_seen = request.form['first_seen']
            last_seen = request.form['last_seen']
            ref_id = request.form['obj_id']
            ref_type = request.form['obj_type']
            created_by = request.form['created_by']
            cur = mysql.connection.cursor()
            cur.execute('''INSERT INTO `field-data` (obj_id, obj_type, delivery_vectors, first_seen, last_seen, created_by)
                        values (%s , %s, %s, %s, %s, %s)''',(ref_id, ref_type, delivery_vectors, first_seen, last_seen, created_by))
            mysql.connection.commit()
            print('Successfully entered field data')
            return jsonify({'result': 'success'})


# Field data- update(ajax post query)
@app.route('/updatefielddata',methods=['POST'])
def update_fielddata():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            delivery_vectors = request.json['delivery_vectors']

            cur = mysql.connection.cursor()
            cur.execute("UPDATE `field-data` SET delivery_vectors=%s where sno=%s ",(aliases,id))
            mysql.connection.commit()
            print "Successfully updated aliases"
            return jsonify({'result': 'success'})


# Field data - delete(ajax post query)
@app.route('/deletefielddata', methods=['POST'])
def delete_fielddata():
    id = request.json['id']
    query = "delete from `field-data` where sno=%s"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()
    print "successfully deleted"
    return jsonify({'result': 'success'})

# Refined capability - Insert (Ajax post query)
@app.route('/insertrefinedcapability', methods=['POST'])
def insert_refinedcapability():
    if g.user:
        if request.method == 'POST':
            name = request.form['nm']
            description = request.form['desc']
            attrb_dict = request.form['attrb_dictionary']
            behavior_refs = request.form['behavior_refs']
            references = request.form['references']
            ref_id = request.form['obj_id']
            ref_type = request.form['obj_type']
            created_by = request.form['created_by']
            cur = mysql.connection.cursor()
            cur.execute('''INSERT INTO `refined_capability` (obj_id, obj_type, name, description, attributes, behavior_refs, `references`, created_by)
                        values (%s , %s, %s, %s, %s, %s, %s, %s)''',(ref_id, ref_type, name, description, attrb_dict, behavior_refs, references,  created_by))
            mysql.connection.commit()
            print('Successfully entered refined capability')
            return jsonify({'result': 'success'})


# Refined capability- update(ajax post query)
@app.route('/updaterefinedcapability',methods=['POST'])   # to be update
def update_refinedcapability():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            delivery_vectors = request.json['delivery_vectors']

            cur = mysql.connection.cursor()
            cur.execute("UPDATE `refined_capability` SET delivery_vectors=%s where sno=%s ",(aliases,id))
            mysql.connection.commit()
            print "Successfully updated aliases"
            return jsonify({'result': 'success'})


# Refined capability - delete(ajax post query)
@app.route('/deleterefinedcapability', methods=['POST'])
def delete_refinedcapability():
    id = request.json['id']
    query = "delete from `refined_capability` where sno=%s"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()
    print "successfully deleted"
    return jsonify({'result': 'success'})

#  capability - Insert (Ajax post query)
@app.route('/insertcapability', methods=['POST'])
def insert_capability():
    if g.user:
        if request.method == 'POST':
            name = request.form['nm']
            refined_capability = request.form['ref_capabilities']
            description = request.form['desc']
            attrb_dict = request.form['attrb_dict']
            behavior_refs = request.form['behavior_refs']
            references = request.form['references']
            ref_id = request.form['obj_id']
            ref_type = request.form['obj_type']
            created_by = request.form['created_by']
            cur = mysql.connection.cursor()
            cur.execute('''INSERT INTO capability (obj_id, obj_type, name, refined_capabilities, description, attributes, behavior_refs, `references`, created_by)
                        values (%s , %s, %s, %s, %s, %s, %s, %s, %s)''',(ref_id, ref_type, name, refined_capability, description, attrb_dict, behavior_refs, references,  created_by))
            mysql.connection.commit()
            print('Successfully entered refined capability')
            return jsonify({'result': 'success'})


#  capability- update(ajax post query)
@app.route('/updatecapability',methods=['POST'])   # to be update
def update_capability():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            delivery_vectors = request.json['delivery_vectors']

            cur = mysql.connection.cursor()
            cur.execute("UPDATE `capability` SET delivery_vectors=%s where sno=%s ",(aliases,id))
            mysql.connection.commit()
            print "Successfully updated aliases"
            return jsonify({'result': 'success'})


#  capability - delete(ajax post query)
@app.route('/deletecapability', methods=['POST'])
def delete_capability():
    id = request.json['id']
    query = "delete from `capability` where sno=%s"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()
    print "successfully deleted"
    return jsonify({'result': 'success'})

# kill chain - Insert (Ajax post query)
@app.route('/killchain', methods=['POST'])
def kill_chain_submit():
    if g.user:
        if request.method == 'POST':
            kc_name=request.form['kcName']
            ph_name = request.form['phase_name']
            ref_id = request.form['obj_id']
            ref_type = request.form['obj_type']
            created_by = request.form['created_by']
            cur = mysql.connection.cursor()
            cur.execute('''INSERT INTO kill_chain_phase (obj_id, obj_type, killchain_name, phase_name, created_by)
                        values (%s , %s, %s, %s, %s)''',(ref_id, ref_type, kc_name, ph_name, created_by))
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
            cur.execute("UPDATE kill_chain_phase SET killchain_name=%s, phase_name=%s where sno=%s ",(kc_name,phase_name,id))
            mysql.connection.commit()
            print "Successfully update kill chain data"
            return jsonify({'result': 'success'})


# kill chain - delete(ajax post query)
@app.route('/deletekillchaindata', methods=['POST'])
def delete_killchaindata():
    id = request.json['id']
    query = "delete from kill_chain_phase where sno=%s"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()
    print "successfully deleted"
    return jsonify({'result': 'success'})


# External References - Insert (Ajax post query)
@app.route('/insertextref', methods=['POST'])
def insert_extref():
    if g.user:
        if request.method == 'POST':
            src_name = request.form['extref_srcname']
            ref_id = request.form['ref_id']
            ref_type = request.form['ref_type']
            description = request.form['extref_desc']
            ext_url = request.form['extref_url']
            hash_type = request.form['hash_type']
            hash_val = request.form['hash_value']
            ext_id = request.form['extref_extid']
            created_by = request.form['created_by']

            cur = mysql.connection.cursor()
            cur.execute('''INSERT INTO external_references (obj_id, obj_type, src_name, description, url, hash_type,
                        hash_value, external_id, created_by) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                        (ref_id, ref_type, src_name, description, ext_url, hash_type, hash_val, ext_id, created_by))
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
            cur.execute(query, (src_name, description, ext_id, id))
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


# API call - Insert (Ajax post query)
@app.route('/insert_apicall', methods=['POST'])
def insert_apicall():
    if g.user:
        if request.method == 'POST':
            ref_id = request.form['ref_id']
            ref_type = request.form['obj_type']
            address = request.form['address']
            return_value = request.form['return_val']
            parameters = request.form['parameters']
            function_name = request.form['func_name']
            created_by = g.user
            cur = mysql.connection.cursor()
            query = '''INSERT INTO `api-call` (obj_id, obj_type, address, return_value, parameters, function_name, created_by)
                             values (%s, %s, %s, %s, %s, %s, %s)'''
            cur.execute(query, (ref_id, ref_type, address, return_value, parameters, function_name, created_by))
            mysql.connection.commit()
            print('Successfully entered API call !!')
            return jsonify({'result': 'success'})


# API call - Update (Ajax post query)
@app.route('/update_apicall', methods=['POST'])
def update_apicall():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            address = request.json['api_address']
            return_value = request.json['api_retval']

            function_name = request.json['api_funcname']
            query = "UPDATE `api-call` SET address=%s, return_value=%s, function_name=%s where sno=%s"
            cur = mysql.connection.cursor()
            cur.execute(query, (address, return_value, function_name, id))
            mysql.connection.commit()
            print "successfully Updated"
            return jsonify({'result': 'success'})


# API call - delete (Ajax post query)
@app.route('/delete_apicall', methods=['POST'])
def delete_apicall():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            query = "delete from `api-call` where sno=%s"
            cur = mysql.connection.cursor()
            cur.execute(query, (id,))
            mysql.connection.commit()
            print "successfully deleted"
            return jsonify({'result': 'success'})


# Artifact - Insert (Ajax post query)
@app.route('/insert_artifact', methods=['POST'])
def insert_artifact():
    if g.user:
        if request.method == 'POST':
            obj_id = request.form['obj_id']
            obj_type = request.form['obj_type']
            ref_type = request.form['ref_type']
            type = request.form['type']
            mime_type = request.form['mime_type']
            payload_bin = request.form['payload_bin']
            url = request.form['url']
            hash_type = request.form['hash_type']
            hash_value = request.form['hash_value']
            created_by = g.user
            cur = mysql.connection.cursor()
            query = '''INSERT INTO `artifact` (obj_id, obj_type, ref_type, type, mime_type, payload_bin, url, hash_type, hash_value, created_by)
                             values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            cur.execute(query, (obj_id, obj_type, ref_type, type, mime_type, payload_bin, url, hash_type, hash_value, created_by))
            mysql.connection.commit()
            print('successfully inserted')
            return jsonify({'result': 'success'})

# Artifact - update (Ajax post query)
@app.route('/update_artifact', methods=['POST'])
def update_artifact():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            ref_type = request.json['referred_as']
            name = request.json['nm']
            description = request.json['desc']
            timestamp = request.json['timestamp']
            query = "UPDATE `artifact` SET mime_type=%s, url=%s where sno=%s AND ref_type=%s"
            cur = mysql.connection.cursor()
            cur.execute(query, (name, description, id, ref_type))
            mysql.connection.commit()
            print "successfully Updated"
            return jsonify({'result': 'success'})

# Artifact - Delete (Ajax post query)
@app.route('/delete_artifact', methods=['POST'])
def delete_artifact():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            ref_type = request.json['ref_type']
            query = "delete from `artifact` where sno=%s AND ref_type=%s"
            cur = mysql.connection.cursor()
            cur.execute(query, (id, ref_type))
            mysql.connection.commit()
            print "successfully deleted"
            return jsonify({'result': 'success'})


# Autonomous system - Insert ( Ajax post query)
@app.route('/insert_autonomoussystem', methods=['POST'])
def insert_autonomoussystem():
    if g.user:
        if request.method == 'POST':
            obj_id = request.form['obj_id']
            obj_type = request.form['obj_type']
            ref_type = request.form['ref_type']
            type = request.form['type']
            number = request.form['number']
            name = request.form['name']
            rir = request.form['rir']
            created_by = g.user
            cur = mysql.connection.cursor()
            query = '''INSERT INTO `autonomous-system` (obj_id, obj_type, ref_type, type, number, name, rir, created_by)
                             values (%s, %s, %s, %s, %s, %s, %s, %s)'''
            cur.execute(query, (obj_id, obj_type, ref_type, type, number, name, rir, created_by))
            mysql.connection.commit()
            print('successfully inserted')
            return jsonify({'result': 'success'})


# Autonomous system - Update ( Ajax post query)
@app.route('/update_autonomoussystem', methods=['POST'])
def update_autonomoussystem():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            ref_type = request.json['ref_type']
            # type = request.json['type']
            name = request.json['nm']
            number = request.json['number']
            rir = request.json['rir']
            query = "UPDATE `autonomous-system` SET name=%s, number=%s, rir=%s where sno=%s AND ref_type=%s"
            cur = mysql.connection.cursor()
            cur.execute(query, (name, number, rir, id, ref_type))
            mysql.connection.commit()
            print "successfully Updated"
            return jsonify({'result': 'success'})


# Autonomous system - Delete ( Ajax post query)
@app.route('/delete_autonomoussystem', methods=['POST'])
def delete_autonomoussystem():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            ref_type = request.json['ref_type']
            query = "delete from `autonomous-system` where sno=%s AND ref_type=%s"
            cur = mysql.connection.cursor()
            cur.execute(query, (id, ref_type))
            mysql.connection.commit()
            print "successfully deleted"
            return jsonify({'result': 'success'})


# Directory - Insert ( Ajax post query)
@app.route('/insert_directory', methods=['POST'])
def insert_directory():
    if g.user:
        if request.method == 'POST':
            obj_id = request.form['obj_id']
            obj_type = request.form['obj_type']
            ref_type = request.form['ref_type']
            type = request.form['type']
            path = request.form['path']
            path_enc = request.form['path_enc']
            created = request.form['created']
            modified = request.form['modified']
            accessed = request.form['accessed']
            contains_refs = request.form['contains_refs']
            created_by = g.user
            cur = mysql.connection.cursor()
            query = '''INSERT INTO `directory` (obj_id, obj_type, ref_type, type, path, path_enc, created, modified, accessed, contains_refs,  created_by)
                             values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            cur.execute(query, (obj_id, obj_type, ref_type, type, path, path_enc, created, modified, accessed, contains_refs, created_by))
            mysql.connection.commit()
            print('successfully inserted')
            return jsonify({'result': 'success'})


# Directory - Update ( Ajax post query)
@app.route('/update_directory', methods=['POST'])
def update_directory():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            ref_type = request.json['ref_type']
            # type = request.json['type']
            path = request.json['path']
            path_enc = request.json['path_enc']
            created = request.json['created']
            modified = request.json['modified']
            accessed = request.json['accessed']
            cur = mysql.connection.cursor()
            query = "UPDATE `directory` SET path=%s, path_enc=%s, created=%s, modified=%s, accessed=%s where sno=%s AND ref_type=%s"
            cur.execute(query, (path, path_enc, created, modified, accessed, id, ref_type))
            mysql.connection.commit()
            print('successfully inserted')
            return jsonify({'result': 'success'})


# Directory - Delete ( Ajax post query)
@app.route('/delete_directory', methods=['POST'])
def delete_directory():
    if g.user():
        if request.method == 'POST':
            id = request.json['id']
            ref_type = request.json['ref_type']
            query = "delete from `directory` where sno=%s AND ref_type=%s"
            cur = mysql.connection.cursor()
            cur.execute(query, (id, ref_type))
            mysql.connection.commit()
            print "successfully deleted"
            return jsonify({'result': 'success'})


# Domain name - Insert ( Ajax post query)
@app.route('/insert_domainname', methods=['POST'])
def insert_domainname():
    if g.user:
        if request.method == 'POST':
            obj_id = request.form['obj_id']
            obj_type = request.form['obj_type']
            ref_type = request.form['ref_type']
            type = request.form['type']
            value = request.form['value']
            resolves_to_refs = request.form['resolves_to_refs']
            created_by = g.user
            cur = mysql.connection.cursor()
            query = '''INSERT INTO `domain-name` (obj_id, obj_type, ref_type, type, value, resolves_to_refs,  created_by)
                             values (%s, %s, %s, %s, %s, %s, %s)'''
            cur.execute(query, (obj_id, obj_type, ref_type, type, value, resolves_to_refs, created_by))
            mysql.connection.commit()
            print('successfully inserted')
            return jsonify({'result': 'success'})


# Domain name - Update ( Ajax post query)
@app.route('/update_domainname', methods=['POST'])
def update_domainname():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            ref_type = request.json['ref_type']
            # type = request.json['type']
            value = request.json['value']
            resolves_to_refs = request.json['resolves_to_refs']
            cur = mysql.connection.cursor()
            query = " UPDATE `domain-name` SET value=%s, resolves_to_refs=%s where sno=%s and ref_type=%s"
            cur.execute(query, (value, resolves_to_refs, id, ref_type))
            mysql.connection.commit()
            print('successfully inserted')
            return jsonify({'result': 'success'})

# Domain name - Delete ( Ajax post query)
@app.route('/delete_domainname', methods=['POST'])
def delete_domainname():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            ref_type = request.json['ref_type']
            query = "delete from `domain-name` where sno=%s AND ref_type=%s"
            cur = mysql.connection.cursor()
            cur.execute(query, (id, ref_type))
            mysql.connection.commit()
            print "successfully deleted"
            return jsonify({'result': 'success'})

# email addr  - Insert ( Ajax post query)
@app.route('/insert_emailaddr', methods=['POST'])
def insert_emailaddr():
    if g.user:
        if request.method == 'POST':
            obj_id = request.form['obj_id']
            obj_type = request.form['obj_type']
            ref_type = request.form['ref_type']
            type = request.form['type']
            value = request.form['value']
            display_name = request.form['display_name']
            belongs_to_ref = request.form['belongs_to_ref']
            created_by = g.user
            cur = mysql.connection.cursor()
            query = '''INSERT INTO `email-addr` (obj_id, obj_type, ref_type, type, value, display_name, belongs_to_ref,  created_by)
                             values (%s, %s, %s, %s, %s, %s, %s, %s)'''
            cur.execute(query, (obj_id, obj_type, ref_type, type, value, display_name, belongs_to_ref, created_by))
            mysql.connection.commit()
            print('successfully inserted')
            return jsonify({'result': 'success'})


# email addr - Update ( Ajax post query)
@app.route('/update_emailaddr', methods=['POST'])
def update_emailaddr():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            ref_type = request.json['ref_type']
            # type = request.json['type']
            ref_type = request.json['ref_type']
            type = request.json['type']
            value = request.json['value']
            display_name = request.json['display_name']
            belongs_to_refs = request.json['belongs_to_refs']
            cur = mysql.connection.cursor()
            query = " UPDATE `email-addr` SET value=%s, display_name=%s, belongs_to_ref=%s where sno=%s and ref_type=%s"
            cur.execute(query, (value, display_name, belongs_to_refs, id, ref_type))
            mysql.connection.commit()
            print('successfully inserted')
            return jsonify({'result': 'success'})


# email addr - Delete ( Ajax post query)
@app.route('/delete_emailaddr', methods=['POST'])
def delete_emailaddr():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            ref_type = request.json['ref_type']
            query = "delete from `email-addr` where sno=%s AND ref_type=%s"
            cur = mysql.connection.cursor()
            cur.execute(query, (id, ref_type))
            mysql.connection.commit()
            print "successfully deleted"
            return jsonify({'result': 'success'})


# email msg  - Insert ( Ajax post query)
@app.route('/insert_emailmsg', methods=['POST'])
def insert_emailmsg():
    if g.user:
        if request.method == 'POST':
            obj_id = request.form['obj_id']
            obj_type = request.form['obj_type']
            ref_type = request.form['ref_type']
            type = request.form['type']
            is_multipart = request.form['is_multipart']
            date = request.form['date']
            content_type = request.form['content_type']
            from_ref = request.form['from_ref']
            sender_ref = request.form['sender_ref']
            to_refs = request.form['to_refs']
            cc_refs = request.form['cc_refs']
            bcc_refs = request.form['bcc_refs']
            subject = request.form['subject']
            received_lines = request.form['received_lines']
            additional_header_fields = request.form['additional_header_fields']
            body = request.form['body']
            raw_email_ref = request.form['raw_email_ref']
            created_by = g.user
            cur = mysql.connection.cursor()
            query = '''INSERT INTO `email-message` (obj_id, obj_type, ref_type, type, is_multipart, date, content_type, from_ref, sender_ref, to_refs, 
             cc_refs, bcc_refs, subject, received_lines, additional_header_fields, body, raw_email_ref,  created_by)
                             values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            cur.execute(query, (obj_id, obj_type, ref_type, type, is_multipart, date, content_type, from_ref, sender_ref, to_refs, cc_refs, bcc_refs,
                                subject, received_lines, additional_header_fields, body, raw_email_ref,  created_by))
            mysql.connection.commit()
            print('successfully inserted')
            return jsonify({'result': 'success'})


# email msg - Update ( Ajax post query)
@app.route('/update_emailmsg', methods=['POST'])
def update_emailmsg():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            obj_id = request.json['obj_id']
            obj_type = request.json['obj_type']
            ref_type = request.json['ref_type']
            type = request.json['type']
            is_multipart = request.json['is_multipart']
            date = request.json['date']
            content_type = request.json['content_type']
            from_ref = request.json['from_ref']
            sender_ref = request.json['sender_ref']
            to_refs = request.json['to_refs']
            cc_refs = request.json['cc_refs']
            bcc_refs = request.json['bcc_refs']
            subject = request.json['subject']
            received_lines = request.json['received_lines']
            additional_header_fields = request.json['additional_header_fields']
            body = request.json['body']
            raw_email_ref = request.json['raw_email_ref']
            cur = mysql.connection.cursor()
            query = " UPDATE `email-message` SET date=%s, content_type=%s, subject=%s, received_lines=%s," \
                    " additional_header_fields=%s, body=%s  where sno=%s and ref_type=%s"
            cur.execute(query, (date, content_type, subject, received_lines, additional_header_fields, body,
                                raw_email_ref, id, ref_type))
            mysql.connection.commit()
            print('successfully update')
            return jsonify({'result': 'success'})


# email msg - Delete ( Ajax post query)
@app.route('/delete_emailmsg', methods=['POST'])
def delete_emailmsg():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            ref_type = request.json['ref_type']
            query = "delete from `email-message` where sno=%s AND ref_type=%s"
            cur = mysql.connection.cursor()
            cur.execute(query, (id, ref_type))
            mysql.connection.commit()
            print "successfully deleted"
            return jsonify({'result': 'success'})


# file - Insert ( Ajax post query)
@app.route('/insert_file', methods=['POST'])
def insert_file():
    if g.user:
        if request.method == 'POST':
            obj_id = request.form['obj_id']
            obj_type = request.form['obj_type']
            ref_type = request.form['ref_type']
            type = request.form['type']
            extensions = request.form['ext_final']
            hashes = request.form['hash_final']
            size = request.form['size']
            name = request.form['nm']
            name_enc = request.form['name_enc']
            magicnum_hex = request.form['magicnum_hex']
            mime_type = request.form['mime_type']
            created = request.form['created']
            modified = request.form['modified']
            accessed = request.form['accessed']
            parent_directory_ref = request.form['parent_directory_ref']
            is_encrypted = request.form['is_encrypted']
            encryption_algorithm = request.form['encryption_algorithm']
            decryption_key = request.form['decryption_key']
            content_ref = request.form['content_ref']
            created_by = g.user
            cur = mysql.connection.cursor()
            query = '''INSERT INTO `file` (obj_id, obj_type, ref_type, type, extensions, hashes, size, name, name_enc, magic_number_hex, 
             mime_type, created, modified, accessed, parent_directory_ref, is_encrypted, encryption_algorithm, decryption_key, content_ref, created_by)
                             values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            cur.execute(query, (obj_id, obj_type, ref_type, type, extensions, hashes, size, name, name_enc, magicnum_hex, mime_type, created,
                                modified, accessed, parent_directory_ref, is_encrypted, encryption_algorithm, decryption_key, content_ref,  created_by))
            mysql.connection.commit()
            print('successfully inserted')
            return jsonify({'result': 'success'})


# file - Update ( Ajax post query)  -- to be updated
@app.route('/update_file', methods=['POST'])
def update_file():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            obj_id = request.json['obj_id']
            obj_type = request.json['obj_type']
            ref_type = request.json['ref_type']
            type = request.json['type']
            is_multipart = request.json['is_multipart']
            date = request.json['date']
            content_type = request.json['content_type']
            from_ref = request.json['from_ref']
            sender_ref = request.json['sender_ref']
            to_refs = request.json['to_refs']
            cc_refs = request.json['cc_refs']
            bcc_refs = request.json['bcc_refs']
            subject = request.json['subject']
            received_lines = request.json['received_lines']
            additional_header_fields = request.json['additional_header_fields']
            body = request.json['body']
            raw_email_ref = request.json['raw_email_ref']
            cur = mysql.connection.cursor()
            query = " UPDATE `file` SET date=%s, content_type=%s, subject=%s, received_lines=%s," \
                    " additional_header_fields=%s, body=%s  where sno=%s and ref_type=%s"
            cur.execute(query, (date, content_type, subject, received_lines, additional_header_fields, body,
                                raw_email_ref, id, ref_type))
            mysql.connection.commit()
            print('successfully update')
            return jsonify({'result': 'success'})


# file- Delete ( Ajax post query)
@app.route('/delete_file', methods=['POST'])
def delete_file():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            ref_type = request.json['ref_type']
            query = "delete from `file` where sno=%s AND ref_type=%s"
            cur = mysql.connection.cursor()
            cur.execute(query, (id, ref_type))
            mysql.connection.commit()
            print "successfully deleted"
            return jsonify({'result': 'success'})

# ipv4  - Insert ( Ajax post query)
@app.route('/insert_ipv4', methods=['POST'])
def insert_ipv4():
    if g.user:
        if request.method == 'POST':
            obj_id = request.form['obj_id']
            obj_type = request.form['obj_type']
            ref_type = request.form['ref_type']
            type = request.form['type']
            value = request.form['value']
            resolves_to_refs = request.form['resolves_to_refs']
            belongs_to_refs = request.form['belongs_to_refs']
            created_by = g.user
            cur = mysql.connection.cursor()
            query = '''INSERT INTO `ipv4-addr` (obj_id, obj_type, ref_type, type, value, resolves_to_refs, belongs_to_refs, created_by)
                             values (%s, %s, %s, %s, %s, %s, %s, %s)'''
            cur.execute(query, (obj_id, obj_type, ref_type, type, value, resolves_to_refs, belongs_to_refs, created_by))
            mysql.connection.commit()
            print('successfully inserted')
            return jsonify({'result': 'success'})


# ipv4 - Update ( Ajax post query)
@app.route('/update_ipv4', methods=['POST'])
def update_ipv4():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            ref_type = request.json['ref_type']
            type = request.json['type']
            value = request.json['value']
            cur = mysql.connection.cursor()
            query = " UPDATE `ipv4-addr` SET value=%s  where sno=%s and ref_type=%s"
            cur.execute(query, (value, id, ref_type))
            mysql.connection.commit()
            print('successfully update')
            return jsonify({'result': 'success'})


# ipv4 - Delete ( Ajax post query)
@app.route('/delete_ipv4', methods=['POST'])
def delete_ipv4():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            ref_type = request.json['ref_type']
            query = "delete from `ipv4-addr` where sno=%s AND ref_type=%s"
            cur = mysql.connection.cursor()
            cur.execute(query, (id, ref_type))
            mysql.connection.commit()
            print "successfully deleted"
            return jsonify({'result': 'success'})

# ipv6  - Insert ( Ajax post query)
@app.route('/insert_ipv6', methods=['POST'])
def insert_ipv6():
    if g.user:
        if request.method == 'POST':
            obj_id = request.form['obj_id']
            obj_type = request.form['obj_type']
            ref_type = request.form['ref_type']
            type = request.form['type']
            value = request.form['value']
            resolves_to_refs = request.form['resolves_to_refs']
            belongs_to_refs = request.form['belongs_to_refs']
            created_by = g.user
            cur = mysql.connection.cursor()
            query = '''INSERT INTO `ipv6-addr` (obj_id, obj_type, ref_type, type, value, resolves_to_refs, belongs_to_refs, created_by)
                             values (%s, %s, %s, %s, %s, %s, %s, %s)'''
            cur.execute(query, (obj_id, obj_type, ref_type, type, value, resolves_to_refs, belongs_to_refs, created_by))
            mysql.connection.commit()
            print('successfully inserted')
            return jsonify({'result': 'success'})


# ipv6 - Update ( Ajax post query)
@app.route('/update_ipv6', methods=['POST'])
def update_ipv6():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            ref_type = request.json['ref_type']
            type = request.json['type']
            value = request.json['value']
            cur = mysql.connection.cursor()
            query = " UPDATE `ipv6-addr` SET value=%s  where sno=%s and ref_type=%s"
            cur.execute(query, (value, id, ref_type))
            mysql.connection.commit()
            print('successfully update')
            return jsonify({'result': 'success'})


# ipv6 - Delete ( Ajax post query)
@app.route('/delete_ipv6', methods=['POST'])
def delete_ipv6():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            ref_type = request.json['ref_type']
            query = "delete from `ipv6-addr` where sno=%s AND ref_type=%s"
            cur = mysql.connection.cursor()
            cur.execute(query, (id, ref_type))
            mysql.connection.commit()
            print "successfully deleted"
            return jsonify({'result': 'success'})

# mac  - Insert ( Ajax post query)
@app.route('/insert_mac', methods=['POST'])
def insert_mac():
    if g.user:
        if request.method == 'POST':
            obj_id = request.form['obj_id']
            obj_type = request.form['obj_type']
            ref_type = request.form['ref_type']
            type = request.form['type']
            value = request.form['value']
            created_by = g.user
            cur = mysql.connection.cursor()
            query = '''INSERT INTO `mac-addr` (obj_id, obj_type, ref_type, type, value, created_by)
                             values (%s, %s, %s, %s, %s, %s)'''
            cur.execute(query, (obj_id, obj_type, ref_type, type, value, created_by))
            mysql.connection.commit()
            print('successfully inserted')
            return jsonify({'result': 'success'})


# mac - Update ( Ajax post query)
@app.route('/update_mac', methods=['POST'])
def update_mac():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            ref_type = request.json['ref_type']
            type = request.json['type']
            value = request.json['value']
            cur = mysql.connection.cursor()
            query = " UPDATE `mac-addr` SET value=%s  where sno=%s and ref_type=%s"
            cur.execute(query, (value, id, ref_type))
            mysql.connection.commit()
            print('successfully update')
            return jsonify({'result': 'success'})


# mac - Delete ( Ajax post query)
@app.route('/delete_mac', methods=['POST'])
def delete_mac():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            ref_type = request.json['ref_type']
            query = "delete from `mac-addr` where sno=%s AND ref_type=%s"
            cur = mysql.connection.cursor()
            cur.execute(query, (id, ref_type))
            mysql.connection.commit()
            print "successfully deleted"
            return jsonify({'result': 'success'})


# network-traffic  - Insert ( Ajax post query)
@app.route('/insert_networktraffic', methods=['POST'])
def insert_networktraffic():
    if g.user:
        if request.method == 'POST':
            obj_id = request.form['obj_id']
            obj_type = request.form['obj_type']
            ref_type = request.form['ref_type']
            type = request.form['type']
            extensions = request.form['ext_final']
            start = request.form['start']
            end = request.form['end']
            is_active = request.form['is_active']
            src_ref = request.form['src_ref']
            dst_ref = request.form['dst_ref']
            src_port = request.form['src_port']
            dst_port = request.form['dst_port']
            proto = request.form['proto']
            src_byte_count = request.form['src_byte_count']
            dst_byte_count = request.form['dst_byte_count']
            src_packets = request.form['src_packets']
            dst_packets = request.form['dst_packets']
            ipfix = request.form['ipfix']
            src_payload_ref = request.form['src_payload_ref']
            dst_payload_ref = request.form['dst_payload_ref']
            encapsulates_ref = request.form['encapsulates_ref']
            encapsulatedby_ref = request.form['encapsulatedby_ref']
            created_by = g.user
            cur = mysql.connection.cursor()
            query = '''INSERT INTO `network-traffic` (obj_id, obj_type, ref_type, type, extensions,
            start, end, is_active, src_ref, dst_ref, src_port, dst_port, protocols, src_byte_count, dst_byte_count,
             src_packets, dst_packets, ipfix, src_payload_ref, dst_payload_ref, encapsulates_refs, encapsulated_by_ref,
              created_by) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s,
                              %s, %s, %s)'''
            cur.execute(query, (obj_id, obj_type, ref_type, type, extensions, start, end, is_active, src_ref,
                                dst_ref, src_port, dst_port, proto, src_byte_count, dst_byte_count,  src_packets,
                                dst_packets, ipfix, src_payload_ref, dst_payload_ref, encapsulates_ref,
                                encapsulatedby_ref, created_by))
            mysql.connection.commit()
            print('successfully inserted')
            return jsonify({'result': 'success'})


# network-traffic - Update ( Ajax post query)
@app.route('/update_networktraffic', methods=['POST'])  # -- to be updated
def update_networktraffic():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            ref_type = request.json['ref_type']
            type = request.json['type']
            value = request.json['value']
            cur = mysql.connection.cursor()
            query = " UPDATE `mac-addr` SET value=%s  where sno=%s and ref_type=%s"
            cur.execute(query, (value, id, ref_type))
            mysql.connection.commit()
            print('successfully update')
            return jsonify({'result': 'success'})


# network-traffic - Delete ( Ajax post query)
@app.route('/delete_networktraffic', methods=['POST'])
def delete_networktraffic():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            ref_type = request.json['ref_type']
            query = "delete from `network-traffic` where sno=%s AND ref_type=%s"
            cur = mysql.connection.cursor()
            cur.execute(query, (id, ref_type))
            mysql.connection.commit()
            print "successfully deleted"
            return jsonify({'result': 'success'})


# process - Insert ( Ajax post query)
@app.route('/insert_process', methods=['POST'])
def insert_process():
    if g.user:
        if request.method == 'POST':
            obj_id = request.form['obj_id']
            obj_type = request.form['obj_type']
            ref_type = request.form['ref_type']
            type = request.form['type']
            extensions = request.form['ext_final']
            is_hidden = request.form['is_hidden']
            pid = request.form['pid']
            name = request.form['nm']
            created = request.form['created']
            cwd = request.form['cwd']
            arguments = request.form['args']
            command_line = request.form['cmd_line']
            environment_variables = request.form['env_var']
            opened_connection_refs = request.form['opened_conn_refs']
            creator_user_ref = request.form['create_user_refs']
            binary_ref = request.form['binary_refs']
            parent_ref = request.form['parent_refs']
            child_refs = request.form['child_refs']
            created_by = g.user
            cur = mysql.connection.cursor()
            query = '''INSERT INTO `process` (obj_id, obj_type, ref_type, type, extensions,
            is_hidden, pid, name, created, cwd, arguments, command_line, environment_variables, opened_connection_refs, creator_user_ref,
             binary_ref, parent_ref, child_refs, created_by) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
              %s, %s, %s, %s, %s, %s)'''
            cur.execute(query, (obj_id, obj_type, ref_type, type, extensions, is_hidden, pid, name, created,
                                cwd, arguments, command_line, environment_variables, opened_connection_refs, creator_user_ref,  binary_ref,
                                parent_ref, child_refs, created_by))
            mysql.connection.commit()
            print('successfully inserted')
            return jsonify({'result': 'success'})


# process - Update ( Ajax post query)
@app.route('/update_process', methods=['POST'])  # -- to be updated
def update_process():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            ref_type = request.json['ref_type']
            type = request.json['type']
            value = request.json['value']
            cur = mysql.connection.cursor()
            query = " UPDATE `process` SET value=%s  where sno=%s and ref_type=%s"
            cur.execute(query, (value, id, ref_type))
            mysql.connection.commit()
            print('successfully update')
            return jsonify({'result': 'success'})


# process - Delete ( Ajax post query)
@app.route('/delete_process', methods=['POST'])
def delete_process():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            ref_type = request.json['ref_type']
            query = "delete from `process` where sno=%s AND ref_type=%s"
            cur = mysql.connection.cursor()
            cur.execute(query, (id, ref_type))
            mysql.connection.commit()
            print "successfully deleted"
            return jsonify({'result': 'success'})

# software - Insert ( Ajax post query)
@app.route('/insert_software', methods=['POST'])
def insert_software():
    if g.user:
        if request.method == 'POST':
            obj_id = request.form['obj_id']
            obj_type = request.form['obj_type']
            ref_type = request.form['ref_type']
            type = request.form['type']
            name = request.form['nm']
            cpe = request.form['cpe']
            languages = request.form['lang']
            vendor = request.form['vendor']
            version = request.form['version']
            created_by = g.user
            cur = mysql.connection.cursor()
            query = '''INSERT INTO `software` (obj_id, obj_type, ref_type, type, name,
            cpe, languages, vendor, version, created_by) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            cur.execute(query, (obj_id, obj_type, ref_type, type, name, cpe, languages, vendor, version,
                                 created_by))
            mysql.connection.commit()
            print('successfully inserted')
            return jsonify({'result': 'success'})


# software - Update ( Ajax post query)
@app.route('/update_software', methods=['POST'])  # -- to be updated
def update_software():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            ref_type = request.json['ref_type']
            type = request.json['type']
            value = request.json['value']
            cur = mysql.connection.cursor()
            query = " UPDATE `software` SET value=%s  where sno=%s and ref_type=%s"
            cur.execute(query, (value, id, ref_type))
            mysql.connection.commit()
            print('successfully update')
            return jsonify({'result': 'success'})


# software - Delete ( Ajax post query)
@app.route('/delete_software', methods=['POST'])
def delete_software():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            ref_type = request.json['ref_type']
            query = "delete from `software` where sno=%s AND ref_type=%s"
            cur = mysql.connection.cursor()
            cur.execute(query, (id, ref_type))
            mysql.connection.commit()
            print "successfully deleted"
            return jsonify({'result': 'success'})


# URL insert ( Ajax post query)
@app.route('/insert_url', methods=['POST'])
def insert_url():
    if g.user:
        if request.method == 'POST':
            obj_id = request.form['obj_id']
            obj_type = request.form['obj_type']
            ref_type = request.form['ref_type']
            type = request.form['type']
            value = request.form['url_val']
            created_by = g.user
            cur = mysql.connection.cursor()
            query = '''INSERT INTO `url` (obj_id, obj_type, ref_type, type, value, created_by)
             values (%s, %s, %s, %s, %s, %s)'''
            cur.execute(query, (obj_id, obj_type, ref_type, type, value, created_by))
            mysql.connection.commit()
            print('successfully inserted')
            return jsonify({'result': 'success'})


# URL - Update ( Ajax post query)
@app.route('/update_url', methods=['POST'])  # -- to be updated
def update_url():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            ref_type = request.json['ref_type']
            type = request.json['type']
            value = request.json['value']
            cur = mysql.connection.cursor()
            query = " UPDATE `url` SET value=%s  where sno=%s and ref_type=%s"
            cur.execute(query, (value, id, ref_type))
            mysql.connection.commit()
            print('successfully update')
            return jsonify({'result': 'success'})


# URL - Delete ( Ajax post query)
@app.route('/delete_url', methods=['POST'])
def delete_url():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            ref_type = request.json['ref_type']
            query = "delete from `url` where sno=%s AND ref_type=%s"
            cur = mysql.connection.cursor()
            cur.execute(query, (id, ref_type))
            mysql.connection.commit()
            print "successfully deleted"
            return jsonify({'result': 'success'})

# user-account insert ( Ajax post query)
@app.route('/insert_useracc', methods=['POST'])
def insert_useracc():
    if g.user:
        if request.method == 'POST':
            obj_id = request.form['obj_id']
            obj_type = request.form['obj_type']
            ref_type = request.form['ref_type']
            type = request.form['type']
            extensions = request.form['ua_ext_final']
            user_id = request.form['user_id']
            account_login = request.form['account_login']
            acc_type = request.form['acc_type']
            disp_name = request.form['disp_name']
            is_serv_acc = request.form['is_serv_acc']
            is_priv = request.form['is_priv']
            can_escalate_privs = request.form['can_escalate_privs']
            is_disabled = request.form['is_disabled']
            acc_created = request.form['acc_created']
            acc_expires = request.form['acc_expires']
            pwd_last_changed = request.form['pwd_last_changed']
            acc_first_login = request.form['acc_first_login']
            acc_last_login = request.form['acc_last_login']
            created_by = g.user
            cur = mysql.connection.cursor()
            query = '''INSERT INTO `user-account` (obj_id, obj_type, ref_type, type, extensions, user_id, account_login, 
            account_type, display_name, is_service_account, is_privileged, can_escalate_privs, is_disabled, account_created, account_expires, 
            password_last_changed, account_first_login, account_last_login,  created_by)
             values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            cur.execute(query, (obj_id, obj_type, ref_type, type, extensions, user_id, account_login, acc_type,
                                disp_name, is_serv_acc, is_priv, can_escalate_privs, is_disabled,
                                acc_created, acc_expires, pwd_last_changed, acc_first_login, acc_last_login, created_by))
            mysql.connection.commit()
            print('successfully inserted')
            return jsonify({'result': 'success'})


# user-account - Update ( Ajax post query)
@app.route('/update_useracc', methods=['POST'])  # -- to be updated
def update_useracc():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            ref_type = request.json['ref_type']
            type = request.json['type']
            value = request.json['value']
            cur = mysql.connection.cursor()
            query = " UPDATE `user-account` SET value=%s  where sno=%s and ref_type=%s"
            cur.execute(query, (value, id, ref_type))
            mysql.connection.commit()
            print('successfully update')
            return jsonify({'result': 'success'})


# user-account - Delete ( Ajax post query)
@app.route('/delete_useracc', methods=['POST'])
def delete_useracc():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            ref_type = request.json['ref_type']
            query = "delete from `user-account` where sno=%s AND ref_type=%s"
            cur = mysql.connection.cursor()
            cur.execute(query, (id, ref_type))
            mysql.connection.commit()
            print "successfully deleted"
            return jsonify({'result': 'success'})


# windows reg key insert ( Ajax post query)
@app.route('/insert_winregkey', methods=['POST'])
def insert_winregkey():
    if g.user:
        if request.method == 'POST':
            obj_id = request.form['obj_id']
            obj_type = request.form['obj_type']
            ref_type = request.form['ref_type']
            type = request.form['type']
            key = request.form['key']
            modified = request.form['modified']
            creator_user_ref = request.form['creator_user_ref']
            number_of_subkeys = request.form['num_subkeys']
            created_by = g.user
            cur = mysql.connection.cursor()
            query = '''INSERT INTO `windows-registry-key` (obj_id, obj_type, ref_type, type, `key`, modified, creator_user_ref, number_of_subkeys, created_by)
             values (%s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            cur.execute(query, (obj_id, obj_type, ref_type, type, key, modified, creator_user_ref, number_of_subkeys, created_by))
            mysql.connection.commit()
            print('successfully inserted')
            return jsonify({'result': 'success'})


# windows reg key - Update ( Ajax post query)
@app.route('/update_winregkey', methods=['POST'])  # -- to be updated
def update_winregkey():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            ref_type = request.json['ref_type']
            type = request.json['type']
            value = request.json['value']
            cur = mysql.connection.cursor()
            query = " UPDATE `windows-registry-key` SET value=%s  where sno=%s and ref_type=%s"
            cur.execute(query, (value, id, ref_type))
            mysql.connection.commit()
            print('successfully update')
            return jsonify({'result': 'success'})


# windows reg key - Delete ( Ajax post query)
@app.route('/delete_winregkey', methods=['POST'])
def delete_winregkey():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            ref_type = request.json['ref_type']
            query = "delete from `windows-registry-key` where sno=%s AND ref_type=%s"
            cur = mysql.connection.cursor()
            cur.execute(query, (id, ref_type))
            mysql.connection.commit()
            print "successfully deleted"
            return jsonify({'result': 'success'})


# x509 insert ( Ajax post query)
@app.route('/insert_x509', methods=['POST'])
def insert_x509():
    if g.user:
        if request.method == 'POST':
            obj_id = request.form['obj_id']
            obj_type = request.form['obj_type']
            ref_type = request.form['ref_type']
            type = request.form['type']
            is_self_signed = request.form['is_selfsigned']
            hash_type = request.form['hash_type']
            hash_value = request.form['hash_value']
            version = request.form['version']
            serial_num = request.form['serial_num']
            sig_algo = request.form['sig_algo']
            issuer = request.form['issuer']
            validity_notbefore = request.form['validity_notbefore']
            validity_notafter = request.form['validity_notafter']
            subject = request.form['subject']
            subject_pubkey_algo = request.form['subject_pubkey_algo']
            subject_pubkey_mod = request.form['subject_pubkey_mod']
            subject_pubkey_expo = request.form['subject_pubkey_expo']
            created_by = g.user
            cur = mysql.connection.cursor()
            query = '''INSERT INTO `x509-certificate` (obj_id, obj_type, ref_type, type, is_self_signed, hash_type, 
            hash_value, version, serial_number, signature_algorithm, issuer, validity_not_before, validity_not_after,
             subject, subject_public_key_algorithm, subject_public_key_modulus, subject_public_key_exponent, created_by)
             values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            cur.execute(query, (obj_id, obj_type, ref_type, type, is_self_signed, hash_type, hash_value, version,
                                serial_num, sig_algo, issuer, validity_notbefore, validity_notafter, subject, subject_pubkey_algo,
                                subject_pubkey_mod, subject_pubkey_expo, created_by))
            mysql.connection.commit()
            print('successfully inserted')
            return jsonify({'result': 'success'})


# x509- Update ( Ajax post query)
@app.route('/update_x509', methods=['POST'])  # -- to be updated
def update_x509():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            ref_type = request.json['ref_type']
            type = request.json['type']
            value = request.json['value']
            cur = mysql.connection.cursor()
            query = " UPDATE `x509-certificate` SET value=%s  where sno=%s and ref_type=%s"
            cur.execute(query, (value, id, ref_type))
            mysql.connection.commit()
            print('successfully update')
            return jsonify({'result': 'success'})


# x509 - Delete ( Ajax post query)
@app.route('/delete_x509', methods=['POST'])
def delete_x509():
    if g.user:
        if request.method == 'POST':
            id = request.json['id']
            ref_type = request.json['ref_type']
            query = "delete from `x509-certificate` where sno=%s AND ref_type=%s"
            cur = mysql.connection.cursor()
            cur.execute(query, (id, ref_type))
            mysql.connection.commit()
            print "successfully deleted"
            return jsonify({'result': 'success'})


#########################
# Attack pattern - Basic SDO creation - Insert
@app.route('/attackpattern', methods=['GET', 'POST'])
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
################ End of Malware #####################

# ********* Report ********************
# Report- Main object creation - Insert operation
@app.route('/create_report', methods=['POST'])
def create_report():
    if g.user:
        if request.method == 'POST':
            type = request.form['type']
            name = request.form['nm']
            labels = request.form['labels']
            description = request.form['desc']
            published = request.form['published']
            obj_ref = request.form['obj_ref']
            created_by = g.user
            cur = mysql.connection.cursor()
            cur.execute(
                '''INSERT INTO `report` (type, name, description , labels, published, obj_references, created_by) 
                 values (%s, %s, %s, %s, %s, %s, %s)''',
                (type, name, description, labels, published, obj_ref, created_by))
            mysql.connection.commit()
            print('success input data')
        return redirect(url_for('home'))
    else:
        return redirect(url_for('index'))


@app.route('/update_report', methods=['POST'])
def update_report():
    if g.user:
        if request.method == 'POST':
            id = request.form['id']
            name = request.form['nm']
            labels = request.form['labels']
            description = request.form['desc']
            published = request.form['published']
            obj_ref = request.form['obj_ref']
            cur = mysql.connection.cursor()
            cur.execute(
                '''UPDATE `report` SET name=%s, description=%s, labels=%s, published=%s, obj_references=%s WHERE sno=%s ''',
                (name, description,  labels, published, obj_ref, id))
            mysql.connection.commit()
            print "successfully Updated"
        return redirect(url_for('home'))
    else:
        return redirect(url_for('index'))


################ End of Report #####################
# ********* Threat actor ********************
# Threat actor- Main object creation - Insert operation

@app.route('/create_threatactor',methods=['POST'])
def create_threatactor():
    if g.user:
        if request.method == 'POST':
            type = request.form['type']
            name = request.form['nm']
            labels = request.form['labels']
            description = request.form['desc']
            aliases = request.form['aliases']
            roles = request.form['roles']
            goals = request.form['goals']
            sophistication = request.form['sophistication']
            res_level = request.form['res_level']
            prim_motiv = request.form['prim_motiv']
            sec_motiv = request.form['sec_motiv']
            per_motiv = request.form['per_motiv']
            created_by = g.user
            cur = mysql.connection.cursor()
            cur.execute(
                '''INSERT INTO `threat-actor` (type, name, labels, aliases, description , roles, goals, sophistication,
                 resource_level, primary_motivation, secondary_motivations, personal_motivations, created_by) 
                 values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                (type, name, labels, description, aliases, roles, goals, sophistication, res_level, prim_motiv, sec_motiv, per_motiv, created_by))
            mysql.connection.commit()
            print('success input data')
        return redirect(url_for('home'))
    else:
        return redirect(url_for('index'))


@app.route('/update_threatactor', methods=['POST'])
def update_threatactor():
    if g.user:
        if request.method == 'POST':
            id = request.form['id']
            name = request.form['nm']
            labels = request.form['labels']
            description = request.form['desc']
            aliases = request.form['aliases']
            roles = request.form['roles']
            goals = request.form['goals']
            sophistication = request.form['sophistication']
            res_level = request.form['res_level']
            prim_motiv = request.form['prim_motiv']
            sec_motiv = request.form['sec_motiv']
            per_motiv = request.form['per_motiv']
            cur = mysql.connection.cursor()
            cur.execute(
                '''UPDATE `threat-actor` SET name=%s, labels=%s, aliases=%s, description=%s , roles=%s, goals=%s, sophistication=%s,
                 resource_level=%s, primary_motivation=%s, secondary_motivations=%s, personal_motivations=%s WHERE sno=%s ''',
                (name, labels,aliases, description, roles, goals, sophistication, res_level, prim_motiv, sec_motiv, per_motiv, id))
            mysql.connection.commit()
            print "successfully Updated"
        return redirect(url_for('home'))
    else:
        return redirect(url_for('index'))





################ End of Threat actor #####################
# ********* Tool ********************
# Tool- Main object creation - Insert operation
@app.route('/create_tool', methods=['POST'])
def create_tool():
    if g.user:
        if request.method == 'POST':
            type = request.form['type']
            name = request.form['nm']
            labels = request.form['labels']
            description = request.form['desc']
            tool_ver = request.form['tool_ver']
            created_by = g.user
            cur = mysql.connection.cursor()
            cur.execute(
                '''INSERT INTO `tool` (type, name, labels, description, tool_version, created_by) 
                 values (%s, %s, %s, %s, %s, %s)''',
                (type, name, labels, description, tool_ver, created_by))
            mysql.connection.commit()
            print('success input data')
        return redirect(url_for('home'))
    else:
        return redirect(url_for('index'))


@app.route('/update_tool', methods=['POST'])
def update_tool():
    if g.user:
        if request.method == 'POST':
            id = request.form['id']
            name = request.form['nm']
            labels = request.form['labels']
            description = request.form['desc']
            tool_ver = request.form['tool_ver']
            cur = mysql.connection.cursor()
            cur.execute(
                '''UPDATE `tool` SET name=%s, labels=%s, description=%s, tool_version=%s WHERE sno=%s ''',
                (name, labels, description, tool_ver, id))
            mysql.connection.commit()
            print "successfully Updated"
        return redirect(url_for('home'))
    else:
        return redirect(url_for('index'))


################ End of Tool #####################

# ********* Vulnerability ********************
# Vulnerability- Main object creation - Insert operation
@app.route('/create_vulnerability', methods=['POST'])
def create_vulnerability():
    if g.user:
        if request.method == 'POST':
            type = request.form['type']
            name = request.form['nm']
            description = request.form['desc']
            created_by = g.user
            cur = mysql.connection.cursor()
            cur.execute(
                '''INSERT INTO `vulnerability` (type, name, description, created_by) 
                 values (%s, %s, %s, %s)''',
                (type, name, description, created_by))
            mysql.connection.commit()
            print('success input data')
        return redirect(url_for('home'))
    else:
        return redirect(url_for('index'))


@app.route('/update_vulnerability', methods=['POST'])
def update_vulnerability():
    if g.user:
        if request.method == 'POST':
            id = request.form['id']
            name = request.form['nm']
            description = request.form['desc']
            cur = mysql.connection.cursor()
            cur.execute(
                '''UPDATE `vulnerability` SET name=%s, description=%s WHERE sno=%s ''',
                (name, description, id))
            mysql.connection.commit()
            print "successfully Updated vulnerability"
        return redirect(url_for('home'))
    else:
        return redirect(url_for('index'))

################ End of vulnerability #####################

# ********* MAEC objects  ********************

# ********* MAEC Behavior  ********************
@app.route('/create_behavior',methods=['POST'])
def create_behavior():
    if g.user:
        if request.method == 'POST':
            type = request.form['type']
            name = request.form['nm']
            description = request.form['desc']
            timestamp = request.form['timestmp']
            created_by = g.user
            cur = mysql.connection.cursor()
            cur.execute(
                '''INSERT INTO `behavior` (type, name, description, timestamp, created_by) 
                 values (%s, %s, %s, %s, %s)''',
                (type, name, description, timestamp, created_by))
            mysql.connection.commit()
            print('success input data')
        return redirect(url_for('home'))
    else:
        return redirect(url_for('index'))


@app.route('/update_behavior', methods=['POST'])
def update_behavior():
    if g.user:
        if request.method == 'POST':
            id = request.form['id']
            name = request.form['nm']
            description = request.form['desc']
            timestamp = request.form['timestmp']
            attributes = request.form['attr_val_final']
            action_refs = request.form['action_refs']
            cur = mysql.connection.cursor()
            cur.execute(
                '''UPDATE `behavior` SET name=%s, description=%s, timestamp=%s, attributes=%s, action_refs=%s  WHERE sno=%s ''',
                (name, description, timestamp, attributes, action_refs,  id))
            mysql.connection.commit()
            print "successfully Updated behavior"
        return redirect(url_for('home'))
    else:
        return redirect(url_for('index'))

################ End of Behavior #####################

# ********* MAEC Collection  ********************

@app.route('/create_collection',methods=['POST'])
def create_collection():
    if g.user:
        if request.method == 'POST':
            type = request.form['type']
            description = request.form['desc']
            association_type = request.form['assoc_type']
            created_by = g.user
            cur = mysql.connection.cursor()
            cur.execute(
                '''INSERT INTO `collection` (type, description, association_type, created_by) 
                 values (%s, %s, %s, %s)''',
                (type, description, association_type, created_by))
            mysql.connection.commit()
            print('success input data')
        return redirect(url_for('home'))
    else:
        return redirect(url_for('index'))

@app.route('/update_collection', methods=['POST'])
def update_collection():
    if g.user:
        if request.method == 'POST':
            id = request.form['id']
            description = request.form['desc']
            association_type = request.form['assoc_type']
            entity_refs = request.form['entity_refs']
            observable_refs = request.form['observ_refs']
            cur = mysql.connection.cursor()
            cur.execute(
                '''UPDATE `collection` SET description=%s, association_type=%s, entity_refs=%s, observable_refs=%s  WHERE sno=%s ''',
                (description, association_type, entity_refs, observable_refs,  id))
            mysql.connection.commit()
            print "successfully Updated collection"
        return redirect(url_for('home'))
    else:
        return redirect(url_for('index'))

################ End of Collection #####################
# ********* MAEC Malware action  ********************


@app.route('/create_malwareaction',methods=['POST'])
def create_malaction():
    if g.user:
        if request.method == 'POST':
            name = request.form['nm']
            type = request.form['type']
            description = request.form['desc']
            is_successful = request.form['is_successful']
            timestmp = request.form['timestmp']
            created_by = g.user
            cur = mysql.connection.cursor()
            cur.execute(
                '''INSERT INTO `malware-action` (type, name,  description, is_successful, timestamp, created_by) 
                 values (%s, %s, %s, %s, %s, %s)''',
                (type, name,  description, is_successful, timestmp, created_by))
            mysql.connection.commit()
            print('success input data')
        return redirect(url_for('home'))
    else:
        return redirect(url_for('index'))


@app.route('/update_malwareaction', methods=['POST'])
def update_malaction():
    if g.user:
        if request.method == 'POST':
            id = request.form['id']
            name = request.form['nm']
            description = request.form['desc']
            is_successful = request.form['is_successful']
            timestamp = request.form['timestamp']
            input_obj_refs = request.form['input_object_refs']
            output_obj_refs = request.form['output_object_refs']
            cur = mysql.connection.cursor()
            cur.execute('''UPDATE `malware-action` SET name=%s, description=%s, is_successful=%s, timestamp=%s,
             input_refs=%s, output_refs=%s WHERE sno=%s''',
                        (name, description, is_successful, timestamp, input_obj_refs, output_obj_refs, id))
            mysql.connection.commit()
            print "Successfully updated collection"
            return jsonify({'result': 'success'})
        return redirect(url_for('home'))
    else:
        return redirect(url_for('index'))

################ End of Malware action #####################
# ********* MAEC Malware Family  ********************
@app.route('/create_malwarefamily',methods=['POST'])
def create_malwarefamily():
    if g.user:
        if request.method == 'POST':
            type = request.form['type']
            labels = request.form['labels']
            description = request.form['desc']
            comm_strings = request.form['comm_strings']
            created_by = g.user
            cur = mysql.connection.cursor()
            cur.execute(
                '''INSERT INTO `malware-family` (type, labels,  description, common_strings, created_by) 
                 values (%s, %s, %s, %s, %s)''',
                (type, labels, description, comm_strings, created_by))
            mysql.connection.commit()
            print('success input data')
        return redirect(url_for('home'))
    else:
        return redirect(url_for('index'))


@app.route('/update_malwarefamily',methods=['POST'])
def update_malwarefamily():
    if g.user:
        if request.method == 'POST':
            id = request.form['id']
            labels = request.form['labels']
            description = request.form['desc']
            comm_strings = request.form['comm_strings']
            comm_capabilities = request.form['comm_capabilities']
            comm_coderefs = request.form['comm_coderefs']
            comm_behaviorrefs = request.form['comm_behaviorrefs']
            references = request.form['references']
            created_by = g.user
            cur = mysql.connection.cursor()
            cur.execute('''UPDATE `malware-family` SET labels=%s, description=%s, common_strings=%s, common_capabilities=%s,
             common_coderefs=%s, common_behaviorRefs=%s, `references`=%s WHERE sno=%s and created_by=%s''',
                        (labels, description, comm_strings, comm_capabilities, comm_coderefs, comm_behaviorrefs, references, id, created_by))
            mysql.connection.commit()
            print('successfully updated!!')
        return redirect(url_for('home'))
    else:
        return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)
