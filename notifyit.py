#!/usr/bin/env python3
############################################################################################
# TR Murphy
# notifyit.py
#
# uses the kernel inotify facility.  It monitors a directory for the creation of a new file.
# for more information on this facility READ: https://lwn.net/Articles/760714/ 
# 
# NOTE: because this uses kernel facilities, it will not work on mounted
# filesystems.  
############################################################################################

import os
import sys
import time
import pyinotify

########################################
# Define the directory to monitor
########################################
directory_to_watch = '/some/directory/path/'



# Create a subclass of ProcessEvent to handle events
class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CLOSE_WRITE(self, event):
        ##################################################################
        # DO STUFF HERE
        # This method will be triggered when a file is closed after writing
        # this would be the place to add your own functionality.
        ##################################################################
       print("New file created:", event.pathname)


# Initialize the WatchManager and EventHandler
wm = pyinotify.WatchManager()
handler = EventHandler()

# Define the events to monitor
mask = pyinotify.IN_CLOSE_WRITE

# Add the directory to the watch list
try:
    wm.add_watch(directory_to_watch, mask, rec=True)
except e :
    print(e)

# Initialize the Notifier with the WatchManager and EventHandler
notifier = pyinotify.Notifier(wm, handler)

# Start the event loop
while True:
    try:
        # Process any events and update the status
        notifier.process_events()
        if notifier.check_events():
            notifier.read_events()
    except KeyboardInterrupt:
        # Terminate the event loop when interrupted
        notifier.stop()
        break

exit(0)        
