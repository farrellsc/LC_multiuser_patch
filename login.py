import time
from selenium import webdriver

csrftoken = "WoFQyqNDLakJ3kWKiDlgonCZs4x85lMGFFNQMoGIdPu3Ed9hJwuO2WKgfQjZEr7j"
LEETCODE_SESSION = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMTM0MDA4OSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWM1NzcxM2Y2YjA4MWJhYjdmNGVkMGJkZTk3ZjM5YmM0NTVmOTA2MCIsImlkIjoxMzQwMDg5LCJlbWFpbCI6IlVjb2x1bWJpYTE4TENzaGFyZUBvdXRsb29rLmNvbSIsInVzZXJuYW1lIjoiVWNvbHVtYmlhMThMQ3NoYXJlIiwidXNlcl9zbHVnIjoidWNvbHVtYmlhMThsY3NoYXJlIiwiYXZhdGFyIjoiaHR0cHM6Ly93d3cuZ3JhdmF0YXIuY29tL2F2YXRhci9jNjc2MTEyN2VlMWEwYjNmNjUwMjlkNDUwNTM5OTNhYi5wbmc_cz0yMDAiLCJ0aW1lc3RhbXAiOiIyMDE4LTA3LTI2IDA5OjM2OjM5Ljg4NTQxMiswMDowMCIsIlJFTU9URV9BRERSIjoiMjAyLjEyMC4yMzQuMTA1IiwiSURFTlRJVFkiOiI1NmYwOTJhMjkxOTVmM2MwNGNhNGEzYTFmZmU5ZTg3MCIsIl9zZXNzaW9uX2V4cGlyeSI6MTIwOTYwMH0.mpR0EsOZBEHqEgamxEkGaSndPzUEEQWFfTpbLonddkc"

cookies1 = {
	'name': 'csrftoken',
	'value': csrftoken, 
	'hehe': 'hehe'
}
cookies2 = {
	'name': 'LEETCODE_SESSION',
	'value': LEETCODE_SESSION
}

# headers = {
# 	'Host': 'leetcode.com',
# 	'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
# 	'Accept': '*/*',
# 	'Accept-Language': 'en-GB,en;q=0.5',
# 	'Accept-Encoding': 'gzip, deflate, br',
# 	'Referer': 'https://leetcode.com/accounts/login/',
# 	'X-NewRelic-ID': 'UAQDVFVRGwEAXVlbBAg=',
# 	'X-Requested-With': 'XMLHttpRequest',
# 	'Cookie': 'csrftoken=' + csrftoken + ';',
# 	'Connection': 'keep-alive'
# }


# data = {
#     'csrfmiddlewaretoke': csrftoken,
#     'login': 'Ucolumbia18LCshare',
#     'password': '180725LeetcodeShare'
# }

options = webdriver.ChromeOptions()
options.add_argument('Host=leetcode.com')
options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36')
options.add_argument('Accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8')
options.add_argument('Accept-Language=zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7')
options.add_argument('Accept-Encoding=gzip, deflate, br')
options.add_argument('Connection=keep-alive')
options.add_argument('Upgrade-Insecure-Requests=1')
driver = webdriver.Chrome("./chrome_driver/chromedriver_windows.exe", chrome_options=options)

driver.get("http://leetcode.com")
driver.delete_all_cookies()
driver.add_cookie(cookies1)
driver.add_cookie(cookies2)
driver.execute_script('window.open("https://leetcode.com");')
