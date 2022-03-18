#!/usr/bin/env python3

from flask import Flask, jsonify, request
from flask_caching import Cache
import requests, json, aiohttp, asyncio 
import ast

# Cache config setup
config = {
	"DEBUG":True,
	"CACHE_TYPE":"SimpleCache",
	"CACHE_DEFAULT_TIMEOUT":300
}

app = Flask(__name__)

# Enables Flask to use the above defined cache-config
app.config.from_mapping(config)
cache = Cache(app)

# Error response
tagsErrorMessage = {"error":"Tags parameter is required"}
sortByErrorMessage = {"error":"sortBy parameter invalid"}
directionErrorMessage = {"error":"direction parameter invalid"}

# Acceptable parameter values for /api/posts
acceptableSortBy = ['id','reads','likes','popularity',None]
acceptableDirection = ['desc','asc',None]

# Parallel Requst stuff below
async def get(url, session):
	try:
		async with session.get(url=url) as response:
			resp = await response.read()
			# DEBUG Statement
			# print("Successfully got url {} with resp of length {}.".format(url,len(resp)))
	except Exception as e:
		print("Unable to get url {} due to {}.".format(url,e.__class__))

	return resp


async def main(urls):
	async with aiohttp.ClientSession() as session:
		ret = await asyncio.gather(*[get(url, session) for url in urls])

	# DEBUG Statement
	# print("Finalized all. Return is a list of len {} outputs".format(len(ret)))
	
	return ret

# Welcome message
@app.route("/")
def welcome():
	"""
	Basic welcome message. Enjoy my API
	"""
	return "Welcome to my API! Enjoy your stay!\n"

# Checks whether server is alive
@app.route("/api/ping",methods=["GET"]) 
#@cache.cached(timeout=50,query_string=True)
def ping():
	"""
	Checks whether Walnut's API is reachable.
	@return Returns successMessage if the API is reachable, 
	        otherwise returns hostUnreachableMessage
	"""
	successMessage = {"success":True}
	hostUnreachableMessage = {"success":False}

	url = 'https://api.hatchways.io/assessment/blog/posts' # Baseline
	r = requests.get(url)
	if (r.status_code == 400):
		return jsonify(successMessage),200

	return jsonify(hostUnreachableMessage), 400

@app.route('/api/posts',methods=["GET"])
@cache.cached(timeout=50,query_string=True)
def posts():
	"""
	Pulls all specified entries with at least one tag from Walnut's 
	API and compiles them all into a godlist. Removes duplicates.
	@param string tags List of tags to be queried seperated via comma (ex. science,technology,history)
	@param string sortBy Category to sort the returned entries by. Default is 'id'
	@param string direction Order of entries returned, either ascending or descending. Default is 'asc'
	@return Return list of compiled results from Walnut's API / 200 Status Code, otherwise return one of the three
			error messages concerning the parameters: tags, sortBy, and direction / 400 Status Code
	"""

	# Parse through GET request arguments
	tags = request.args.get("tags",type=str) 
	sortBy = request.args.get("sortBy",default="id",type=str)
	direction = request.args.get("direction",default="asc",type=str)

	posts = {} # JSON object which will be returned 
	results = [] # Results from querying Walnut's API
	godlist = [] # Final list containing all entries
	noneDump = [] # This was the best way I could add items to godlist w/o overwriting godlist everytime :(
	
	# Error handling
	if (tags is None):
		return jsonify(tagsErrorMessage), 400
	elif (sortBy not in acceptableSortBy):
		return jsonify(sortByErrorMessage), 400
	elif (direction not in acceptableDirection):
		return jsonify(directionErrorMessage), 400

	tags = tags.split(',')

	# Form list of URL's to fetch from
	urls = ["https://api.hatchways.io/assessment/blog/posts?tag=%s" % tag for tag in tags if tag != '' or tag != '&']
	results = asyncio.run(main(urls))

	# Append results to godlist
	for result in results:
		# Convert bytes object to dictionary.
		result = result.decode("UTF-8")
		result = ast.literal_eval(result)
		
		# Iterate through every dictionary and filter out repeat entries while appending to godlist
		# append returns None and using list comprehension for godlist overwrites the list everytime,
		# so I dump the return from append here. 
		noneDump = [godlist.append(entry) for entry in result['posts'] if entry not in godlist]

	posts["posts"] = godlist

	# Sort list of results by descending or ascending
	if (direction == 'desc'):
		posts['posts'].sort(key=lambda x: x[sortBy], reverse=True)
	else:
		posts['posts'].sort(key=lambda x: x[sortBy])	

	return posts, 200