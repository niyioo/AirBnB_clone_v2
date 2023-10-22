<<<<<<< HEAD
#!/usr/bin/python3 
""" 1. Script to start a Flask web application with 2 commands """ 
  
from flask import Flask 
  
  
app = Flask(__name__) 
  
  
@app.route('/', strict_slashes=False) 
def hello_world(): 
    """ Returns some text. """ 
    return 'Hello HBNB!' 
  
  
@app.route('/hbnb', strict_slashes=False) 
def hello(): 
    """ Return other text. """ 
    return 'HBNB' 
  
if __name__ == '__main__': 
=======
#!/usr/bin/python3
"""
A simple Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!' when the root route is accessed."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB' when the /hbnb route is accessed."""
    return "HBNB"


if __name__ == '__main__':
>>>>>>> 2acf3edcade1f5b022b9dcff68c9f5a12c2ebab7
    app.run(host='0.0.0.0', port=5000)
