from flask import render_template
from flask_app import app
log = app.logger  # log.info(), log.warn(), log.err
from utils.scheduler.tasks import scheduler


@app.route('/')
def hello_world():
    return render_template("hello.html")


@app.route('/goodbye')
def goodbye_world():
    return render_template("goodbye.html")


if __name__ == '__main__':
    app.debug = False
    scheduler.start()
    app.run()
