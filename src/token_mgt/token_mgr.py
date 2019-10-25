import os
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant
# from src.utils.conf import get_conf

# ACCOUNT_SID = get_conf().get('setup', 'TWILIO_ACCOUNT_SID')
# API_KEY_SID = get_conf().get('setup', 'TWILIO_API_KEY')
# API_KEY_SECRET = get_conf().get('setup', 'TWILIO_API_SECRET')

ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
API_KEY_SID = os.environ['TWILIO_API_KEY']
API_KEY_SECRET = os.environ['TWILIO_API_SECRET']


def get_token(identity, room_name):
    try:
        # Create an Access Token
        token = AccessToken(ACCOUNT_SID, API_KEY_SID, API_KEY_SECRET)
        # token = AccessToken(account_sid, api_key, api_secret, identity=identity)

        # Set the Identity of this token
        token.identity = identity

        # Grant access to Video
        grant = VideoGrant(room=room_name)
        token.add_grant(grant)

        # Serialize the token as a JWT
        jwt = token.to_jwt()
        return jwt.decode()
    except Exception as e:
        print(e)
