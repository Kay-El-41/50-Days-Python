import winsound
import datetime

com_time = datetime.datetime.now()
current_time = com_time.strftime("%H:%M")


def alarm():
    user_hour = input("Enter hour: ")
    user_minute = input("Enter minute: ")
    user_time = f"{user_hour}:{user_minute}"

    print(f"Alarm will go off at {user_hour}:{user_minute}")

    if current_time == user_time:
        winsound.PlaySound("SystemAsterisk", winsound.SND_LOOP)


alarm()