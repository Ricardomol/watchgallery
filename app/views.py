from flask import render_template
from flask import request
from app import app
from instagram.client import InstagramAPI

CLIENT_ID = '8f997230fd2e44399d0f7a4085c642f8'
CLIENT_SECRET = '9c02c793fd3f47a4b5415d487cbf7b16'

SKX = "skx007"
GSHOCK = "gshock"
PROTREK = "protrek"
PANERAI = "panerai"

@app.route('/')
@app.route('/index')
def index():

	search = ""
	search_term = request.args.get('search_term', '')

	if search_term == SKX:
		search = SKX
		print "Search_term SKX = ", search
	elif search_term == GSHOCK:
		search = GSHOCK
		print "Seearch_term GSHOCK = ", search
	elif search_term == PROTREK:
		search = PROTREK
		print "Seearch term PROTREK= ", search
	elif search_term == PANERAI:
		search = PANERAI
		print "Seearch term PANERAI= ", search
	else:
		search = SKX
		print "Seearch ELSE = ", search

	count = 30
	fotos = []

	api = InstagramAPI(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

	max_id = 0
	api.tag(search) 

	etiquetadas, next = api.tag_recent_media(count, max_id, search)

	for media in etiquetadas:
		print media.caption
		media_dicc = {}
		media_dicc['thumb_url'] = media.images['thumbnail'].url
		media_dicc['big_url'] = media.images['standard_resolution'].url
		fotos.append(media_dicc)

	return render_template("index.html",
		        	fotos = fotos)
