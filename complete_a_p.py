print("=" * 50)
print("     SMART ARITHMETIC PROGRESSION (AP) SOLVER     ")
print("=" * 50)

while True:
    try:
        print("\n--- Welcome to Smart AP Solver ---")
        print("This tool helps you solve Arithmetic Progression problems easily.")
        print("You can find sequences, sums, last terms, and more!")
        print("What information do you have?")
        print("1. First Term (a), Common Difference (d), and Number of Terms (n)")
        print("2. Two Terms and their positions (to find 'a' and 'd')")
        print("3. First Term (a), Last Term (l), and Number of Terms (n)")
        print("4. First Term (a), Common Difference (d), and Last Term (l) -> [Find n]")
        print("5. [AUTO] First Term, Second Term, and Last Term (Finds everything!)")
        print("6. Exit Program")

        choice = input("\nEnter your choice (1, 2, 3, 4, 5, or 6): ")

        if choice == "1":
            print("\n--- Enter Known Values ---")
            a = float(input("Enter the starting number (a): "))
            d = float(input("Enter the common difference (d): "))
            n = int(input("Enter the number of terms (n): "))
            if n < 1:
                raise ValueError("The number of terms must be positive.")
            sequence = [a + (i * d) for i in range(n)]
            last_term = a + (n - 1) * d
            total_sum = (n / 2) * (2 * a + (n - 1) * d)

        elif choice == "2":
            print("\n--- Enter Two Known Terms ---")
            term1 = float(input("Enter the first known term value: "))
            pos1 = int(input("Enter its position (e.g., 3 for 3rd term): "))
            term2 = float(input("Enter the second known term value: "))
            pos2 = int(input("Enter its position (e.g., 7 for 7th term): "))
            if pos1 < 1 or pos2 < 1 or pos1 == pos2:
                raise ValueError("Positions must be positive and distinct.")
            d = (term2 - term1) / (pos2 - pos1)
            a = term1 - (pos1 - 1) * d
            n = int(input("\nHow many total terms (n) do you want to generate/sum? "))
            if n < 1:
                raise ValueError("The number of terms must be positive.")
            sequence = [a + (i * d) for i in range(n)]
            last_term = a + (n - 1) * d
            total_sum = (n / 2) * (2 * a + (n - 1) * d)
            print(f"\n[Auto-Calculated: a = {a}, d = {d}]")

        elif choice == "3":
            print("\n--- Enter First Term, Last Term, and Total Terms ---")
            a = float(input("Enter the first term (a): "))
            last_term = float(input("Enter the last term (l): "))
            n = int(input("Enter the number of terms (n): "))
            if n < 1:
                raise ValueError("The number of terms must be positive.")
            if n == 1 and last_term != a:
                raise ValueError("For one term, the first and last terms must match.")
            d = (last_term - a) / (n - 1) if n > 1 else 0
            sequence = [a + (i * d) for i in range(n)]
            total_sum = (n / 2) * (a + last_term)
            print(f"\n[Auto-Calculated Common Difference (d) = {d}]")

        elif choice == "4":
            print("\n--- Enter First Term, Common Difference, and Last Term ---")
            a = float(input("Enter the first term (a): "))
            d = float(input("Enter the common difference (d): "))
            last_term = float(input("Enter the last term (l): "))
            if d == 0:
                if last_term != a:
                    raise ValueError("With a zero common difference, the last term must equal the first.")
                n = 1
            else:
                steps = (last_term - a) / d
                if steps < 0 or not steps.is_integer():
                    raise ValueError("The last term is not at a valid position in this progression.")
                n = int(steps) + 1
            sequence = [a + (i * d) for i in range(n)]
            total_sum = (n / 2) * (a + last_term)
            print(f"\n[Auto-Calculated Number of Terms (n) = {n}]")

        elif choice == "5":
            print("\n--- Enter Raw Problem Details ---")
            a = float(input("Enter the 1st term (from the sequence): "))
            second_term = float(input("Enter the 2nd term (to find difference): "))
            last_term = float(input("Enter the last term: "))
            d = second_term - a
            if d == 0:
                if last_term != a:
                    raise ValueError("With a zero common difference, the last term must equal the first.")
                n = 1
            else:
                steps = (last_term - a) / d
                if steps < 0 or not steps.is_integer():
                    raise ValueError("The last term is not at a valid position in this progression.")
                n = int(steps) + 1
            sequence = [a + (i * d) for i in range(n)]
            total_sum = (n / 2) * (a + last_term)
            print(f"\n[AI Auto-Calculated: d = {d}, n = {n}]")

        elif choice == "6":
            print("\nThank you for using Smart AP Solver. Keep practicing! Goodbye!")
            break

        else:
            print("\nInvalid choice! Please select 1, 2, 3, 4, 5, or 6.")
            continue

        print("\n" + "=" * 50)
        print("                   RESULTS               ")
        print("=" * 50)
        print(f"Number of terms (n): {n}")
        print(f"Common difference(d): {d}")
        print(f"Full AP Sequence   : {sequence}")
        print(f"Sum of all terms   : {total_sum}")
        print("=" * 50)

    except ZeroDivisionError:
        print("\n❌ Math Error: Division by zero (check positions or common difference).")
    except ValueError:
        print("\n❌ Input Error: Please enter valid numbers only!")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")

    cont = input("\nWould you like to solve another problem? (y/n): ").strip().lower()
    if cont != "y":
        print("\nThank you for using Smart AP Solver. Goodbye!")
        break