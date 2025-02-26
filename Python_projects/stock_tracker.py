import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "3ET51PG7GJYM4J4Q"
NEWS_API_KEY = "0bce931fae364ca49b47aff7bbeb0d70"

r = requests.get(STOCK_ENDPOINT, params={
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
})

data = r.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

diff = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))

print(diff)

diff_percentage = diff / float(yesterday_closing_price) * 100

print(diff_percentage)


if diff_percentage > 1:
    print("Get News")
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": STOCK_API_KEY
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_data = news_response.json()
    print(news_data)

if diff_percentage > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_data = news_response.json()
    articles = news_data["articles"]

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]
    print(three_articles)



#Optional TODO: Format the message like this: 
