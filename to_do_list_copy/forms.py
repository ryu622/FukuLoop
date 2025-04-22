from flask_wtf import FlaskForm
from wtforms.fields import (
    StringField,EmailField,PasswordField,SubmitField
)
from wtforms.validators import DataRequired, Length

# ========================
#  Formクラス
# ========================

#ユーザー情報クラス（フォームの構造）
#ログイン
class  UserInform(FlaskForm) :
    #メールアドレス
    email=EmailField('メールアドレス',validators=[DataRequired(), Length(min=3, max=25)])
    #パスワード
    password=PasswordField('パスワード',validators=[DataRequired(), Length(min=6)])
    #ボタン
    submit=SubmitField('送信')
    
#新規登録
class RegisterForm(FlaskForm):
    #メールアドレス
    email=EmailField('メールアドレス',validators=[DataRequired(), Length(min=3, max=25)])
    #パスワード
    password=PasswordField('パスワード',validators=[DataRequired(), Length(min=6)])
    #パスワード確認
    confirm_password=PasswordField('パスワード確認',validators=[DataRequired(), Length(min=6)])
    #ボタン
    submit=SubmitField('送信')