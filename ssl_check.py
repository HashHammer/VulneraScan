
import ssl
import socket

def scan(host):
    result = {}
    try:
        context = ssl.create_default_context()
        conn = context.wrap_socket(socket.socket(), server_hostname=host)
        conn.settimeout(3)
        conn.connect((host, 443))
        cert = conn.getpeercert()
        result["valid_till"] = cert.get("notAfter", "N/A")
    except Exception as e:
        result["error"] = str(e)
    return result
