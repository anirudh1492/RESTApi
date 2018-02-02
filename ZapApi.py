from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_restful import reqparse
from flaskext.mysql import MySQL
import json

app = Flask(__name__)


mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'an1rudh'
app.config['MYSQL_DATABASE_DB'] = 'testdatabase'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

api = Api(app)


class CreateRest(Resource):
    def post(self):
    	try:
    		parser = reqparse.RequestParser()
    		parser.add_argument('Restraunt_id',type=str,help = 'Enter an Id for the Restraunt')
    		parser.add_argument('Name',type=str,help='Enter a name for the Restraunt')
    		parser.add_argument('Country',type=str,help='Enter the name of the country it is located in.')
    		parser.add_argument('City',type=str,help='Enter the name of the city it is present in.')
    		args = parser.parse_args()

    		_rid = args['Restraunt_id']
    		_name = args['Name']
    		_country = args['Country']
    		_city = args['City']
    		_emp = args['Num_of_employee']

    		conn = mysql.connect()
    		cursor = conn.cursor()
    		cursor.callproc('spcreate',(_name,_city,_rid))
    		data = cursor.fetchall()
    		#return {'Restraunt_id': _rid, 'Name':_name
    		conn.commit()
    	except Exception as e:
    		return {'error': str(e)}

api.add_resource(CreateRest, '/CreateRest')


if __name__ == '__main__':
    app.run(debug=True)