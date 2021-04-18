from flask import Flask, request
from flask_restful import Api, Resource,reqparse,abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
api = Api(app) #wrap our app in an api
app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
#db.create_all() #created once but we want to model first, comment out after the first run or delete this line

class PlantModel(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50),nullable=False)
	category = db.Column(db.String(80), nullable=False)
	sunlight = db.Column(db.String, nullable=False)
	
	def __repr__(self):
		return f"Plant(name={name}, sunlight={sunlight})"
plant_put_args = reqparse.RequestParser()
plant_put_args.add_argument("name", type=str, help="Name of the plant")
plant_put_args.add_argument("category", type=str, help="Tpye of the plant")
plant_put_args.add_argument("sunlight", type=str, help="Sunlight requrirements")

resource_fields = {
	'id' : fields.Integer,
	'name': fields.String,
	'category': fields.String,
	'sunlight': fields.String
}

# def abort_if_id_doesnt_exist(plant_id):
	# if plant_id not in plants:
		# abort(404, message="Could not find plant")
# def abort_if_video_exists(plant_id):
	# if plant_id in plants:
		# abort(409, message+"Plant with that ID already exists")
#inherits from resource
class Plant(Resource):
	@marshal_with(resource_fields) #for serializing objects
	def get(self,plant_id):#when a get request is sent, overrident the get method
		# abort_if_id_doesnt_exist(plant_id)
		result = PlantModel.query.get(id=plant_id)
		return plants[plant_id]
	@marshal_with(resource_fields)
	def put(self, plant_id):
		# abort_if_video_exists(plant_id)
		#args = plant_put_args.parse_args()	
		#plants[plant_id] = args
		#print(request.form)
		args = plant_put_args.parse_args()
		plant = PlantModel(id=plant_id, name=args['name'], category=args['category'],sunlight=['sunlight'])
		db.session.add(plant)
		db.session.commit()#permanently putting it in
		return plants[plant_id], 201
	def delete(self, plant_id):
		# abort_if_id_doesnt_exist(plant_id)
		del plants[plant_id]
		return "",204
#register it as a resource; <> = to define parameters 
api.add_resource(Plant, "/plant/<int:plant_id>")

if __name__ == "__main__":
	app.run(debug=True)#Will start our server; only in dev envt
	
	
	### video mark : 26:45