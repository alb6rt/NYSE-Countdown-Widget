import datetime;
import pytz;

# Calculates the time until next NYSE market open
# Returns a string
def countdown_status():
    # Fetch present new york time
    newyork_timezone = pytz.timezone('America/New_York');
    newyork_time = datetime.datetime.now(newyork_timezone);

    # Store NYSE open time in a variablew
    nyse_open = newyork_time.replace(hour = 9, minute = 30, second = 0, microsecond = 0);

    # Case for weekday and already past market open
    if (newyork_time.weekday() < 5 and newyork_time.time() >= nyse_open.time()):
        nyse_open += datetime.timedelta(days = 1);

    # Ensure that nyse_open is not on a weekend
    if (nyse_open.weekday() == 5):
        nyse_open += datetime.timedelta(days = 2);
    elif (nyse_open.weekday() == 6):
        nyse_open += datetime.timedelta(days = 1);

    # Calculate the difference between current newyork_time and next nyse_open time
    remaining_time = nyse_open - newyork_time;
    remaining_seconds = int(remaining_time.total_seconds());

    # Main logic
    # If market is open, return string saying that market is open
    # Else, return the remaining countdown until market is open
    if (
        newyork_time.weekday() < 5 
        and newyork_time.time() >= datetime.time(9, 30) 
        and newyork_time.time() < datetime.time(16, 0)
    ):
        return 'Market is open';
    else:
        hours = remaining_seconds // 3600;
        minutes = (remaining_seconds % 3600) // 60;
        seconds = remaining_seconds % 60;

        return f'Market opens in {hours:02}:{minutes:02}:{seconds:02}';