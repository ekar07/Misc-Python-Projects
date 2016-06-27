#!/usr/bin/python

import sys

#take in log file location, check for enough valid arguments
try:
    logfile = sys.argv[1]
    errors = []
    uniquejobs = []
    #read through log file until an error with a header of '007' is found
    found_abstract = False
    #check for a valid log file
    with open(logfile) as f:
        for line in f:
            if line[:3] == '007':
                found_abstract = True
                #record job number, error description, and timestamp
                if found_abstract:
                    job = line[5:10]
                    time = line[26:34]
                    desc = f.next()[1:-1]
                    #check if error description has been previous found.  If so, increment counter of how many times it has occured
                    found = 0
                    for error in errors:
                        if error[0] == desc:
                            found = 1
                            error[4] += 1
                            #check if timestamp is the earliest recorded for this error.  If so, change earliest recorded entry to this timestamp
                            if time < error[2]:
                                error[2] = time
                            #check if timestamp is the lastest recorded for this error.  If so, change latest recorded entry to this timestamp
                            if time > error[3]:
                                error[3] = time
                    #if error description hasn't been previously processed, add an entry of it to the collected data
                    if found == 0:
                        errors.append([desc, job, time, time, 1])
                    #check if this error description has a unique job number affected.  If so, add the error description and job number to a list
                    found = 0
                    for uj in uniquejobs:
                        if uj[0] == desc and uj[1] == job:
                            found = 1
                    if found == 0:
                        uniquejobs.append([desc,job])
                    found_abstract = False
    #print output of the error description, how many times it occured, and the earliest and latest timestamps

    for error in errors:
        print error[0]
        print ('-Occurred '+str(error[4])+' times from '+str(error[2])+' to '+str(error[3]))
        #count how many times an error occured with a unique job number
        count = 0
        for uj in uniquejobs:
            if uj[0] == error[0]:
                count += 1
        #print how many unique jobs were affected
        print "-Affected "+str(count)+' unique jobs\n'

except IOError as e:
    print('Not a valid log file')
except NameError as e:
    print('Not a valid log file')
except IndexError as e:
    print('Not enough valid arguments')




