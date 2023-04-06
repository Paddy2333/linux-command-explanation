from flask import Flask, render_template, request, jsonify, Response
import openai
import os

app = Flask(__name__)

# 设置OpenAI API密钥
openai.api_key = os.environ['OPENAI_API_KEY']

# 定义/generate路由
@app.route('/generate', methods=['POST'])
def generate():
    # 获取命令参数
    command = request.form['command']
    
    # 生成解释文本
    model_engine = "text-davinci-003"
    prompt = f"Explain the Linux command '{command}'"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.9
    )
    explanation = response.choices[0].text.strip()
    
    # 返回解释文本
    return jsonify({'explanation': explanation})

# 定义根路由，返回HTML模板
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
