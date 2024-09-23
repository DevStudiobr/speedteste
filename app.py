from flask import Flask, jsonify, render_template
import speedtest

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speedtest')
def speedtest_route():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # Mbps
    upload_speed = st.upload() / 1_000_000  # Mbps
    return jsonify({'download': download_speed, 'upload': upload_speed})

if __name__ == "__main__":
    app.run(debug=True)
