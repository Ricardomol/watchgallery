from instagram.client import InstagramAPI

CLIENT_ID = '8f997230fd2e44399d0f7a4085c642f8'
CLIENT_SECRET = '9c02c793fd3f47a4b5415d487cbf7b16'

api = InstagramAPI(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
popular_media = api.media_popular(count=20)
for media in popular_media:
    print media.images['thumbnail'].url