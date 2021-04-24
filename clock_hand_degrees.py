""" The hardest part of this problem is realizing the hour hand moves 0.5 degrees every minute.
There are 360 degress in a circle so that is a good place to start.

This program always returns the minimun clock hands angle.

degrees_in_circle = 360
degrees_in_hour = degrees_in_circle / 12 = 30
degreess_in_min = degrees_in_circle / (60 * 12) = 6
hour_hand_movement = 15 / 30 = 0.5
"""
import math

def hour_degrees_from_noon(h):
    return h * 30

def hour_hand_adjust(m):
    return m * 0.5

def minute_degrees_from_noon(m):
    return m * 6

def get_clock_hand_angle(h,m):
   angle = 360 - abs((hour_degrees_from_noon(h) + hour_hand_adjust(m) - minute_degrees_from_noon(m)))
   return math.ceil(min(360-angle,angle))

def get_times_when_angle_is_zero():

    for h in range(1,13):
        for m in range(60):
            if get_clock_hand_angle(h,m) <= 3:  
                print('angle = 0 at ',h,':',m)
                break 

get_times_when_angle_is_zero()

print('12:15 ', get_clock_hand_angle(12,15))
print('3:00 ', get_clock_hand_angle(3,0))
print('9:15 ', get_clock_hand_angle(9,15))
print('9:00 ', get_clock_hand_angle(9,0))
print('9:01 ', get_clock_hand_angle(9,1))
print('6:00 ', get_clock_hand_angle(6,0))
print('6:01 ', get_clock_hand_angle(6,1))
print('6:40 ', get_clock_hand_angle(6,40))
print('3:45 ', get_clock_hand_angle(3,45))
print('12:00 ', get_clock_hand_angle(12,0))
print('6:45 ', get_clock_hand_angle(6,45))
print('12:30 ', get_clock_hand_angle(12,30))

