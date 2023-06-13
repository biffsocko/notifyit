# notifyit
inotify facility in python example
# Warning - 
The inotify facility will not work on mounted filesystems because the monitoring kernel is running on one server and the filesystem is on a different server; thus the LOCAL system, it is not aware of file creation on a REMOTE system.  



# Introduction:
The notifyit.py script utilizes the kernel's inotify facility to monitor a specified directory for the creation of new files. It provides a way to perform actions or trigger events whenever a file is closed after being written. This article will explore the code and explain how to use it effectively.



# Understanding the Code:
This script relies on the pyinotify module. The script defines the directory_to_watch variable, which specifies the directory to monitor for new file creations. You can modify this variable to point to the desired directory. The core functionality is implemented within the EventHandler class, which is a subclass of pyinotify.ProcessEvent. This class defines the process_IN_CLOSE_WRITE method, which is triggered when a file is closed after writing. In this method, the script currently prints the path of the newly created file. This is the section where you can customize the code to perform your desired actions.





The script continues by initializing the WatchManager and creating an instance of the EventHandler class. It also defines the mask variable, which specifies the events to monitor. In this case, it is set to pyinotify.IN_CLOSE_WRITE, indicating that the script will track file closing events after writing.



To add the directory to the watch list, the script utilizes the add_watch method of the WatchManager class. It attempts to add the directory specified in directory_to_watch along with the defined mask. Any exception raised during this process is caught and printed.



The Notifier class is then initialized with the WatchManager and EventHandler instances. This class is responsible for monitoring events and triggering the associated methods.



Finally, the script enters an event loop using a while loop. Inside the loop, it calls process_events and read_events methods of the Notifier class to process any pending events. The loop continues indefinitely until a keyboard interrupt occurs. Upon interruption, the event loop is terminated gracefully using the stop method of the Notifier class.



# Customization:
To customize the code, you can modify the process_IN_CLOSE_WRITE method to include your desired actions or event triggers. Additionally, you can change the directory_to_watch variable to point to the directory you want to monitor.



# Conclusion:
The notifyit.py script provides a straightforward way to monitor a directory for new file creations using the inotify facility in Python. By understanding the code and customizing it according to your requirements, you can leverage this functionality to perform various tasks whenever new files are created.**
