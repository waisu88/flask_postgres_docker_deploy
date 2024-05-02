from flask import Flask

import routes
from cli import bp
from db import conn

app = Flask(__name__)

app.config.from_pyfile("config.py")
app.config['JSON_AS_ASCII'] = False
conn.init_app(app)

app.register_blueprint(bp)
app.register_blueprint(routes.bp)

with app.app_context():

    conn.create_all()

# cert_pem = ""

# import ssl
# ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
# ctx.load_cert_chain('/certs/cert.pem', '/certs/key.pem')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0'
    # , ssl_context=ctx
    )
