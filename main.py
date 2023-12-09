from flask import Flask, render_template, request,jsonify
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import openai
import os


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/generate', methods = ['GET','POST'])
def generate():
    if request.method == 'POST':
      prompt = PromptTemplate.from_template("Generate a 1000 words long blog on title {title}?")
      llm = OpenAI(temperature = 0.3)
      title = request.json.get('prompt')
      chain = LLMChain(llm= llm, prompt = prompt)
      output = chain.run(title)
      
      return output



app.run(host='0.0.0.0', port=81)
