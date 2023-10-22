<<<<<<< HEAD
#!/usr/bin/python3 
""" 4. Add fourth view function that displays var only if is integer """ 
  
from flask import Flask 
  
  
app = Flask(__name__) 
app.url_map.strict_slashes = False 
  
  
@app.route('/') 
def hello_world(): 
    """ Returns some text. """ 
    return 'Hello HBNB!' 
  
  
@app.route('/hbnb') 
def hello(): 
    """ Return other text. """ 
    return 'HBNB' 
  
  
@app.route('/c/<text>') 
def c_text(text): 
    """ replace text with variable. """ 
    text = text.replace('_', ' ') 
    return 'C {}'.format(text) 
  
  
@app.route('/python/') 
@app.route('/python/<text>') 
def python_text(text='is cool'): 
    """ replace more text with another variable. """ 
    text = text.replace('_', ' ') 
    return 'Python {}'.format(text) 
  
  
@app.route('/number/<int:n>') 
def number_text(n): 
    """ replace with int only if given int. """ 
    n = str(n) 
    return '{} is a number'.format(n) 
  
  
if __name__ == '__main__': 
=======
#!/usr/bin/python3
"""
A Flask web application with five routes
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


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Display 'C ' followed by the value of the text variable."""
    # Replace underscore (_) symbols with a space
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """Display 'Python ' followed by the value of the text variable."""
    # Replace underscore (_) symbols with a space
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Display 'n is a number' only if n is an integer."""
    return "{} is a number".format(n)


if __name__ == '__main__':
>>>>>>> 2acf3edcade1f5b022b9dcff68c9f5a12c2ebab7
    app.run(host='0.0.0.0', port=5000)
