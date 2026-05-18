# Write function bmi that calculates body mass index (bmi = weight / height²).
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
# if bmi > 30 return "Obese"
def bmi(weight, height):
    bmi = weight / (height ** 2)
    return "Underweight" if bmi <= 18.5 else "Normal" if bmi <= 25 else "Overweight" if bmi <= 30 else "Obese"


if __name__ == "__main__":
    print(bmi(50, 1.80))  # Underweight
    print(bmi(100, 1.90))  # Overweight
    print(bmi(64, 1.45))  # Obese
