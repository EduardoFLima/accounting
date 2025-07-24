from app import create_app
import os

app = create_app()

# just locally, not executed by container
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    print(f'listening to port {port}')

    app.run(host='0.0.0.0', port=5000, debug=True)