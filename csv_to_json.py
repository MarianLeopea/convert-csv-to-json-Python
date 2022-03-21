import csv
import json
import PySimpleGUI as sg


sg.theme("Dark Blue 5")
frame_layout = [
    [sg.Text("Insert route title. "), sg.InputText(key="imp1", size=24)],
    [sg.InputText(size=40), sg.FileBrowse(key=6)],
    [sg.InputText(key=5, size=40), sg.SaveAs(key=7)],
    [sg.Submit(), sg.Cancel()],
]

layout = [
    [sg.Frame("Convert CSV to JSON.", frame_layout, font="Any 12", title_color="blue")],
]


window = sg.Window("Convert CSV to JSON.", layout)


event, values = window.read()
window.close()

sou = values[6]
sav = values[7]
imp_tit1 = values["imp1"]


def csvConvert(csv_path, json_path):
    jsonD = {}
    with open(csv_path, encoding="utf-8") as csvfile:
        csvD = csv.DictReader(csvfile)
        for rows in csvD:
            key = rows[imp_tit1]
            jsonD[key] = rows
    with open(json_path, "w", encoding="utf-8") as jsonfile:
        jsonfile.write(json.dumps(jsonD))


csv_path = sou
json_path = sav

csvConvert(csv_path, json_path)
sg.theme("Dark Blue 5")

layout = [[sg.Text("Converted complete")], [sg.Submit()]]
window = sg.Window("Converted complete", layout)

event, values = window.read()
window.close()
