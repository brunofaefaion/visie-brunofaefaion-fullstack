from flask import Flask, render_template, request, redirect
from flask_restful import Resource, Api
from flask_mysqldb import MySQL

app = Flask(__name__)
api = Api(app)


app.config['MYSQL_HOST'] = 'jobs.visie.com.br'
app.config['MYSQL_USER'] = 'brunofaion'
app.config['MYSQL_PASSWORD'] = 'YnJ1bm9mYWlv'
app.config['MYSQL_DB'] = 'brunofaion'

mysql = MySQL(app)

@app.route('/', methods = ['GET', 'POST', 'DELETE'])
def home():
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        result = cursor.execute(''' SELECT * FROM pessoas ''')
        mysql.connection.commit()
        data = cursor.fetchall()
        cursor.close()
        return render_template('index.html', data=data)

    if request.method == 'POST':
        values = request.form
        sql = ''' INSERT INTO pessoas(`nome`,`rg`,`cpf`,`data_nascimento`,`data_admissao`,`funcao`) VALUES(%s,%s,%s,%s,%s,%s) '''
        args = (values['name'],values['rg'],values['cpf'],values['born'],values['admission'],values['function'])
        cursor = mysql.connection.cursor()
        result = cursor.execute(sql, args)
        mysql.connection.commit()
        data = cursor.fetchall()
        cursor.close()
        return redirect('/')

    if request.method == 'DELETE':
        return 'DELETE'

if __name__ == '__main__':
    app.run(debug=True)
