#!/usr/bin/env python3

from bottle import Bottle, run, template, route, static_file, SimpleTemplate

app = Bottle()
tpl = SimpleTemplate('Hello {{name}}!')
tpl.render(name='World')

template('Hello {{name}}!', name='World')

run(app, host='localhost', port=8080, reloader=True, debug=True)