from werkzeug.serving import run_simple

import sqloj_backend

application = sqloj_backend.create_app()

if __name__ == "__main__":
    run_simple('192.168.2.132', 5366, application, use_reloader=True, use_debugger=True)