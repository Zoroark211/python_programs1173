import datetime
import pytz
import time

def display_current_time():
    while True:
        utc_time = datetime.datetime.utcnow()

        timezone = 'America/Los_Angeles'
        local_time = utc_time.astimezone(pytz.timezone(timezone))

        formatted_time = local_time.strftime("%I:%M:%S %p %Z")
        print(formatted_time)

        time.sleep(1)

if __name__ == "__main__":
    display_current_time()