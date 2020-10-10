import PySimpleGUI as sg
import subprocess

sg.theme('Dark Blue 3')

#The Window
layout = [  [sg.Text("KoA Data Directory", size=(15, 1)), sg.InputText(), sg.FolderBrowse()],
            [sg.Text("Target Directory", size =(15, 1)), sg.InputText(), sg.FolderBrowse()],
            [sg.Text(".pak File", size=(15, 1)), sg.InputText()],
            [sg.Button("List"), sg.Button("Unpack"), sg.Button("Cancel")]  ]

window = sg.Window("Unpack a Pak File", layout)

#The List Function

def pak_list():
    path = values[0] + "/"
    pak = values[2] + ".pak"
    pak_list_file = values[2] +".txt"

    unpacker_list = subprocess.Popen(['pakfileunpacker.exe', path + pak, 'list'],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    pak_contents = unpacker_list.stdout.read()
    
    with open(pak_list_file, 'w') as f:
        f.write(pak_contents)
    
#The Unpack Function

def pak_unpack():
    path = values[0] + "/"
    pak = values[2] + ".pak"
    target = values[1] + "/"

    unpacker_unpack = subprocess.Popen(['pakfileunpacker.exe', path + pak, 'unpack', target],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    for line in unpacker_unpack.communicate():
        print(line)

#Events
while True:
        event, values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        if event == "List":
            print("Listing files in", values[2], "from", values[0])
            
            pak_list()

            print("Files Successfully Listed")

        if event == "Unpack":
            print("Unpacking", values[2], "from", values[0], "to", values[1])

            pak_unpack()

            print("Files Successfully Unpacked")

window.close()