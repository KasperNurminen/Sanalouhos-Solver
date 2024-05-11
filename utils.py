import datetime


def print_with_date(message: str, color_code="\033[94m") -> None:
    # Get the current time
    now = datetime.datetime.now()
    # Format the time to include only hours, minutes, and seconds
    time_str = now.strftime("%H:%M:%S")
    # Reset color to default after the message
    reset_code = "\033[0m"
    # Print the formatted time followed by the user's message
    print(f"{color_code}{time_str}{reset_code} {message}")
