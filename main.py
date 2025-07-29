
import argparse
from modules import network_scan, web_scan, dir_enum, ssl_check, cms_detect, report

def main():
    parser = argparse.ArgumentParser(description="VulneraScan - CLI Vulnerability Scanner")
    parser.add_argument("--target", required=True, help="Target domain or IP")
    parser.add_argument("--network", action="store_true", help="Run network scan")
    parser.add_argument("--web", action="store_true", help="Run web vulnerability scan")
    parser.add_argument("--dir", action="store_true", help="Run directory brute force")
    parser.add_argument("--ssl", action="store_true", help="Run SSL/TLS check")
    parser.add_argument("--cms", action="store_true", help="Run CMS/Tech detection")
    parser.add_argument("--output", default="report.txt", help="Output report file")
    args = parser.parse_args()

    results = {"target": args.target}

    if args.network:
        print("[*] Running network scan...")
        results["network"] = network_scan.scan(args.target)

    if args.web:
        print("[*] Running web scan...")
        results["web"] = web_scan.scan(args.target)

    if args.dir:
        print("[*] Running directory enumeration...")
        results["dirs"] = dir_enum.scan(args.target)

    if args.ssl:
        print("[*] Checking SSL...")
        results["ssl"] = ssl_check.scan(args.target)

    if args.cms:
        print("[*] Detecting CMS...")
        results["cms"] = cms_detect.scan(args.target)

    print("[*] Writing report to:", args.output)
    report.generate(results, args.output)
    print("[+] Scan completed.")

if __name__ == "__main__":
    main()
