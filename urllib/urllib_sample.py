import urllib.request
import urllib.robotparser as rob

url = "http://books.toscrape.com/"
urllib.request.urlopen(url)
request_url = urllib.request.urlopen(url)
print(request_url.read())

bot = rob.RobotFileParser()
url_bot = url + '/robot.txt'
bot_loc = bot.set_url(url_bot)
print(bot_loc)

bot_content = bot.read()
print(bot_content)

web_crawl = bot.can_fetch('*', url)
print(web_crawl)
