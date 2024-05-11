'''
    CS 5001
    Lab 1
    Exercise 4
    Name: Tianyuan Yan
'''

'''
Write a Python program to solve the general version of the problem below. Ask the user for the time now (in hours),
and ask for the number of hours to wait. Your program should output what the time will be on the clock when the
alarm goes off.

You look at the clock and it is exactly 11am. You set an alarm to go off in 51 hours.
At what time does the alarm go off?

You may assume military time, so 1pm is 13:00 hours. Here is some example output:

What time is it? 23
How long until your alarm expires? 4
Your alarm will expire at 3.
'''


def main():
    curr_time = int(input('What time is it?'))  # get current time
    duration = int(input('How long until your alarm expires?'))  # get interval
    if 0 <= curr_time <= 24 and duration >= 0:  # set the conditions for continuing
        total_time = curr_time + duration
        alarm = total_time % 24  # get final time on the clock

        print(f'Your alarm will expire at {alarm}')  # print answer
    else:
        print('Invalid input')  # when user inputs invalid data


if __name__ == '__main__':
    main()
