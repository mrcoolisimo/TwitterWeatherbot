#access twitter
import tweepy
#access HTML data
import requests

#Connect to Twitter
consumer_key = '...' 
consumer_secret = '...'
access_token = '...'
access_token_secret = '...'

#Hand over authorization to Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#Set Access Token
auth.set_access_token(access_token, access_token_secret)
#Let API read from Tweepy
api = tweepy.API(auth)

#Pulls my twitter details from my account
#user = api.me()
#print(user.name)

def main():
    #search for keywords in tweets
    searchterm = ("python", "coding")

    #and then retweet two of them, reporting any errors
    numberofTweets = 2
    for tweet in tweepy.Cursor(api.search, searchterm).items(numberofTweets):
        try:
            tweet.retweet()
            print("Tweet Retweeted")
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

#tweets for us
def howToTweet(x):
    api.update_status("WeatherBot: " + x)
    print("success[howToTweet]")

def tweetWeather():
    #access the correct URL for your city
    city = 'Seattle'
    URL = 'http://api.openweathermap.org/data/2.5/weather?&APPID=YOURKEYHERE=' + city

    #Get data from URL 
    json_data = requests.get(URL).json()

    #Get max temperature in Kelvin and converts it to Fahrenheit
    tempKelvinMax = json_data['main']['temp_max']
    tempFahrenheitMax = int(convertToFahrenheit(tempKelvinMax))
    #print (int(tempFahrenheitMax))

    #Get min temperature in Kelvin and converts it to Fahrenheit
    tempKelvinMin = json_data['main']['temp_min']
    tempFahrenheitMin = int(convertToFahrenheit(tempKelvinMin))

    #Description
    weatherDescription = json_data['weather'][0]['description']

    weatherReport = "Seattle's weather report: " + weatherDescription + ", low " + str(tempFahrenheitMin) + " and high " + str(tempFahrenheitMax)
    howToTweet(weatherReport)

#Converts a value x to Fahrenheit and returns it
def convertToFahrenheit(x):
    fahrenheit = (x - 273.15) * 9 / 5 + 32
    return fahrenheit

tweetWeather()