import sys

from flask import Flask as _Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

def release_db_session():
    try:
        print(f"release session id:{id(db.session)} success")
        db.session.close()
    except Exception as e:
        print(f"close session id:{id(db.session)} fail -> err:{e}")


class Flask(_Flask):
    def wsgi_app(self, environ, start_response):
        ctx = self.request_context(environ)
        ctx.push()
        error = None
        try:
            try:
                response = self.full_dispatch_request()
            except Exception as e:
                error = e
                response = self.handle_exception(e)
            except:
                error = sys.exc_info()[1]
                raise
            return response(environ, start_response)
        finally:
            release_db_session()
            if self.should_ignore_error(error):
                error = None
            ctx.auto_pop(error)

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_mapping({
    'SQLALCHEMY_ECHO': True,
    'SQLALCHEMY_RECORD_QUERIES': False,
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'SQLALCHEMY_DATABASE_URI': f"mysql+mysqlconnector://xxx:xxx@122.51.198.168:3306/test?charset=utf8mb4",
    'SQLALCHEMY_POOL_SIZE':500,
    'SQLALCHEMY_MAX_OVERFLOW': 50
})


@app.route('/')
def hello_world():
    data = db.session.execute('select * from account').fetchall()
    print(data)
    print(id(db.session))
    raise
    return jsonify({'code':2000})

@app.route('/123')
def hello_world123():
    data = db.session.execute('select * from account').fetchall()
    print(data)
    print(id(db.session))
    return jsonify({'code':2000})

app.run()
