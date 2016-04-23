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
TRASER = "traser"

@app.route('/')
@app.route('/index')
def index():

	s = ""
	s = request.args.get('s', '')
	print "***Request.args = ", request.args.items()

	if s == SKX:
		search = SKX
		print "s SKX = ", search
	elif s == GSHOCK:
		search = GSHOCK
		print "s GSHOCK = ", search
	elif s == PROTREK:
		search = PROTREK
		print "s PROTREK= ", search
	elif s == PANERAI:
		search = PANERAI
		print "s PANERAI= ", search
	elif s == TRASER:
		search = TRASER
		print "s TRASER= ", search
	elif s != "":
		search = s.replace(" ", "")
	else:
		search = SKX
		print "s ELSE = ", search

	count = 33
	fotos = []

	api = InstagramAPI(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

	max_id = 0
	api.tag(search)

	etiquetadas, next = api.tag_recent_media(count, max_id, search)

	for media in etiquetadas:
		print media.caption
		media_dicc = {}
		media_dicc['thumb_url'] = media.images['low_resolution'].url
		media_dicc['big_url'] = media.images['standard_resolution'].url
		fotos.append(media_dicc)

	return render_template("index.html", fotos=fotos)
