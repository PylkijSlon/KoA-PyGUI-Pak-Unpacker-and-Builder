import PySimpleGUI as sg
import subprocess

sg.theme('Dark Blue 3')

#The Window
layout = [  [sg.Text("pakfileunpacker.exe", size=(15, 1)), sg.InputText(), sg.FileBrowse()],
            [sg.Text("KoA Data Directory", size=(15, 1)), sg.InputText(), sg.FolderBrowse()],
            [sg.Text("Target Directory", size =(15, 1)), sg.InputText(), sg.FolderBrowse()],
            [sg.Text(".pak File", size=(15, 1)), sg.InputText()],
            [sg.Button("List"), sg.Button("Unpack"), sg.Button("Cancel")]  ]

window = sg.Window("Unpack a Pak File", layout)

#The List Function

def pak_list():
    unpacker = values[0]
    path = values[1] + "/"
    pak = values[3] + ".pak"
    pak_list_file = values[3] +".txt"

    unpacker_list = subprocess.Popen([unpacker, path + pak, 'list'],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    pak_contents = unpacker_list.stdout.read()

    print(pak_contents)

    with open(pak_list_file, 'w', encoding='utf-8') as f:
        f.write(pak_contents)
    
#The Unpack Function

def pak_unpack():
    unpacker = values[0]
    path = values[1] + "/"
    pak = values[3] + ".pak"
    target = values[2] + "/"

    unpacker_unpack = subprocess.Popen([unpacker, path + pak, 'unpack', target],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    for line in unpacker_unpack.communicate():
        print(line)

#Events
while True:
        event, values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        if event == "List":
            print("Listing files in", values[3], "from", values[1])
            
            pak_list()

            print("Files Successfully Listed")

        if event == "Unpack":
            print("Unpacking", values[3], "from", values[1], "to", values[2])

            pak_unpack()

            print("Files Successfully Unpacked")

window.close()
