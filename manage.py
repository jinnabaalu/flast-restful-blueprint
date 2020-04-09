import sys

from app.api.hello import *
from app.api.square import *


app = Flask(__name__) 
api = Api(app) 

api.add_resource(Hello, '/') 
api.add_resource(Square, '/square/<int:num>') 


if __name__ == '__main__': 
	app.run(debug = True) 
