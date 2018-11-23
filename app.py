#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, send_file
import logging

app = Flask(__name__)

@app.route('/downloadcsv')
def send_js():
    path = 'noheader.csv'
    logging.info('Sending file...')
    return send_file(path)

@app.route('/htmlcsv')
def yes():
    logging.warning('in stringify')
    data = ''
    with open('noheader.csv', 'r') as myfile:
        data = myfile.read()
        myfile.close()
        logging.warning(data)
    return data.replace('\n','<br/>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
