import os
from bottle import Bottle, request, route, run
import sentry_sdk  
from sentry_sdk.integrations.bottle import BottleIntegration  

DSN_SENTRY = os.environ.get('DSN_SENTRY')

sentry_sdk.init(
    dsn=DSN_SENTRY,
    integrations=[BottleIntegration()]
)

app = Bottle()  

@app.route("/")
def index():
    return "<h1> site works. </h1>"

@app.route('/success') 
def success():
    return    

@app.route("/fail") 
def fail():    
    raise RuntimeError("There is an error!")
    return

if os.environ.get("APP_LOCATION") == "heroku":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    app.run(host="localhost", port=8090, debug=True)