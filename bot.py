#!/usr/bin/python
from config import getApi
import os

api = getApi()

def postStatus(update): # tweets out update (string)
  status = api.PostUpdate(update)
  print(status)

def postWithImage(update, pic): # tweets out picture
  print(api.PostUpdate(update, media=pic))