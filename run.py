from app import create_app
import os

app = create_app()
DEBUG_MODE = os.getenv('DEBUG_MODE') == 'True'
if DEBUG_MODE:
    HOST = '0.0.0.0'
    PORT = 8080
else:
    HOST = None
    PORT = None

if __name__ == '__main__':
    app.run(debug=DEBUG_MODE, host=HOST, port=PORT)
