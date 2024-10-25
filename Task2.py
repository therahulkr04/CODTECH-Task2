import socket
import requests
from urllib.parse import urlparse

def scan_ports(target, port_range):
    """Scan for open ports on the target."""
    open_ports = []
    for port in port_range:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout for the connection
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def check_http_headers(url):
    """Check HTTP headers for common security misconfigurations."""
    try:
        response = requests.get(url)
        headers = response.headers
        issues = []

        # Check for security headers
        if 'X-Content-Type-Options' not in headers:
            issues.append("Missing X-Content-Type-Options header.")
        if 'X-Frame-Options' not in headers:
            issues.append("Missing X-Frame-Options header.")
        if 'X-XSS-Protection' not in headers:
            issues.append("Missing X-XSS-Protection header.")
        if 'Strict-Transport-Security' not in headers:
            issues.append("Missing Strict-Transport-Security header.")
        
        return issues
    except requests.RequestException as e:
        return [f"Error accessing {url}: {str(e)}"]

def check_software_version(target):
    """Check for outdated software versions (placeholder)."""
    # This is a placeholder function. In a real implementation, you would
    # check the software version against a known database of vulnerabilities.
    # For demonstration, we will just return a static message.
    return ["Software version check is not implemented."]

def main():
    target = input("Enter the target IP address or URL: ")
    port_range = range(1, 1025)  # Scanning ports 1-1024

    # Port scanning
    print(f"Scanning ports on {target}...")
    open_ports = scan_ports(target, port_range)
    if open_ports:
        print(f"Open ports: {', '.join(map(str, open_ports))}")
    else:
        print("No open ports found.")

    # HTTP header check (if the target is a URL)
    if urlparse(target).scheme in ['http', 'https']:
        print(f"Checking HTTP headers for {target}...")
        issues = check_http_headers(target)
        if issues:
            print("Security issues found in HTTP headers:")
            for issue in issues:
                print(f"- {issue}")
        else:
            print("No security issues found in HTTP headers.")

    # Software version check (placeholder)
    print(f"Checking software versions for {target}...")
    version_issues = check_software_version(target)
    for issue in version_issues:
        print(issue)

if __name__ == "__main__":
    main()
