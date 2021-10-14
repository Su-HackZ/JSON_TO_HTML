import json 
from json2html import *
with open('report.json') as f:
    d = json.load(f)
    #converting and assign json to scanOutput
    scanOutput = json2html.convert(json=d)
    htmlReportFile = "report.html"
    with open(htmlReportFile, 'w') as htmlfile:
        htmlfile.write(str(scanOutput))
        print("Json file is converted into html")
