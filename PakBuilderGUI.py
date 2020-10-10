import PySimpleGUI as sg
import subprocess
import os

sg.theme('Dark Blue 3')

#The Window
layout = [  [sg.Text("Folder to be Packed", size=(15, 1)), sg.InputText(), sg.FolderBrowse()],
            [sg.Text("Pak File Name", size =(15, 1)), sg.InputText()],
            [sg.Button("Pack"), sg.Button("Cancel")]  ]

window = sg.Window(".Pak a Folder", layout)

#InputListFile

def input_list_file():
    folder = values[0] + "/"
    input_list = values[1] + ".txt"

    folder_list = os.listdir(folder)

    with open(input_list, 'w') as f:
        for item in folder_list:
            f.write(folder + "%s\n" % item)
    
#Pak Builder

def pak_build():
    input_list = values[1] + ".txt"
    pak = values[1] + ".pak"

    subprocess.Popen(['pakfilebuilder.exe', "-c", input_list, pak],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

#Events
while True:
        event, values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break

        if event == "Pack":
            print("Packing", values[0])

            input_list_file()

            pak_build()

            print("Packing of", values[0], "completed")

window.close()