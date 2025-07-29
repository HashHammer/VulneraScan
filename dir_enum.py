
import requests

def scan(url, wordlist='modules/common.txt'):
    found = []
    try:
        with open(wordlist) as f:
            for line in f:
                path = line.strip()
                full_url = f"{url.rstrip('/')}/{path}"
                try:
                    r = requests.get(full_url, timeout=3)
                    if r.status_code in [200, 301, 302]:
                        found.append(full_url)
                except:
                    continue
    except Exception as e:
        found.append(f"Error: {e}")
    return found
