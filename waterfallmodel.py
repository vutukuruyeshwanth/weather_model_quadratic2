print("=== WATERFALL MODE ===")
# Plan -> Develop -> Test -> Deliver (one cycle)
for hour in range(0, 25, 6):  # every 6 hours
    temp = quadratic_weather_model(hour)
    print(f"Time: {hour} hrs -> Predicted Temp: {temp:.2f}°C")
