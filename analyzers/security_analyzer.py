def analyze_security_protocol(protocol: str) -> str:
    if protocol == "Open":
        get_warning("Open")
        return "Terrible"
    elif protocol == "WEP":
        get_warning("WEP")
        return "Bad"
    elif protocol == "WPA":
        get_warning("WPA")
        return "Not Safe"
    elif protocol == "WPA2":
        return "Safe"
    elif protocol == "WPA3":
        return "Excellent"
    else:
        return "Network uses unknown encryption" 

def get_warning(protocol: str) -> None:
    if protocol == "Open":
        print(f"Warning: {protocol} is a really dangerous one because it uses no encryption.")
    elif protocol == "WEP":
        print(f"Warning: {protocol} is a really dangerous one because it uses a weak encryption.")
    elif protocol == "WPA":
        print(f"Warning: {protocol} is a really dangerous one because it uses an old encryption standard.")
        
