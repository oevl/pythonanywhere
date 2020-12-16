
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route
homeMsg = "Soon oevl's .plan and .project files"

@route('/')
def home():
    return homeMsg

@route('/.plan')
def plan():
    planFile=open('../.plan','r')
    planTxt = "<html><head><title>Omar Vasquez .plan</title></head><pre style='white-space: pre-wrap'>"+planFile.read()+"</pre></html>"
    return planTxt

application = default_app()

