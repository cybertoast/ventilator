"""
# TODO: encoding, license, copyright
"""
import redis
import logging

# TODO: better log naming so that it's for this application!
logging.basicConfig(filename='log.log', format='%(levelname)s:%(asctime)s - %(message)s',
                    datefmt='%H:%M:%S', level=logging.NOTSET)
useredis = False

# TODO: redis connection parameters should be configurable for each host
r = redis.StrictRedis(
    host='dupi1.local',
    port=6379,
    password='',
    decode_responses=True)

# TODO: These parameters should come from configuration
fullscreen = False

# TOD: what's args? and how is it used?
args = None
