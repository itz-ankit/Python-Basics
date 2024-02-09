import time
import winsound


def set_alarm():
    print("Enter the alarm time in HH:MM format:")
    alarm_time = input()
    return alarm_time


def validate_time(time_str):
    try:
        time.strptime(time_str, "%H:%M")
        return True
    except ValueError:
        return False


def play_alarm_sound():
    frequency = 2500  # Frequency of the sound (Hz)
    duration = 3000  # Duration of the sound (milliseconds)
    winsound.Beep(frequency, duration)


def main():
    print("Simple Alarm Clock")
    while True:
        alarm_time = set_alarm()
        if validate_time(alarm_time):
            break
        else:
            print("Invalid time format. Please use HH:MM format.")

    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            print("Time to wake up!")
            play_alarm_sound()
            break
        time.sleep(60)  # Check the time every 60 seconds


if __name__ == "__main__":
    main()
