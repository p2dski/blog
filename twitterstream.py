# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Connecting to Twitter's API is the most difficult part for most people. There are plenty of other tutorials online on how to do it, but here I'll just go through how I connect. This is the way I learned it. Most of this comes from [oauth2's repository](https://github.com/simplegeo/python-oauth2).

# <codecell>

import oauth2
import urllib2 as urllib
import json

# <markdowncell>

# First, we'll set up instances for our Token and Consumer. To get your own key, token, and secret visit https://apps.twitter.com/.

# <codecell>

API_key = "mNVvc8X5Qv4xcQev85mA"
API_secret = "IgXwIAnVCmEA0E9BH20XGatJvYXITolgOAzxnKKCHE"
access_token = "461995403-hikjj8AqGaQNtIwqFZ8R4VoL5sOMOcr6V6MThV97"
access_token_secret = "6v0ps1m1DKDhpss7ng27u62z3ENqQkjSiIbVHMW6tB6Zk"

# <codecell>

oauth_token    = oauth2.Token(key=access_token, secret=access_token_secret)
oauth_consumer = oauth2.Consumer(key=API_key, secret=API_secret)

# <markdowncell>

# Now, we're going to sign our request.

# <codecell>

signature_method = oauth2.SignatureMethod_HMAC_SHA1()

# <codecell>

http_method = "GET"
_debug = 0

# <codecell>

http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

# <codecell>

def twitterreq(url, method, parameters):
  req = oauth2.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

# <markdowncell>

# Now we have constructed, signed, and opened a twitter request we can move on to the fun stuff. First, let's grab some tweets.

# <codecell>

def fetchtweets():
    url = "https://stream.twitter.com/1/statuses/sample.json"
    parameters = []
    response = twitterreq(url, "GET", parameters)
    for line in response:
        print line.strip()

if __name__ == '__main__':
  fetchtweets()
# <codecell>


