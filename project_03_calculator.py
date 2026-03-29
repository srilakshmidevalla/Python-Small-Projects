# project_03_calculator.py
# Mini Project 3: Calculator with history
# Run: python 06_mini_projects/project_03_calculator.py

import math

history = []

def calculate(expression):
    """Safely evaluate a math expression."""
    # Allow only safe characters
    allowed = set("0123456789+-*/()., ")
    if not all(c in allowed for c in expression):
        return None, "Invalid characters in expression."
    try:
        result = eval(expression)
        return result, None
    except ZeroDivisionError:
        return None, "Cannot divide by zero!"
    except Exception:
        return None, "Invalid expression."

def show_history():
    if not history:
        print("No history yet.")
        return
    print("\n📜 HISTORY")
    for i, (expr, result) in enumerate(history[-10:], 1):
        print(f"  {i}. {expr} = {result}")

def special_operations():
    print("\n🔢 SPECIAL OPERATIONS")
    print("  sq  → Square root")
    print("  pow → Power (x^y)")
    print("  pct → Percentage")
    print("  back → Back to main")
    
    op = input("Operation: ").strip().lower()
    
    if op == "sq":
        n = float(input("Number: "))
        result = math.sqrt(n)
        print(f"√{n} = {result}")
        history.append((f"sqrt({n})", result))
    elif op == "pow":
        base = float(input("Base: "))
        exp = float(input("Exponent: "))
        result = base ** exp
        print(f"{base}^{exp} = {result}")
        history.append((f"{base}^{exp}", result))
    elif op == "pct":
        value = float(input("Value: "))
        pct = float(input("Percentage: "))
        result = (pct / 100) * value
        print(f"{pct}% of {value} = {result}")
        history.append((f"{pct}% of {value}", result))

def main():
    print("=" * 40)
    print("   🧮 PYTHON CALCULATOR")
    print("=" * 40)
    print("Type a math expression or a command:")
    print("  h → history | s → special | q → quit")
    print("Examples: 2+3, 10*5, (4+2)/3\n")

    while True:
        user_input = input(">>> ").strip().lower()

        if user_input == "q":
            print("👋 Bye!")
            break
        elif user_input == "h":
            show_history()
        elif user_input == "s":
            special_operations()
        elif user_input == "":
            continue
        else:
            result, error = calculate(user_input)
            if error:
                print(f"❌ {error}")
            else:
                print(f"= {result}")
                history.append((user_input, result))

if __name__ == "__main__":
    main()
