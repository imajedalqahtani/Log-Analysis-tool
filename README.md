# Log Analysis Tool (Python)

## Project Overview
This project is a simple log analysis tool built in Python. It reads system log files and detects suspicious activities such as repeated failed login attempts.

The purpose of this project is to understand how security monitoring and incident detection work in real systems.

## How It Works
The program reads a log file line by line. It searches for failed login attempts and extracts IP addresses using pattern matching. It then counts how many times each IP appears and flags those with repeated failures.

## Features
- Reads and processes log files
- Detects failed login attempts
- Extracts IP addresses using regex
- Identifies suspicious IPs based on repeated failures

## Technologies Used
- Python
- File handling
- Regular expressions (regex)
- Data structures (dictionary)

## How to Run
1. Create or provide a log file (e.g. log.txt)
2. Run the script:
