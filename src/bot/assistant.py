import random
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote import webelement
from selenium.webdriver.common.by import By


class _Colors:
    RED_BOLD = "\033[1;31m"
    RED = "\033[0;31m"
    WHITE = "\033[0;37m"
    GREEN = "\033[0;32m"



class Devices:
    ANDROID = "android"
    IPHONE = "iphone"
    WINDOWS = "windows"
    TABLET = "tablet"
    DESKTOP = "desktop"
    SETUPBOX = "setupbox"
    GAMECONSOLE = "gameconsole"
    BOTS = "bots"
    EREADER = "ereader"


class Browsers:
    CHROME = "Chrome"
    FIREFOX = "Firefox"


class botAssistant:
    """
    Bot Assistant Module to seamlessly create bots and webscrappers with advanced controls
    """

    def __init__(self, printLogs: bool = True, debugMode: bool = False) -> None:
        """
        Creates a new instance of the bot assistant.

        :Args:
         - printLogs - If Logs and Warnings are to be printed ot not. If the default is used it prints all logs
         - debugMode - If the bot should raise Errors. Errors are raised if debugMode is true, otherwise Errors are handled automatically
        """
        self.__useragentList = []
        self.sleepRandom_minTime = 4
        self.sleepRandom_maxTime = 15
        self.printLogs = printLogs
        self.browser = None
        self.debugMode = debugMode
        self.randomisedWaiting = True

    def _showError(self, errorMessage: str, exception: Exception) -> None:
        self._printLogs(errorMessage, color=_Colors.RED_BOLD)

        if self.debugMode:
            print(_Colors.RED, end="")
            print(exception)
            raise exception

        print(_Colors.WHITE, end="")

    def _printLogs(self, logs: str, color: _Colors = _Colors.GREEN) -> None:
        if self.printLogs:
            print(color+logs)
        print(_Colors.WHITE, end="")

    def calculateTimeInSeconds(self, hours: int = 0, minutes: int = 0, seconds: int = 0, days: int = 0, weeks: int = 0, months: int = 0, years: int = 0) -> int:
        return (hours * 60 * 60) + (minutes * 60) + (seconds) + (days*60*60*24) + (weeks*60*60*24*7) + (months*60*60*24*30) + (years*60*60*24*365)

    def calculateTimeInMs(self, hours: int = 0, minutes: int = 0, seconds: int = 0, days: int = 0, weeks: int = 0, months: int = 0, years: int = 0, milliSec: int = 0) -> int:
        return (self.calculateTimeInSeconds(hours=hours, minutes=minutes, seconds=seconds, days=days, months=months, weeks=weeks, years=years) * 1000) + milliSec

    def sleepRandom(self, min: int = -1, max: int = -1) -> None:

        try:
            if min < 0:
                min = self.sleepRandom_minTime

            if max < 0:
                max = self.sleepRandom_maxTime

            if max < min:
                max = min

            val = random.randint(min, max) + (random.randint(11, 99) / 100)

            self._printLogs("Waiting for " + str(val) + " seconds")

            time.sleep(val)
            # self.browser.implicitly_wait(val)

        except Exception as e:
            self._showError("Unable to sleep", e)

    def getUserAgentList(self, devices: list = []) -> list:
        ua = []
        if len(devices) <= 0:
            devices.append(Devices.ANDROID)
            devices.append(Devices.IPHONE)
            devices.append(Devices.WINDOWS)
            devices.append(Devices.TABLET)
            devices.append(Devices.DESKTOP)
            devices.append(Devices.SETUPBOX)
            devices.append(Devices.GAMECONSOLE)
            devices.append(Devices.BOTS)
            devices.append(Devices.EREADER)

        if Devices.ANDROID in devices:
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

        if Devices.IPHONE in devices:
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

        if Devices.WINDOWS in devices:
            # Microsoft Lumia 650
            ua.append('Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254')
            # Microsoft Lumia 550
            ua.append('Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536')
            # Microsoft Lumia 950
            ua.append('Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058')

        if Devices.TABLET in devices:
            # Google Pixel C
            ua.append('Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36')
            # Sony Xperia Z4 Tablet
            ua.append('Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36')
            # Nvidia Shield Tablet K1
            ua.append('Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36')
            # Samsung Galaxy Tab S3
            ua.append(
                'Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36')
            # Samsung Galaxy Tab A
            ua.append('Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36')
            # Amazon Kindle Fire HDX 7
            ua.append('Mozilla/5.0 (Linux; Android 4.4.3; KFTHWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/47.1.79 like Chrome/47.0.2526.80 Safari/537.36')
            # LG G Pad 7.0
            ua.append('Mozilla/5.0 (Linux; Android 5.0.2; LG-V410/V41020c Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/34.0.1847.118 Safari/537.36')

        if Devices.DESKTOP in devices:
            # Windows 10-based PC using Edge browser
            ua.append(
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246')
            # Chrome OS-based laptop using Chrome browser (Chromebook)
            ua.append(
                'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36')
            # Mac OS X-based computer using a Safari browser
            ua.append(
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9')
            # Windows 7-based PC using a Chrome browser
            ua.append(
                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36')
            # Linux-based PC using a Firefox browser
            ua.append(
                'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1')

        if Devices.SETUPBOX in devices:
            # Chromecast
            ua.append(
                'Mozilla/5.0 (CrKey armv7l 1.5.16041) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.0 Safari/537.36')
            # Roku Ultra
            ua.append('Roku4640X/DVP-7.70 (297.70E04154A)')
            # Minix NEO X5
            ua.append('Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30')
            # Amazon 4K Fire TV
            ua.append('Mozilla/5.0 (Linux; Android 5.1; AFTS Build/LMY47O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/41.99900.2250.0242 Safari/537.36')
            # Google Nexus Player
            ua.append(
                'Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T)')
            # Apple TV 5th Gen 4K
            ua.append('AppleTV6,2/11.1')
            # Apple TV 4th Gen
            ua.append('AppleTV5,3/9.1.1')

        if Devices.GAMECONSOLE in devices:
            # Nintendo Wii U
            ua.append(
                'Mozilla/5.0 (Nintendo WiiU) AppleWebKit/536.30 (KHTML, like Gecko) NX/3.0.4.2.12 NintendoBrowser/4.3.1.11264.US')
            # Xbox One S
            ua.append('Mozilla/5.0 (Windows NT 10.0; Win64; x64; XBOX_ONE_ED) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393')
            # Xbox One
            ua.append('Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586')
            # Playstation 4
            ua.append(
                'Mozilla/5.0 (PlayStation 4 3.11) AppleWebKit/537.73 (KHTML, like Gecko)')
            # Playstation Vita
            ua.append(
                'Mozilla/5.0 (PlayStation Vita 3.61) AppleWebKit/537.73 (KHTML, like Gecko) Silk/3.2')
            # Nintendo 3DS
            ua.append('Mozilla/5.0 (Nintendo 3DS; U; ; en) Version/1.7412.EU')

        if Devices.BOTS in devices:
            # Google bot
            ua.append(
                'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')
            # Bing bot
            ua.append(
                'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)')
            # Yahoo! bot
            ua.append(
                'Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')

        if Devices.EREADER in devices:
            # Amazon Kindle 4
            ua.append('Mozilla/5.0 (X11; U; Linux armv7l like Android; en-us) AppleWebKit/531.2+ (KHTML, like Gecko) Version/5.0 Safari/533.2+ Kindle/3.0+')
            # Amazon Kindle 3
            ua.append('Mozilla/5.0 (Linux; U; en-US) AppleWebKit/528.5+ (KHTML, like Gecko, Safari/528.5+) Version/4.0 Kindle/3.0 (screen 600x800; rotate)')

        if len(ua) <= 0:
            ua.append(
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36')

        self.__useragentList = ua
        return ua

    def setUserAgent(self, userAgent: str = None, devices: list = [], exportHeader: bool = False):
        ua = []
        if userAgent != None:
            ua.append(userAgent.strip())
        else:
            if len(devices) > 0:
                ua = self.getUserAgentList(devices)
            elif len(self.__useragentList) > 0:
                ua = self.__useragentList
            else:
                ua = self.getUserAgentList()

        uaTxt = ua[random.randint(0, len(ua)-1)]

        if exportHeader:
            return {'User-agent': uaTxt}

        return uaTxt

    def openBrowser(self, headless: bool = False, browser: Browsers = Browsers.CHROME, driverExecutablePath: str = None) -> None:
        self.browserOptions = Options()
        if headless:
            self.browserOptions.add_argument("--headless")

        try:
            if browser == Browsers.CHROME:
                if driverExecutablePath == None:
                    self.browser = webdriver.Chrome(
                        options=self.browserOptions)
                else:
                    self.browser = webdriver.Chrome(
                        options=self.browserOptions, executable_path=driverExecutablePath)

            elif browser == Browsers.FIREFOX:
                if driverExecutablePath == None:
                    self.browser = webdriver.Firefox(
                        options=self.browserOptions)
                else:
                    self.browser = webdriver.Firefox(
                        options=self.browserOptions, executable_path=driverExecutablePath)
            else:
                self._showError("Invalid Browser. Browser counld not be identified", TypeError(
                    "Browser provided is not of class Browsers"))

            self._printLogs(f"{browser} Browser Opened")
        except Exception as e:
            self._showError("Unable to open Browser", e)

    def openNewTab(self, link: str) -> bool:
        try:
            self.browser.execute_script(f'window.open("{link}", "_blank")')

            self._printLogs(f"New Tab Opened with link: {link}")

            if self.randomisedWaiting:
                self.sleepRandom()
            self.browser.window_handles

            return True

        except Exception as e:
            self._showError("Unable to Open New Tab", e)
            return False

    def closeTab(self, tabNo: int = None) -> bool:
        try:
            if tabNo == None:
                self.browser.close()
                self._printLogs("Tab Closed")
                return True
            else:
                self.switchToTab(tabNo=tabNo)
                if self.randomisedWaiting:
                    self.sleepRandom(1, 1)
                return self.closeTab()
        except Exception as e:
            self._showError("Unable to close Tab", e)
            return False

    def switchToTab(self, tabNo: int = 1) -> bool:
        if tabNo <= 0:
            tabNo = 1

        try:
            if len(self.browser.window_handles) < tabNo:
                self._showError("No Tab Found", ValueError(
                    "Invalid tabNo passed as argument. Tab doesn't exist"))
                return False

            self.browser.switch_to.window(
                window_name=self.browser.window_handles[tabNo-1])

            self._printLogs(f"Switched to tab {tabNo}")

        except Exception as e:
            self._showError(f"Cannot switch to tab {tabNo}", e)

    def goToLink(self, link: str) -> bool:

        try:
            self.browser.get(link)
            self._printLogs(f"Link opened in Browser: {link}")
            if self.randomisedWaiting:
                self.sleepRandom()

            return True
        except Exception as e:
            self._showError(f"Unable to open link: {link}", e)
            return False

    def closeBrowser(self) -> bool:
        try:
            self.browser.quit()
            self._printLogs("Browser Closed")
        except Exception as e:
            self._showError("Unable to close browser", e)

    def typeKeys(self, text: str, element: webelement) -> None:
        temp_logs = self.printLogs
        temp_debug = self.debugMode
        self.printLogs = False
        self.debugMode = False
        for c in text:
            element.send_keys(c)
            self.sleepRandom(0,1)
        
        self.printLogs = temp_logs
        self.debugMode = temp_debug