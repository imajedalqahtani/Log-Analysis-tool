import re  # Used for pattern matching
from collections import defaultdict  # dictionary that auto-initializes values


# function to analyze log file
def analyze_logs(file_path):

    # Dictionary to store failed login counts per IP
    failed_logins = defaultdict(int)

    # open the log file in read mode
    with open(file_path, 'r') as file:

        # Read file line by line
        for line in file:

            # convert line to lowercase and check for "failed"
            if "failed" in line.lower():

                # extract IP address using regex pattern
                ip_match = re.search(r'\d+\.\d+\.\d+\.\d+', line)

                # If IP is found
                if ip_match:
                    ip = ip_match.group()  # Get actual IP string

                    # Increase count for this IP
                    failed_logins[ip] += 1

    print("\nSuspicious Activity Report:")

    # loop through all recorded IPs
    for ip, count in failed_logins.items():

        # If more than 3 failed attempts then suspicious
        if count > 3:
            print(f"IP {ip} → {count} failed attempts (SUSPICIOUS)")


# ask user for log file path
log_file = input("Enter log file path: ")

# Run analysis
analyze_logs(log_file)