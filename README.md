# CODTECH-Task2

Name- RAHUL KUMAR SINGH
Company: CODTECH IT SOLUTIONS
ID: CT08DS8558
Domain: CYBER SECURITY & ETHICAL HACKING
Duration: September 25, 2024 to October 25, 2024

#vulnerability scanning tool that scans a network or website
for common security vulnerabilities such as open ports, outdated software
versions, and misconfigurations#

Explanation of the Code:

1. Port Scanning:
The scan_ports function scans a specified range of ports (1-1024 in this case) on the target IP address or hostname. It uses the socket library to attempt to connect to each port and checks if it is open.

2. HTTP Header Check:
The check_http_headers function sends an HTTP GET request to the target URL and checks for the presence of common security headers. If any are missing, it adds them to a list of issues.

3. Software Version Check:
The check_software_version function is a placeholder. In a real-world scenario, you would implement logic to check the software version against a database of known vulnerabilities.

4. Main Function:
The main function prompts the user for a target IP address or URL, performs the port scan, checks HTTP headers, and calls the software version check.

Usage:
1. Run the script in a Python environment.
2. Enter the target IP address or URL when prompted.
3. The tool will output the results of the port scan, any HTTP header issues, and a placeholder message for software version checks.

![image](https://github.com/user-attachments/assets/2a598696-063a-4820-a820-48ca457dc06c)

