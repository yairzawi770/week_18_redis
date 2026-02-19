import os
import redis


REDIS_URI = os.getenv("REDIS_URI", "redis://localhost:6379")
r = redis.Redis(host='localhost', port=6379, decode_responses=True)





















