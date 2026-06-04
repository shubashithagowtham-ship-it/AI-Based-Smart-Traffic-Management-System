def congestion_level(vehicle_count):
    if vehicle_count > 20:
        return "HIGH"
    elif vehicle_count > 10:
        return "MEDIUM"
    else:
        return "LOW"