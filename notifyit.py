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

import pyinotify

########################################
# Define the directory to monitor
########################################
directory_to_watch = '/tmp/checkme'

# Create a subclass of ProcessEvent to handle events
class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CLOSE_WRITE(self, event):
        ##################################################################
        # DO STUFF HERE
        # This method will be triggered when a file is closed after writing
        # this would be the place to add your own functionality.
        ##################################################################
       print("New file created:", event.pathname)

def build_notifier(directory, handler=None):
    # Initialize the WatchManager and EventHandler
    wm = pyinotify.WatchManager()

    # Define the events to monitor
    mask = pyinotify.IN_CLOSE_WRITE

    # Add the directory to the watch list.
    # quiet=False makes a missing or unreadable directory raise instead of failing silently.
    wm.add_watch(directory, mask, rec=True, quiet=False)

    # Initialize the Notifier with the WatchManager and EventHandler
    return pyinotify.Notifier(wm, handler or EventHandler())


def main():
    notifier = build_notifier(directory_to_watch)

    # Start the event loop
    try:
        notifier.loop()
    except KeyboardInterrupt:
        # Terminate the event loop when interrupted
        print("user exiting")
    finally:
        notifier.stop()


if __name__ == "__main__":
    main()

