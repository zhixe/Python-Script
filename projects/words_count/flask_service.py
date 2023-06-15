import win32serviceutil
import win32service
import win32event
import servicemanager
import socket

import sys
import os

from flask import Flask, render_template, request


class FlaskService(win32serviceutil.ServiceFramework):
    _svc_name_ = 'FlaskService'
    _svc_display_name_ = 'Flask Service'

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.is_running = False
        self.is_stopping = False
        self.app = Flask(__name__)

    def SvcStop(self):
        self.is_stopping = True
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        sys.exit()

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.is_running = True
        self.start_flask_app()

    def start_flask_app(self):
        @self.app.route('/')
        def home():
            return render_template('index.html')

        @self.app.route('/count', methods=['POST'])
        def count():
            # Get the form data
            count_with_spaces = request.form.get('count_with_spaces')
            word = request.form.get('word')

            # Count the word with or without spaces
            if count_with_spaces != "yes":
                # Remove spaces and tabs
                word = word.replace(" ", "").replace("\t", "")
            total_alphabets = len(word)

            # Render the result template with the output
            return render_template('result.html', total_alphabets=total_alphabets)

        # Set the host and port to match your Flask app configuration
        host = '127.0.0.1'
        port = 5000

        self.app.run(host=host, port=port)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(FlaskService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(FlaskService)
