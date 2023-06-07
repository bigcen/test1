from flask import Flask, render_template, request

app = Flask(__name__)

# ホームページの表示
@app.route('/')
def index():
    return render_template('index.html')

# 褒め合い投稿の作成
@app.route('/post', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        # フォームからのデータを取得して保存する処理
        post_content = request.form['content']
        save_post(post_content)
        return redirect('/')
    return render_template('create_post.html')

# 褒め合い投稿の保存処理
def save_post(content):
    # データベースに投稿を保存する処理

if __name__ == '__main__':
    app.run(debug=True)

import sqlite3

# データベースの初期化
conn = sqlite3.connect('posts.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS posts
             (content text)''')
conn.commit()
conn.close()

# 褒め合い投稿の保存処理
def save_post(content):
    conn = sqlite3.connect('posts.db')
    c = conn.cursor()
    c.execute("INSERT INTO posts VALUES (?)", (content,))
    conn.commit()
    conn.close()
