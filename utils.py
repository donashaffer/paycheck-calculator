from datetime import datetime

def parse_time_flexible(time_str):
    formats_to_try = [
        "%H%M",        # 0900
        "%I:%M %p",    # 9:00 AM
        "%I:%M%p",     # 9:00AM
        "%I %p",       # 9 AM
        "%I%p",        # 9AM
        "%H:%M",       # 09:00 (24-hour with colon)
    ]
    
    time_str = time_str.strip().upper()
    
    for fmt in formats_to_try:
        try:
            return datetime.strptime(time_str, fmt)
        except ValueError:
            continue
    
    return None  # none of the formats worked