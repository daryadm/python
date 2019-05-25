# Define a function that returns formatted minutes and seconds

###################################################
# Time formatting function
# Student should enter function on the next lines.
def convert_units(time, name):
    result = str(time) + " " + name
    if time > 1:
        result = result + "s"
    return result

def format_time(time):
    minutes = time // 60
    seconds = time - minutes * 60

    minutes_string = convert_units(minutes, "minute")
    seconds_string = convert_units(seconds, "second")

    if minutes == 0 and seconds == 0:
        return "Zero time left"
    elif minutes == 0:
        return seconds_string
    elif seconds == 0:
        return minutes_string
    else:
        return minutes_string + " and " + seconds_string




###################################################
# Tests

print format_time(23)
print format_time(1237)
print format_time(0)
print format_time(1860)

###################################################
# Output to console
#0 minutes and 23 seconds
#20 minutes and 37 seconds
#0 minutes and 0 seconds
#31 minutes and 0 seconds