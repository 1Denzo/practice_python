from os import environ
from FlaskWebProject import app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')