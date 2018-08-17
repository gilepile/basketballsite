from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

app.config["DEBUG"] = True

