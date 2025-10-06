options = {
    "Corporation 1": {
        "success": {"prob": 0.6, "profit": 8},
        "failure": {"prob": 0.4, "profit": -0.5}
    },
    "Corporation 2": {
        "success": {"prob": 0.7, "profit": 12},
        "failure": {"prob": 0.3, "profit": -0.5}
    },
    "Association": {
        "success": {"prob": 0.3, "profit": 25},
        "failure": {"prob": 0.7, "profit": -1}
    }
}

expected_values = {}
for option, data in options.items():
    
    E_success = data["success"]["prob"] * data["success"]["profit"]
    E_failure = data["failure"]["prob"] * data["failure"]["profit"]
    E_total = E_success + E_failure
    
    expected_values[option] = E_total
    
    print(f"{option}:")
    print(f"  Success: {E_success:.2f}")
    print(f"  Failure: {E_failure:.2f}")
    print(f"  Expected profit: {E_total:.2f}\n")

best_option = None
best_value = -float("inf")

for option, value in expected_values.items():
    if value > best_value:
        best_value = value
        best_option = option

print(f"The best option for the firm: {best_option}")
print(f"Expected profit: {best_value:.2f} million UAH")
