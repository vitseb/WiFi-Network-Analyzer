def get_quality(rssi):
    if rssi < -30 and rssi > -70 :
        return "Excellent"
    elif rssi < -71 and rssi > -80 :
        return "Good"
    elif rssi < -81 and rssi > -90 :
        return "Fair"
    else:
        return "Weak"

if __name__ == "__main__":
    rssi = -65
    print("Signal strength is " + get_quality(rssi))