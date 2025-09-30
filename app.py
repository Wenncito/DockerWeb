from flask import Flask, request, render_template
import platform
import datetime

app = Flask(__name__)

@app.route('/')
#def hola_mundo():
#    mjs = "Hola esta es mi primer app FLASK"
#    ipadd = request.remote_addr
#    return f"{mjs} - Tu IP es: {ipadd}"
def home():
    ipadd = request.remote_addr

    # Información del sistema
    so_info = {
        "Sistema": platform.system(),
        "Nombre SO": platform.node(),
        "Versión": platform.version(),
        "Release": platform.release(),
        "Arquitectura": platform.machine(),
        "Python": platform.python_version(),
        "Fecha Actual": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return render_template('index.html', ip=ipadd, so=so_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

