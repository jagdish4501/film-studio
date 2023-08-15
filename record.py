import subprocess
import shlex

# List available windows/screens


def list_available_screens():
    try:
        process_list = subprocess.check_output(
            ['powershell', 'Get-Process | Where-Object {$_.mainWindowTitle} | Format-Table mainWindowtitle -AutoSize'], text=True)
        return process_list.strip().split('\n')[2:]  # Exclude table headers
    except subprocess.CalledProcessError:
        return []

# Ask user for screen choice by number


def choose_screen():
    available_screens = list_available_screens()
    if available_screens:
        print("Available Screens:")
        for i, screen in enumerate(available_screens, start=1):
            print(f"{i}. {screen}")

        choice_num = int(input(
            "Enter the number of the screen you want to capture (or 0 for entire desktop): "))
        if choice_num == 0:
            return "desktop"
        elif 1 <= choice_num <= len(available_screens):
            return available_screens[choice_num - 1]
        else:
            print("Invalid choice.")
            return None
    else:
        print("No screens found.")
        return None

# Record the chosen screen


def record_screen(screen_choice, output_filename):
    cleaned_screen_choice = screen_choice.strip()
    cmd = f'ffmpeg -f gdigrab -framerate 5 -i title="{cleaned_screen_choice}" "{output_filename}.mp4"'
    try:
        subprocess.run(cmd, shell=True)
    except KeyboardInterrupt:
        print("Recording stopped.")


# Main function


def main():
    screen_choice = choose_screen()
    if screen_choice:
        output_filename = input(
            "Enter the output filename (e.g., output.mp4): ")
        record_screen(screen_choice, output_filename)


if __name__ == "__main__":
    main()
