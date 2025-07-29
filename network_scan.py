
import nmap

def scan(target):
    scanner = nmap.PortScanner()
    scanner.scan(target, arguments='-sV')
    results = {}
    if target in scanner.all_hosts():
        results['open_ports'] = []
        for proto in scanner[target].all_protocols():
            for port in scanner[target][proto]:
                service = scanner[target][proto][port]['name']
                version = scanner[target][proto][port].get('version', '')
                results['open_ports'].append(f"{port}/{proto} - {service} {version}")
    return results
