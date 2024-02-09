import time
import winsound


def set_alarm():
    try:
        alarm_time = input("Enter the alarm time in HH:MM format: ")
        alarm_hour, alarm_minute = map(int, alarm_time.split(":"))
        return alarm_hour, alarm_minute
    except ValueError:
        print("Invalid time format. Please use HH:MM format.")
        return set_alarm()


def main():
    print("Welcome to the Python Alarm Clock!")

    alarm_hour, alarm_minute = set_alarm()

    while True:
        current_time = time.localtime()

        if current_time.tm_hour == alarm_hour and current_time.tm_min == alarm_minute:
            print("Time's up! Wake up!")
            winsound.Beep(1000, 1000)  # Beep sound for 1 second
            break

        time.sleep(30)  # Sleep for 30 seconds before checking again


if __name__ == "__main__":
    main()
