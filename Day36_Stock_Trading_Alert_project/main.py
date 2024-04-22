from time import sleep
import requests
from twilio.rest import Client

TWILIO_ACCOUNT_SID = ""
TWILIO_AUTH_TOKEN = ""

STOCK_API_URL = "https://www.alphavantage.co/query"
STOCK_API_KEY = ""

NEWS_API_URL = "https://newsapi.org/v2/everything"
NEWS_API_KEY = ""

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_parameters ={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":STOCK_API_KEY
}

news_parameters ={
    "q":COMPANY_NAME,
    "apikey":NEWS_API_KEY
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

response = requests.get(STOCK_API_URL,params = stock_parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

#Get the yesterday's closing stock price
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']
print(yesterday_closing_price)

#Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']
print(day_before_yesterday_closing_price)

#Find the positive difference between 1 and 2
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)

#Percentage difference
diff_percent = (difference / float(yesterday_closing_price)) * 100
print(diff_percent)


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

#If percentage is greater than 5, then print ("Get News")
if diff_percent >1:
    news_response = requests.get(NEWS_API_URL, params = news_parameters)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    print(three_articles)

    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in \
            three_articles]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(body = article, from_ = '+12513125281',to = '+PhoneNumber')
        sleep(10)
        print(message.status)


