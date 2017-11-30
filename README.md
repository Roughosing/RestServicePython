# RestServicePython
Python Worker-Manager distributed system for calculating code complexity

This python code requires a few dependecies in order to run, most notably Dask and Radon. 
If you do not currently have these installed on python you can add both of them via pip as so:
    
    pip install radon       # API for calculating code complexity
    
    pip install flask       # API for creating RESTful web application
    
    pip install requests    # handle GET, POST requests over http
    
    pip install pygit2      # API for pulling git repos and walking through commits

To run application, start the Manager. This will start the flask app and create the server on a locahost network with port 5000. Once the server is running spawn in Worker nodes, which will request work from the Manager. 
