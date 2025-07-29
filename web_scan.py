
import requests

def scan(url):
    findings = {"xss": False, "missing_headers": []}
    try:
        test_payload = "<script>alert(1)</script>"
        r = requests.get(f"{url}?q={test_payload}", timeout=5)
        if test_payload in r.text:
            findings["xss"] = True

        headers_to_check = ["X-Frame-Options", "X-Content-Type-Options"]
        for header in headers_to_check:
            if header not in r.headers:
                findings["missing_headers"].append(header)
    except Exception as e:
        findings["error"] = str(e)
    return findings
