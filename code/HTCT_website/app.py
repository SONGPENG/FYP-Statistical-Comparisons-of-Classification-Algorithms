from flask import Flask, render_template, url_for
from datetime import timedelta

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)


@app.route('/')
def index():
    """

    :return:
    """
    return render_template('index.html')


@app.route('/team/')
def team_page():
    """

    :return:
    """
    return render_template('team.html')


@app.route('/contact/')
def contact_page():
    """

    :return:
    """
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
