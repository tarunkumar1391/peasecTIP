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
            ref_type = request.form['obj_type']
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
            cur = mysql.connection.cursor()
            cur.execute(
                '''UPDATE `malware-action` SET name=%s, description=%s, is_successful=%s, timestamp=%s  WHERE sno=%s ''',
                (name, description, is_successful, timestamp,  id))
            mysql.connection.commit()
            print "successfully Updated collection"
        return redirect(url_for('home'))
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
