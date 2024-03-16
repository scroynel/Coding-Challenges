import requests
import pandas

'''
Get statistics of all players from https://www.afl.com.au/stats/leaders
'''

url = "https://api.afl.com.au/statspro/playersStats/seasons/CD_S2024014"

payload = {}
headers = {
  'Accept': '*/*',
  'Sec-Fetch-Site': 'same-site',
  'Accept-Encoding': 'gzip, deflate, br',
  'If-None-Match': 'W/"bc3a08f6c5fb45000b9de30fdac1b2bc"',
  'Sec-Fetch-Mode': 'cors',
  'Accept-Language': 'en-US,en;q=0.9',
  'Origin': 'https://www.afl.com.au',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Safari/605.1.15',
  'Referer': 'https://www.afl.com.au/',
  'Connection': 'keep-alive',
  'Host': 'api.afl.com.au',
  'Sec-Fetch-Dest': 'empty',
  'x-media-mis-token': '59118c686ddcbff055cdbbf63c1c106a',
  'Cookie': 'ak_bmsc=B639ADA33060D78FF092A320ED4667A9~000000000000000000000000000000~YAAQkMbPFztC5heOAQAAEMsASBcS1Tqs0OscPssiWjufkyFshGNUeNQTAyXh8iBQjW8dJnIS/6PSfnL+UFaxQhTSlxO9DxRCj0ADBApVah5pGH+uVXOJGFeYD/2+LuyRT3VL098tNaqzNKZuwUmpDyas3keChQVng+5CeiXFWPlk5xnTUHqGY/95yIseWw6anXy3Ez9I/+8KJjbhJ7FG8YRTPHmf8VgvZ6r+CHnU1KnYksxSm1He4iWJnnhW0lGdgLpRp6slpL6KQeAS2WYWrJQ9vV9ZCwiIeEWvR16w3c+PRFRRt4GioAwph8FQbpB9CJLClR/65g2v4901ZnUYRwiQOpVsh2JyyZU1l1s8RZpG2AidVUmLOlaTMA==; bm_sv=7DD9091A6ED8FFBC4AA390B9803CAC2A~YAAQIfkwFz5Pyy2OAQAAmwRCSBcNqYoSgb+TDxL/RpKGw3Apv72reAyMsF/0yQX9WNXNDvXqhP0tdiwFHUDqo4FdhXrCn9Kf6csvRgApGJfVGz6O8ZIn62hn0EhOJg3JQ7GIi3CaO/ayhFwIHLs9LgE/BqPzgll0FS5Xfv8LswqbgubP/CxlvFwlxehH8eIjbrAJfO75IDa0OsYDd+Q6Dt2Dhn4wGPsKzddSVH+G7eCxRiowi+wew4hgGl3K7Ezy~1'
}

r = requests.get(url, headers=headers)

playerdata = r.json()

df = pandas.json_normalize(playerdata)
df.to_csv('response.csv', index=False)