
def main():
    # Lists to store ages
    female_ages = []
    male_ages = []

    print("This program calculates the average age by gender.")
   
    # Ask how many people to input
    num_people = get_valid_int("How many people do you want to enter? ")

    # Main input loop
    for i in range(num_people):
        print(f"\n--- Person {i + 1} ---")
        age = get_valid_int("Age: ")
        gender = get_valid_gender("Gender (m/f): ")

        if gender == 'f':
            female_ages.append(age)
        elif gender == 'm':
            male_ages.append(age)

    # Calculate averages
    avg_female = calculate_average(female_ages)
    avg_male = calculate_average(male_ages)

    # Display results
    print("\n Results:")
    if avg_female is not None:
        print(f"Average age of women: {avg_female:.2f}")
    else:
        print("No data for women.")

    if avg_male is not None:
        print(f"Average age of men: {avg_male:.2f}")
    else:
        print("No data for men.")


def get_valid_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print(" Please enter a valid number.")

def get_valid_gender(prompt):
    """Prompt user until they give a valid gender: 'm' or 'f'."""
    while True:
        gender = input(prompt).lower()
        if gender in ['m', 'f']:
            return gender
        else:
            print("Please enter 'm' for male or 'f' for female.")

def calculate_average(age_list):
    """Return the average age from a list of ages, or None if empty."""
    if len(age_list) == 0:
        return None
    return sum(age_list) / len(age_list)


if __name__ == "__main__":
    main()
