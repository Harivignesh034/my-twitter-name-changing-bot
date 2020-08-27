import tweepy
import os
def create_api():
  consumer_key=os.getenv('consumer_key')
  consumer_secret=os.getenv('consumer_secret')
  access_tokens=os.getenv('access_tokens')
  access_token_secret=os.getenv('access_token_secret')
  auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
  auth.set_access_token(access_tokens,access_token_secret)
  api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
  api.verify_credentials()
  print('API Created')
  return api
  
  import time

def follower_count(user):
  emoji_numbers={0:"0️⃣",1:"1️⃣",2:"2️⃣",3:"3️⃣",4:"4️⃣",5:"5️⃣",6:"6️⃣",7:"7️⃣",8:"8️⃣",9:"9️⃣"}

  uf_split = [int(i) for i in str(user.followers_count)]

  emoji_followers = ''.join([emoji_numbers[j] for j in uf_split if j in emoji_numbers.keys()])
  return emoji_followers

api = create_api()

def main():
  while True:
     user=api.get_user('Harivig82738362')
     print(user)
     api.update_profile(name=f'HARI {follower_count(user)} ')
     print(f'updating twitter name :HARI|{follower_count(user)} Follwers')
     print('writing to refresh')
     time.sleep(60)  
main()
