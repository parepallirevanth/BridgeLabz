# 13. Simulate Stopwatch Program
# a. Desc ­> Write a Stopwatch Program for measuring the time that elapses between
# the start and end clicks
# b. I/P ­> Start the Stopwatch and End the Stopwatch
# c. Logic ­> Measure the elapsed time between start and end
# d. O/P ­> Print the elapsed time.
# -------------------------------------------------------------------------------------

# importing time library
import time


# function takes sec as inputs and converts it into HH:MM:SS format
def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    # using format function printing HH:MM:SS
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours), int(mins), sec))


input("Press Enter to start")
# time function returns the number of seconds passed in epoch
start_time = time.time()
input("Press Enter to stop")
end_time = time.time()
# calculates elapsed time by finding the difference of end time and start time
time_lapsed = end_time - start_time
# calls the function to convert seconds to HH:MM:SS
time_convert(time_lapsed)
