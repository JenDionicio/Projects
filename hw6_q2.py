"""
Author: Jen Martinez
Assignment / Part: HW6 - Q2 (depending on the file name)
Date due: 2022-10-20, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
import math

def get_decimal_time(hour, minute, second):
    # 60 * 60 --> 3600 * hours --> secs in hour
    # 60 * min --> secs in min 
    total_secs = hour*3600 + minute* 60 + second
    
    french_hours = total_secs // 10000
    french_minutes = (total_secs -  (french_hours*10000))//100
    french_secs = (total_secs - (french_hours*10000)) % 100

    return '{}:{}:{}'.format(french_hours, french_minutes, french_secs)


def get_decimal_date(g_month, day, g_year):

    if g_month == 1:
        french_revol = 'Nivôse'
    elif g_month == 2:
        french_revol = 'Pluviôse'
    elif g_month == 3:
        french_revol = 'Ventôse'
    elif g_month == 4:
        french_revol = 'Germinal'
    elif g_month == 5:
        french_revol = 'Floréal'
    elif g_month == 6:
        french_revol = 'Prairial'
    elif g_month == 7:
        french_revol = 'Messidor'
    elif g_month == 8:
        french_revol = 'Thermidor'
    elif g_month == 9:
        french_revol = 'Fructidor'
    elif g_month == 10:
        french_revol = 'Vendémiaire'
    elif g_month == 11:
        french_revol = 'Brumaire'
    elif g_month == 12:
        french_revol = 'Frimaire'

    year = int(math.fabs(g_year-1792))

    if day > 20:
        décade = 3 
    elif day > 10:
        décade = 2
    else:
        décade = 1


    return '{} {} Year {}, Décade {}'.format(day, french_revol, year, décade)

def get_french_datetime(string): # HR:MIN:SEC MONTH/DAY/YEAR
    
    split_s = string.split()
    military_time = split_s[0].split(':')
    gregorian_time = split_s[1].split('/')

    index = 0 
    while index < 3:
        military_time[index] = int(military_time[index])
        gregorian_time[index] = int(gregorian_time[index])
        index +=1

    hour = military_time[0]
    min = military_time[1]
    sec = military_time[2]

    g_month = gregorian_time[0]
    day = gregorian_time[1]
    g_year = gregorian_time[2]
    
    return '{}\n{}'.format(get_decimal_time(hour, min, sec), get_decimal_date(g_month, day, g_year))


def main():
    gregorian_datetime = "16:07:46 03/22/2022"
    french_datetime = get_french_datetime(gregorian_datetime)
    print(french_datetime)

main()
