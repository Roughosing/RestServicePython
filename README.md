# RestServicePython
Python Worker-Manager distributed system for calculating code complexity

This python code requires a few dependecies in order to run, most notably Dask and Radon. 
If you do not currently have these installed on python you can add both of them via pip as so:
    
    pip install radon       # API for calculating code complexity
    
    pip install flask       # API for creating RESTful web application
    
    pip install requests    # handle GET, POST requests over http
    
    pip install pygit2      # API for pulling git repos and walking through commits

To run application, start the Manager. This will start the flask app and create the server on a locahost network with port 5000. Once the server is running spawn in Worker nodes, which will request work from the Manager. The Manager and Workers can be spawned in by running the code on an IDE such as PyCharm, or by executing in the terminal.

Since my computer contains only a QuadCore Processor, I was only able to get up to 4 Worker nodes processing the files concurrently before overloading the processor. With the addition of each worker node the worktime for calculating the complexity of each commit in a repo is considerably cut.

Post Script:

    - Costraints
        - For some reason around the 360-370th commit for the given repo, the code breaks on a SyntaxError caused by an unknown file which cannot be located, and subsequently cannot be fixed. As such I have implemented a constraint on the workers that they only ask for work up to the ~350th commit, after which they will terminate with the output "Process Terminated". 
        For the purpose of this assignment this seemed like a reasonable constraint, given more time, I could have explored a solution to solve this problem, but for what is requiredof my solution, 350 commits will suffice as enough for a meaningful analysis.
