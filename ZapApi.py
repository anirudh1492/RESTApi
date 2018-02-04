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
    		

    		conn = mysql.connect()
    		cursor = conn.cursor()
    		cursor.callproc('spcreate',(_name,_city,_rid))
    		data = cursor.fetchall()
    		#return {'Restraunt_id': _rid, 'Name':_name
    		conn.commit()
    	except Exception as e:
    		return {'error': str(e)}

class CreateMenuItem(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('Mtype',type=str,help='Enter the ID for the Restraunt')
        parser.add_argument('Menu_id',type=str,help='Enter the Menu Id')
        parser.add_argument('Mname',type=str,help='Enter the Menu Id')
        args = parser.parse_args()

        _mtype = args['Mtype']
        _mid = args['Menu_id']
        _mname = args['Mname']

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('menuitem',(_mtype,_mid,_mname))
        data = cursor.fetchall()
        conn.commit()

class CreateMenu(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('Restraunt_id',type=str,help='Enter the ID for the Restraunt')
        parser.add_argument('Menu_id',type=str,help='Enter the Menu Id')
        args = parser.parse_args()

        _rid = args['Restraunt_id']
        _mid = args['Menu_id']

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('createmenu',(_rid,_mid))
        data = cursor.fetchall()
        conn.commit()

class Restraunt(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('Name',type=str,help='Enter the city name to find its restraunts')
        args = parser.parse_args()
        _rfname = args['Name']
        conn = mysql.connect()
        cursor = conn.cursor()
        cmdstr = ('CALL showdata("'+_rfname+'");')
        cursor.execute(cmdstr)
        data = cursor.fetchall()
        temp = dict()
        for row in data:
            temp[row[0]] = {'City':row[1],'Country':row[2]}
        
        return jsonify(temp)

class GetMenuItem(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('Rname',type=str,help='Enter the restraunt to find its menu')
        args = parser.parse_args()

        _rname = args['Rname']
    
        conn = mysql.connect()
        cursor = conn.cursor()
        
        #cmdstr = ('select mname from t3 INNER JOIN t2 ON t2.mid = t3.mid INNER JOIN t1 ON t2.rid = t1.rid WHERE name ="'+_rname+'" ')
        cmdstr = ('CALL getmenuitems("'+_rname+'");')
        print('::::',_rname)
        #cursor.callproc('getmenuitems',(_rname))
        cursor.execute(cmdstr)
        data = cursor.fetchall()
        temp = dict()
        for row in data:
            temp[_rname] = {'Itemname':row[0],'MenuType':row[1]}
        
        return jsonify(temp)

class GetMenu(Resource):
    def get(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('select * from testdatabase.t2')
        data = cursor.fetchall()
        
        for row in data:
            return jsonify(temp)    
        


api.add_resource(CreateRest, '/CreateRest')
api.add_resource(CreateMenuItem,'/Crtmitem')
api.add_resource(CreateMenu,'/Crmenu')
api.add_resource(Restraunt, '/GetRestraunt')
api.add_resource(GetMenu,'/GetMenu')
api.add_resource(GetMenuItem,'/GetMenuItem')

if __name__ == '__main__':
    app.run(debug=True)