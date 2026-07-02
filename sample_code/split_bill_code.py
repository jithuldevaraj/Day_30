def split_bill():
    print("--- Welcome to the Bill Splitter ---")

    try:
        # 1. TRY: The "risky" operations
        # We try to convert the input into numbers and do the math
        total_bill = float(input("How much is the total bill? $"))
        num_people = int(input("How many people are splitting it? "))

        cost_per_person = total_bill / num_people

    except ValueError:
        # 2. EXCEPT: Catching Typos
        # Triggers if the user types "fifty" instead of "50"
        print("\nError: Please enter numbers only. No letters or symbols.")

    except ZeroDivisionError:
        # 3. EXCEPT: Catching impossible math
        # Triggers if the user says 0 people are splitting the bill
        print("\nError: You cannot split a bill with 0 people!")

    else:
        # 4. ELSE: The Happy Path
        # Runs ONLY if the user typed valid numbers and the math worked
        print(f"\nSuccess! Each person owes: ${cost_per_person:.2f}")

    finally:
        # 5. FINALLY: The Cleanup
        # Runs EVERY time, whether it succeeded or an error popped up
        print("--- Thank you for using the Bill Splitter! ---\n")


# Let's run the program
split_bill()