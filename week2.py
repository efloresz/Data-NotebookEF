''' Understand the data and describe the data using Python libraries '''
# Load dataset into pandas python notebook
import pandas as pd
df = pd.read_csv('twcs.csv')
print(df)

''' Identify 3 ways the data can be cleaned '''
# The data can be cleaned by reordering the 'created_at' attribute by date added.
# Most recent tweet at the top of data set & oldest tweets at the end

# The data can be cleaned by reorganizing the 'author_id' by alphabetic order.
# Start with 'author_id' that starts with 'a' & ends with 'z'

# I noticed there are repeated 'author_id' we can group them together.
# While maintaining the 'author_id' in alphabetic order
# This will make it easier to access tweets from certain users

''' How many inbound & outbound responses are in the dataset? ''' 
# Inbound (original message) & Outbound (replies)
# There seems to be 1-5 Outbound responses per inbound response.
# TODO * estimated calculations 

''' How many unique tweets are there & top 20 Twitter users? '''
# Unique tweets: TODO * estimated calculations 
# Top users: TODO * find most repeated users
'''
VerizonSupport, ChipotleTweets, ATVIAssist, AdobeCare, AmazonHelp,
AirbnbHelp, nationalrailenq, AirAsiaSupport, NikeSupport, AskAmex,
McDonalds, AppleSupport, Uber_Support, Delta
'''