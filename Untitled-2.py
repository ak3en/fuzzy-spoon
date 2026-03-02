import math

# Prompt and message variables
PROMPT_FIRST = "enter a number for function: "
PROMPT_SECOND = "enter a second number for function: "
INVALID_MSG = "Invalid input. Please enter numeric values."


def calculate_hypotenuse(a: float, b: float) -> float:
    """Return the hypotenuse for sides `a` and `b`."""
    return math.hypot(a, b)


def main() -> None:
    while True:
        try:
            first = input(PROMPT_FIRST)
            second = input(PROMPT_SECOND)
            a = float(first)
            b = float(second)
            hypotenuse = calculate_hypotenuse(a, b)
            print(f"result: {hypotenuse}")
        except ValueError:
            print(INVALID_MSG)
        except (KeyboardInterrupt, EOFError):
            print("Exiting.")
            break


if __name__ == "__main__":
    main()
