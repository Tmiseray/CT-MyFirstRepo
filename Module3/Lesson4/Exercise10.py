
# Exercise 10: Formatting Log Files for Analysis
"""
Objective:
Develop a Python script to reformat entries in a log file for easier analysis, using the re.sub() function to standardize date formats and anonymize sensitive information.

Problem Statement:
You have a log file from a web server that contains various entries with timestamps and user emails. The timestamps are in different formats, and you need to standardize them. Additionally, for privacy concerns, you need to anonymize user email addresses in the log.

Instructions:
1. Read a string that represents log file entries.
2. Use re.sub() to standardize timestamp formats (e.g., convert "14/03/2022" to "2022-03-14")
3. Use re.sub() to replace email addresses with a placeholder text like "[ANONYMIZED]"
4. Handle any exceptions that might occur during the process.
5. Display the reformatted log entries.

Hints:
- Develop regex patterns to identify different timestamp formats and email addresses.
- Use re.sub() to replace identified patterns with standardized formats or placeholder text.
- Employ try-except blocks to manage any anomalies in the log entries.

"""

import re

def standardize_timestamps(log):
    # Standardize DD/MM/YYYY to YYYY-MM-DD
    log = re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\2-\1", log)
    return log

def anonymize_emails(log):
    log = re.sub(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", "[ANONYMIZED]", log)
    return log

def format_log(log_entries):
    try:
        log_entries = standardize_timestamps(log_entries)
        log_entries = anonymize_emails(log_entries)
        return log_entries
    except Exception as e:
        print(f"Error formatting log: {e}")
        return log_entries


log_data = """
    User [john.doe@example.com] accessed the system on 14/03/2022.
    User [jane.doe@domain.com] accessed the system on 15/03/2022.
"""

# Formatting and displaying the log data
formatted_log = format_log(log_data)
print(formatted_log)