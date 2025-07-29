
import requests

def scan(url):
    try:
        r = requests.get(url, timeout=5)
        if "wp-content" in r.text:
            return "WordPress"
        elif "Joomla" in r.text:
            return "Joomla"
        return "Unknown"
    except:
        return "Detection Failed"
