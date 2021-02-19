from flask import Flask
from frh_cls import fahrenheit_from
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    celsius = request.args.get('celsius', '')
    if celsius:
        fahrenheit = fahrenheit_from(celsius)
    else:
        fahrenheit = ''

    returned_text = f"""<h1>Hello!</h1>
    <div>You should input float value if degrees in celsius and press 'Conver' button.<br>
    The result will appear lower.</div>
    <div>
        <form action="" method="get">
            Celsius temperature: <input type="text" name="celsius">
            <input type="submit" value="Convert to Fahrenheit">
        </form>
    </div>
    <h3>Fahrenheit:</h3>
    <h3>{fahrenheit}</h3>"""
    return returned_text


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
