import browser_cookie3

# https://github.com/borisbabic/browser_cookie3

# 获取Chrome 浏览器中的Cookie
chrome_cookiejar = browser_cookie3.chrome()        
firefox_cookiejar = browser_cookie3.firefox()  # 获取Firefox 浏览器中的Cookie
print(type(chrome_cookiejar), '#'*10, type(firefox_cookiejar))
print(len(chrome_cookiejar))
count = 0
for cookie in chrome_cookiejar:
    count += 1
    if count <= 10:
        print(cookie)
