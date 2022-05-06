class Chrome:
    #selenium get chrome driver

class RemoteFirefox:
    pass

class Browsers:

    @staticmethod
    def get_browser(browser):
        _browsers = {
            'chrome': Chrome,
            'remote_firefox': RemoteFirefox
        }

        return _browsers.get(browser)
