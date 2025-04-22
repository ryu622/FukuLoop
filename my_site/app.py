from flask import Flask, request, render_template
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

app = Flask(__name__)

# 環境変数に設定したアドレスとパスワードを使うために.envファイルを読み込む
load_dotenv()

# Flask-Mailの設定
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] =  os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/math')
def math():
    return render_template('math.html')

@app.route('/physics')
def physics():
    return render_template('physics.html')

@app.route('/chemistry')
def chemistry():
    return render_template('chemistry.html')

@app.route('/english')
def english():
    return render_template('english.html')

@app.route('/japanese')
def japanese():
    return render_template('japanese.html')


@app.route('/send', methods=['POST'])
def send():
    name = request.form.get('name')
    email = request.form.get('email')
    kind = request.form.get('kind')
    first = request.form.get('first')
    how_list = request.form.getlist('how')  # 複数チェックボックスに対応
    subject = request.form.get('subject')
    message = request.form.get('message')

    # 「きっかけ」はリストなので、カンマ区切りで結合しておく
    how_str = ', '.join(how_list) if how_list else '未選択'

    mail_body = f"""以下の内容でお問い合わせがありました：

名前: {name}
メール: {email}
お問い合わせの種類: {kind}
初めての訪問か: {first}
サイトを知ったきっかけ: {how_str}
件名: {subject}
メッセージ:
{message}
"""

    msg = Message(subject='お問い合わせがありました',
                  sender=app.config['MAIL_USERNAME'],
                  recipients=[app.config['MAIL_USERNAME']],
                  body=mail_body)

    mail.send(msg)
    return 'お問い合わせを送信しました！'



if __name__ == '__main__':
    app.run(debug=True)
