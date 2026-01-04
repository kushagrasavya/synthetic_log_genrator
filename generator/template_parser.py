import re

SYSLOG_PATTERN = re.compile(
    r"^\[(.*?)\]\s+(.*?):\s+(.*)$"
)

def parse_log_line(line):
    match = SYSLOG_PATTERN.match(line)
    if not match:
        return None
    return {
        "timestamp": match.group(1),
        "source": match.group(2),
        "message": match.group(3)
    }
