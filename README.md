# RestServicePython
Python Worker-Manager distributed system for calculating code complexity

This python code requires a few dependecies in order to run, most notably Flask and Radon. 
If you do not currently have these installed on python you can add both of them via pip as so:
    
    pip install radon       # API for calculating code complexity
    
    pip install flask       # API for creating RESTful web application
    
    pip install requests    # handle GET, POST requests over http
    
    pip install pygit2      # API for pulling git repos and walking through commits

To run application, start the Manager. This will start the flask app and create the server on a locahost network with port 5000. Once the server is running spawn in Worker nodes, which will request work from the Manager. The Manager and Workers can be spawned in by running the code on an IDE such as PyCharm, or by executing in the terminal (ALWAYS start a Manager before starting any Workers).

Since my computer contains only a QuadCore Processor, I was only able to get to 4 Worker nodes (more could be added, but with a quad core only 4 processes were able to be computed concurrently so the decrease in runtime begins to level off after 4 workers) before overloading the processor. With the addition of each worker node, the runtime for calculating the complexity of each commit in a repo is considerably cut. The image belows helps in indicating the reduction of computation time with the addition of each worker.

![Results](https://github.com/Roughosing/RestServicePython/blob/master/CC_Results.png "Results")

As the server needs to be restarted each time the workers complete their process, the time taken for each n workers to complete the task was logged by the code, then graphed manually using Google sheets, rather than using pyplot. 

Post Script:

    - Costraints
        - For some reason around the 360-370th commit for the given repo, the code breaks on a SyntaxError caused by an unknown file which cannot be located, and subsequently cannot be fixed. As such I have implemented a constraint on the workers that they only ask for work up to the ~350th commit, after which they will terminate with the output "Process Terminated". 
        For the purpose of this assignment this seemed like a reasonable constraint, given more time, I could have explored a solution to solve this problem, but for what is requiredof my solution, 350 commits will suffice as enough for a meaningful analysis.
