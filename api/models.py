from django.db import models
import random, string
# Create your models here.
# Following are the basic steps to follow to create API:
# 1. Models
# 2. Serializer 
# 3. Views
def generate_unique_code():
    length =  6
    while True:
        code = '.'.join(random.choices(string.ascii_uppercase, k =length))
        if Room.objects.filter(code=code).count() == 0:
            break
class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default= 1)
    created_at = models.DateTimeField(auto_now_add=True)