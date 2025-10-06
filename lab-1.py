def utility(p_rain, u_rain, u_sun):
    return p_rain * u_rain + (1 - p_rain) * u_sun

def main():
    print("=== Decision evaluation: home or forest ===")

    print("Enter score for rain at home:")
    rain_home = float(input("> "))
    print("Enter score for sun at home:")
    sun_home = float(input("> "))
    print("Enter score for rain in forest:")
    rain_forest = float(input("> "))
    print("Enter score for sun in forest:")
    sun_forest = float(input("> "))

    print("Enter the probability of rain (0.0 ... 1.0):")
    p_rain = float(input("> "))
    p_sun = 1 - p_rain

    home = utility(p_rain, rain_home, sun_home)
    forest = utility(p_rain, rain_forest, sun_forest)

    print("\n--- Results ---")
    print(f"Probability of rain: {p_rain:.2f}, sun: {p_sun:.2f}")
    print(f"Utility home: {home:.2f}")
    print(f"Utility forest: {forest:.2f}")

    if home > forest:
        print("Recommendation: stay home")
    elif forest > home:
        print("Recommendation: go to the forest")
    else:
        print("Both options are equally good")

if __name__ == "__main__":
    main()
