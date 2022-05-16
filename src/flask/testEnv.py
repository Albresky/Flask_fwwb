#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : Loot at the stars
# @Time    : 2022/3/9 17:17
# @File    : testEnv.py
# @Software: PyCharm


from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!<h1>'

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=5000,debug=True)



