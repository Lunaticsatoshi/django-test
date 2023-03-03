def calculate_price(time, distance, pricing_config):
    time_multiplier_factor = (time *  pricing_config.time_multiplier_factor)/pricing_config.base_time
    total_price = (pricing_config.distance_base_price + (distance * pricing_config.distance_additional_price)) * time_multiplier_factor
    return total_price