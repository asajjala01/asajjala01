import re
import sys
from collections import defaultdict
from datetime import datetime

def parse_log_line(line):
    """
    Parses a single log line and extracts key fields.
    Returns a dictionary of extracted values or None if line doesn't match.
    """
    pattern = r'(\d+\.\d+\.\d+\.\d+).*\[(.+?)\].*"(\w+)\s+(\S+)\s+HTTP/\d+\.\d+"\s+(\d+)\s+(\d+)'
    
    match = re.match(pattern, line)
    
    if not match:
        return None
    
    return {
        "ip": match.group(1),
        "timestamp": match.group(2),
        "method": match.group(3),
        "endpoint": match.group(4),
        "status": int(match.group(5)),
        "size": int(match.group(6))
    }