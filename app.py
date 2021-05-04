from flask import Flask, render_template
from flask_restful import Resource, Api
from flask_mysqldb import MySQL

app = Flask(__name__)
api = Api(app)


app.config['MYSQL_HOST'] = 'jobs.visie.com.br'
app.config['MYSQL_USER'] = 'brunofaion'
app.config['MYSQL_PASSWORD'] = 'YnJ1bm9mYWlv'
app.config['MYSQL_DB'] = 'brunofaion'

mysql = MySQL(app)

class Pessoas(Resource):
    def get(self):
        # cursor = mysql.connection.cursor()
        # result = cursor.execute(''' SELECT * FROM pessoas ''')
        # mysql.connection.commit()
        # data = cursor.fetchall()
        # cursor.close()
        return {"msg": "hello world!"}

api.add_resource(Pessoas, '/a')

@app.route('/')
def home():
    cursor = mysql.connection.cursor()
    result = cursor.execute(''' SELECT * FROM pessoas ''')
    mysql.connection.commit()
    data = cursor.fetchall()
    cursor.close()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
