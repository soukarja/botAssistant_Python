import requests
from lxml.html import fromstring
from itertools import cycle
import random
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import math

class botAssistant:
    def __init__(self):
        self.proxyList = []
        self.defaultProxyLimit = 10
        self.__useragentList = []

    def generate_proxies(self) :
        url = 'https://free-proxy-list.net/'
        response = requests.get(url)
        parser = fromstring(response.text)
        proxies = set()
        for i in parser.xpath('//tbody/tr')[:1000] :
            if i.xpath('.//td[7][contains(text(),"yes")]') :
                # Grabbing IP and corresponding PORT
                proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
                proxies.add(proxy)
        self.proxyList = list(proxies)
        return self.proxyList

    def findProxies(self, limit=0) :
        print("Fetching Proxies...")
        proxies = self.generate_proxies()
        proxy_pool = cycle(proxies)
        proxies_working = set()
        url = 'https://httpbin.org/ip'
        if limit <= 0:
            max_limit = len(proxies)
        else:
            max_limit = limit
            self.defaultProxyLimit = limit
        # max_limit = 11
        for i in range(0, min(max_limit, len(proxies)-1)) :

            proxy = next(proxy_pool)
            print(f"Request #{i+1}/{min(max_limit, len(proxies))}")
            try :
                response = requests.get(url, proxies={"http" : proxy, "https" : proxy})
                print(response.json())
                proxies_working.add(proxy)
            except :
                # print("Skipping. Connnection error")
                continue

        # print(proxies_working)
        print(f"Found {len(proxies_working)} proxies")
        self.proxyList = list(proxies_working)
        return self.proxyList

    def getRandomProxy(self, proxy=""):
        if proxy.strip() != "" :
            return self.getProxyHeaders(proxy)

        if len(self.proxyList) <= 0 :
            self.discardProxy()

        return self.getProxyHeaders(self.proxyList[random.randint(0, len(self.proxyList)-1)])

    def getProxyHeaders(self, proxy=""):
        if proxy.strip() == "":
            print("No Proxy Found")
            return {"http" : "", "https" : ""}

        return {"http" : proxy, "https" : proxy}

    def calculateTimeInSeconds(self, hours=0, minutes=0, seconds=0, days=0, weeks=0, months=0, years=0):
        return (hours * 60 * 60) + (minutes * 60) + (seconds) + (days*60*60*24) + (weeks*60*60*24*7) + (months*60*60*24*30) + (years*60*60*24*365)

    def calculateTimeInMs(self, hours=0, minutes=0, seconds=0, days=0, weeks=0, months=0, years=0, milliSec=0):
        return (self.calculateTimeInSeconds(hours=hours, minutes=minutes, seconds=seconds, days=days, months=months, weeks=weeks, years=years) * 1000) + milliSec

    def sleepRandom(self, min=5, max=15)  :
        val = random.randint(min, max) + (random.randint(11, 99) / 100)
        print("Waiting for " + str(val) + " seconds")
        time.sleep(val)

    def getUserAgentList(self, devices=[]):
        ua = []
        if len(devices) <= 0:
            devices.append("android")
            devices.append("iphone")
            devices.append("windows")
            devices.append("tablet")
            devices.append("desktop")
            devices.append("setupbox")
            devices.append("gameconsole")
            devices.append("bots")
            devices.append("ereader")

        if "android" in devices:
            # Samsung Galaxy S9
            ua.append('Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36')
            # Samsung Galaxy S8
            ua.append('Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36')
            # Samsung Galaxy S7
            ua.append('Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36')
            # Samsung Galaxy S7 Edge
            ua.append('Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36')
            # Samsung Galaxy S6
            ua.append('Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36')
            # Samsung Galaxy S6 Edge Plus
            ua.append('Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36')
            # Nexus 6P
            ua.append('Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6P Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36')
            # Sony Xperia XZ
            ua.append('Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36')
            # Sony Xperia Z5
            ua.append('Mozilla/5.0 (Linux; Android 6.0.1; E6653 Build/32.2.A.0.253) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36')
            # HTC One X10
            ua.append('Mozilla/5.0 (Linux; Android 6.0; HTC One X10 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36')
            # HTC One M9
            ua.append('Mozilla/5.0 (Linux; Android 6.0; HTC One M9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.3')

        if "iphone" in devices:
            # Apple iPhone XR (Safari)
            ua.append('Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1')
            # Apple iPhone XS (Chrome)
            ua.append('Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1')
            # Apple iPhone XS Max (Firefox)
            ua.append('Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/13.2b11866 Mobile/16A366 Safari/605.1.15')
            # Apple iPhone X
            ua.append('Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1')
            # Apple iPhone 8
            ua.append('Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1')
            # Apple iPhone 8 Plus
            ua.append('Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A5370a Safari/604.1')
            # Apple iPhone 7
            ua.append('Mozilla/5.0 (iPhone9,3; U; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1')
            # Apple iPhone 7 Plus
            ua.append('Mozilla/5.0 (iPhone9,4; U; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1')
            # Apple iPhone 6
            ua.append('Mozilla/5.0 (Apple-iPhone7C2/1202.466; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543 Safari/419.3')

        if "windows" in devices:
            # Microsoft Lumia 650
            ua.append('Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254')
            # Microsoft Lumia 550
            ua.append('Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536')
            # Microsoft Lumia 950
            ua.append('Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058')

        if "tablet" in devices:
            # Google Pixel C
            ua.append('Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36')
            # Sony Xperia Z4 Tablet
            ua.append('Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36')
            # Nvidia Shield Tablet K1
            ua.append('Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36')
            # Samsung Galaxy Tab S3
            ua.append('Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36')
            # Samsung Galaxy Tab A
            ua.append('Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36')
            # Amazon Kindle Fire HDX 7
            ua.append('Mozilla/5.0 (Linux; Android 4.4.3; KFTHWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/47.1.79 like Chrome/47.0.2526.80 Safari/537.36')
            # LG G Pad 7.0
            ua.append('Mozilla/5.0 (Linux; Android 5.0.2; LG-V410/V41020c Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/34.0.1847.118 Safari/537.36')

        if "desktop" in devices:
            # Windows 10-based PC using Edge browser
            ua.append('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246')
            # Chrome OS-based laptop using Chrome browser (Chromebook)
            ua.append('Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36')
            # Mac OS X-based computer using a Safari browser
            ua.append('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9')
            # Windows 7-based PC using a Chrome browser
            ua.append('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36')
            # Linux-based PC using a Firefox browser
            ua.append('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1')

        if "setupbox" in devices:
            # Chromecast
            ua.append('Mozilla/5.0 (CrKey armv7l 1.5.16041) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.0 Safari/537.36')
            # Roku Ultra
            ua.append('Roku4640X/DVP-7.70 (297.70E04154A)')
            # Minix NEO X5
            ua.append('Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30')
            # Amazon 4K Fire TV
            ua.append('Mozilla/5.0 (Linux; Android 5.1; AFTS Build/LMY47O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/41.99900.2250.0242 Safari/537.36')
            # Google Nexus Player
            ua.append('Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T)')
            # Apple TV 5th Gen 4K
            ua.append('AppleTV6,2/11.1')
            # Apple TV 4th Gen
            ua.append('AppleTV5,3/9.1.1')

        if "gameconsole" in devices:
            # Nintendo Wii U
            ua.append('Mozilla/5.0 (Nintendo WiiU) AppleWebKit/536.30 (KHTML, like Gecko) NX/3.0.4.2.12 NintendoBrowser/4.3.1.11264.US')
            # Xbox One S
            ua.append('Mozilla/5.0 (Windows NT 10.0; Win64; x64; XBOX_ONE_ED) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393')
            # Xbox One
            ua.append('Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586')
            # Playstation 4
            ua.append('Mozilla/5.0 (PlayStation 4 3.11) AppleWebKit/537.73 (KHTML, like Gecko)')
            # Playstation Vita
            ua.append('Mozilla/5.0 (PlayStation Vita 3.61) AppleWebKit/537.73 (KHTML, like Gecko) Silk/3.2')
            # Nintendo 3DS
            ua.append('Mozilla/5.0 (Nintendo 3DS; U; ; en) Version/1.7412.EU')

        if "bots" in devices:
            # Google bot
            ua.append('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')
            # Bing bot
            ua.append('Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)')
            # Yahoo! bot
            ua.append('Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')

        if "ereader" in devices:
            # Amazon Kindle 4
            ua.append('Mozilla/5.0 (X11; U; Linux armv7l like Android; en-us) AppleWebKit/531.2+ (KHTML, like Gecko) Version/5.0 Safari/533.2+ Kindle/3.0+')
            # Amazon Kindle 3
            ua.append('Mozilla/5.0 (Linux; U; en-US) AppleWebKit/528.5+ (KHTML, like Gecko, Safari/528.5+) Version/4.0 Kindle/3.0 (screen 600x800; rotate)')

        if len(ua) <= 0:
            ua.append('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36')

        self.__useragentList = ua
        return ua

    def setUserAgent(self, userAgent="", devices=[], exportHeader=False):
        ua = []
        if userAgent == "":
            ua.append(userAgent.strip())
        else:
            if len(devices) > 0:
                ua = self.getUserAgentList(devices)
            elif len(self.__useragentList) > 0:
                ua = self.__useragentList
            else:
                ua = self.getUserAgentList()

        uaTxt = ua[random.randint(0, len(ua)-1)]

        if exportHeader == True:
            return {
                'User-agent' : uaTxt
            }

        return uaTxt

    def discardProxy(self, proxy=""):
        if proxy.strip()=="":
            self.proxyList.clear()
        else:
            try:
                self.proxyList.remove(proxy)
            except:
                print("Proxy Not in List")

        if len(self.proxyList) <= 0:
            self.findProxies(limit=self.defaultProxyLimit)

        return self.proxyList

    def openBrowser(self, headless=False, browser="chrome"):
        self.browserOptions = Options()
        if headless:
            self.browserOptions.add_argument("--headless")

        browser = browser.strip().lower()

        if browser == "chrome":
            self.browser = webdriver.Chrome(options=self.browserOptions)
        else:
            self.browser = webdriver.Firefox(options=self.browserOptions)

        return self.browser

    def openNewTab(self, link) :
        self.browser.execute_script(f'window.open("{link}", "_blank")')
        self.sleepRandom()

    def openNewTab(self, link, browserInstance) :
        browserInstance.execute_script(f'window.open("{link}", "_blank")')
        self.sleepRandom()

    def closeTab(self) :
        self.browser.close()

    def closeTab(self, browserInstance) :
        browserInstance.close()

    def goToLink(self, link):
        self.browser.get(link)
        self.sleepRandom()

    def goToLink(self, link, browserInstance):
        browserInstance.get(link)
        self.sleepRandom()

    def closeBrowser(self):
        self.browser.quit()

    def closeBrowser(self, browserInstance):
        browserInstance.quit()

