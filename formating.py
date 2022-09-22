
import os
import math
import pandas as pd
import numpy as np
from statistics import harmonic_mean


from IPython.display import display, Markdown, Latex

#   <  bold  >
#   <  underline  >
#   <  strike  >
#   <  hr (HUMAN READABLE)  >
#   <  percent  >

def get_formating():
    print(
        '''
from formating import bold, underline, strike, hr, percent
        '''
    )

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<  BOLD  >~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def bold(text):
    result = '\033[1m' + text + '\033[0m'
    return result


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<  UNDERLINE  >~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def underline(text):
    result = ''
    for c in text:
        result = result + c + '\u0332'
    return result

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<  STRIKE  >~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<  HR (HUMAN READABLE)  >~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def hr(n, suffix='', places=2, prefix='$'):
    '''
    Return a human friendly approximation of n, using SI prefixes

    '''
    prefixes = ['','K','M','B','T']
    
    # if n <= 99_999:
    #     base, step, limit = 10, 4, 100
    # else:
    #     base, step, limit = 10, 3, 100

    base, step, limit = 10, 3, 100

    if n == 0:
        magnitude = 0 #cannot take log(0)
    else:
        magnitude = math.log(n, base)

    order = int(round(magnitude)) // step
    return '%s%.1f %s%s' % (prefix, float(n)/base**(order*step), \
    prefixes[order], suffix)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<  Percent  >~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

class percent(float):
    def __str__(self):
        return '{:.2%}'.format(self)
    def __repr__(self):
        return '{:.2%}'.format(self)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<  FLAT  >~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# class flat(pandas.core.frame.DataFrame):
#     def __repr__(self):
#         return ['_'.join(column) for column in self.columns.to_flat_index()]

def flat(df):
    
    df.columns = ['_'.join(column) for column in df.columns.to_flat_index()]
        
    return df

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<  dtf  >~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def dtf():
    '''
    Displays the DateTime Formating info in Markdown
    '''
    display(Markdown('''# DateTime Formating Guide<br>
|Directive|Meaning|Example|Notes|
|:-------:|:------|:------|:----|
|%a|Weekday as locale’s abbreviated name.|Sun, Mon, …, Sat (en_US);So, Mo, …, Sa (de_DE)|(1)|
|%A|Weekday as locale’s full name.|Sunday, Monday, …, Saturday (en_US);Sonntag, Montag, …, Samstag (de_DE)|(1)|
|%w|Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.|0, 1, …, 6|
|%d|Day of the month as a zero-padded decimal number.|01, 02, …, 31|(9)|
|%b|Month as locale’s abbreviated name.|Jan, Feb, …, Dec (en_US) ;Jan, Feb, …, Dez (de_DE)|(1)|
|%B|Month as locale’s full name.|January, February, …, December (en_US); Januar, Februar, …, Dezember (de_DE)|(1)|
|%m|Month as a zero-padded decimal number.|01, 02, …, 12|(9)|
|%y|Year without century as a zero-padded decimal number.|00, 01, …, 99|(9)|
|%Y|Year with century as a decimal number.|0001, 0002, …, 2013, 2014, …, 9998, 9999|(2)|
|%H|Hour (24-hour clock) as a zero-padded decimal number.|00, 01, …, 23|(9)|
|%I|Hour (12-hour clock) as a zero-padded decimal number.|01, 02, …, 12|(9)|
|%p|Locale’s equivalent of either AM or PM.|AM, PM (en_US); am, pm (de_DE)|(1), (3)|
|%M|Minute as a zero-padded decimal number.|00, 01, …, 59|(9)|
|%S|Second as a zero-padded decimal number.|00, 01, …, 59|(4), (9)|
|%f|Microsecond as a decimal number, zero-padded to 6 digits.|000000, 000001, …, 999999|(5)|
|%z|UTC offset in the form ±HHMM[SS[.ffffff]] (empty string if the object is naive).|(empty), +0000, -0400, +1030, +063415, -030712.345216|(6)|
|%Z|Time zone name (empty string if the object is naive).|(empty), UTC, GMT|(6)|
|%j|Day of the year as a zero-padded decimal number.|001, 002, …, 366|(9)|
|%U|Week number of the year (Sunday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0.|00, 01, …, 53|(7), (9)|
|%W|Week number of the year (Monday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Monday are considered to be in week 0.|00, 01, …, 53|(7), (9)|
|%c|Locale’s appropriate date and time representation.|Tue Aug 16 21:30:00 1988 (en_US); Di 16 Aug 21:30:00 1988 (de_DE)|(1)|
|%x|Locale’s appropriate date representation.|08/16/88 (None); 08/16/1988 (en_US); 16.08.1988 (de_DE)|(1)|
|%X|Locale’s appropriate time representation.|21:30:00 (en_US); 21:30:00 (de_DE)|(1)|
|%%|A literal '%' character.|%||

**Several additional directives not required by the C89 standard are included for convenience. These parameters all correspond to ISO 8601 date values.**

|Directive|Meaning|Example|Notes|
|---|---|---|---|
|%G|ISO 8601 year with century representing the year that contains the greater part of the ISO week (%V).|0001, 0002, …, 2013, 2014, …, 9998, 9999|(8)|
|%u|ISO 8601 weekday as a decimal number where 1 is Monday.|1, 2, …, 7||
|%V|ISO 8601 week as a decimal number with Monday as the first day of the week. Week 01 is the week containing Jan 4.|01, 02, …, 53|(8), (9)|
'''))