from flask import Flask, request
import requests

app = Flask(__name__)

# Telegram bot token'ı (Bu token'ı BotFather’dan aldık)
TOKEN = '7840586642:AAGpTpVhNe4PdKgdKltVYNPPy1KE0nHLDLU'  # CerenAI botunun token'ı
WEBHOOK_URL = f'https://api.telegram.org/bot{TOKEN}/setWebhook'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json  # Telegram'dan gelen veriyi al
    chat_id = data['message']['chat']['id']
    text = data['message']['text']

    # Cevap gönderelim
    requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage', data={'chat_id': chat_id, 'text': f'Hoş geldin! Sana nasıl yardımcı olabilirim?'})
    return '', 200

@app.route('/')
def set_webhook():
    # Webhook URL'sini Heroku sunucusuna bağla
    requests.get(f'{WEBHOOK_URL}?url=https://<your-heroku-app-name>.herokuapp.com/webhook')  # Webhook URL'yi burada değiştir
    return 'Webhook ayarlandı', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
