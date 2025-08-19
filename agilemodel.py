print("\n=== AGILE MODE ===")
# Quick sprints, immediate feedback
times_to_check = [0, 6, 12, 18, 24]
for sprint in range(1, 3):
    print(f"Sprint {sprint}:")
    for t in times_to_check:
        temp = quadratic_weather_model(t)
        print(f"Time: {t} hrs -> Temp: {temp:.2f}°C")
    print("---")
