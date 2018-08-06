from flask import Flask, render_template, json, request, redirect, session
from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = 'Why wouldI tell you my secret key?'

mysql = MySQL()

#MySQL configuration
app.config['MYSQL_DATABASE_USER'] = 'user1'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] ='BucketList'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
mysql.init_app(app)



@app.route('/')
def main():
    return render_template('index.html')


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/signUp', methods=['POST'])
def signUp():
    # Read the data from UI
    name=request.form['inputName']
    email=request.form['inputEmail']
    password=request.form['inputPassword']
    

    
    # SQL configuration of the recieved values from UI
    conn = mysql.connect()
    cursor = conn.cursor()
    hashed_password = generate_password_hash(password)
    cursor.execute('CALL BucketList.sp_createUser(%s, %s, %s)',(name, email, hashed_password))
    
    
    data = cursor.fetchall()

    if len(data) is 0:
        conn.commit()
        return json.dumps({'message': 'User created successfully!'})
    else:
        return json.dumps({'error': str(data[0])})


@app.route('/showSignin')
def showSignin():
    return render_template('signin.html')


@app.route('/validateLogin',methods=['POST'])
def validateLogin():
    con= mysql.connect()
    cursor = con.cursor()
    
    username = request.form['inputEmail']
    password = request.form['inputPassword']

       
    cursor.execute('CALL BucketList.sp_validateLogin(%s)',(username))

    data=cursor.fetchall()
    

    if len(data)>0:
        if check_password_hash(str(data[0][3]),password):
            session['user'] = data[0][0]
            return redirect('/userHome')
        else:
            return render_template('error.html', error='Wrong Email address or Password.')
    else:
        
        return render_template('error.html', error='Wrong Email and Password.')

    
    cursor.close()
    con.close()
    

@app.route('/userHome')
def userHome():
    if session.get('user'):
        print("---------"+ str(session.get('user')))
        return render_template('userHome.html')
    else:
        return render_template('error.html', error='Unauthorized Access!')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


@app.route('/showAddWish')
def showAddWish():
    return render_template('addWish.html')

@app.route('/addWish', methods=['POST'])
def addWish():
    title = request.form['inputTitle']
    description = request.form['inputDescription']
    user=str(session.get('user'))

    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute('CALL BucketList.sp_addWish(%s, %s, %s)',(title, description, user))

    data = cursor.fetchall()

    if len(data) is 0:
        conn.commit()
        return redirect('/userHome')
    else:
        return render_template('error.html', error="An error has occured!")

    cursor.close()
    conn.close()

@app.route('/getWish')
def getWIsh():
    if session.get('user'):
        user = session.get('user')
    
        # connect to MySQL and fetch data
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('CALL BucketList.sp_GetWishByUser(%s)',(user))

        data = cursor.fetchall()

        data_dicts=[]
        for d in data:
            data_dict={
                    'ID':d[0],
                    'Title':d[1],
                    'Description':d[2],
                    'Date':d[3]
                    }
            data_dicts.append(data_dict)
        
        return json.dumps(data_dicts)


    else:
        return render_template('error.html', error='Unauthorized Access !')



if __name__=="__main__":
    app.run(debug=True);


