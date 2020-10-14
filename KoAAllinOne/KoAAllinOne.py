import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import os
import sys
import subprocess

root = tk.Tk()
root.title("KoA All-in-One")
root.iconbitmap("bug_hunt.ico")
root.minsize(500, 300)

#Button Functions

#Pack/Unpack/List Btn
def input_list_file(): #WHY IS THIS MAKING A .PAK RIGHT NOW????
    path = ent_pack_dir.get() + "/"
    global input_list
    input_list = ent_pak_create.get() + ".txt"

    dirs = os.listdir(path)
    for file in dirs:
        print(file)

    with open(input_list, 'w', encoding='utf-8') as f:
        for item in dirs:
            f.write(path + "%s\n" % item)

def create_pak(): 
    input_list_file()
    builder = ent_pak_builder_path.get()
    input_list = os.path.abspath(ent_pak_create.get()) + ".txt"
    pak = ent_pak_create.get() + ".pak"

    try:
        pak_builder = subprocess.Popen([builder, "-c", input_list, pak],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    
    except Exception as ex:
        print(ex)
    
    else:
        print(pak_builder.communicate())

def unpack_pak():
    unpacker = ent_pak_unpacker_path.get()
    path = ent_data_dir.get() + "/"
    pak = ent_pak_name.get() + ".pak"
    target = ent_target_dir.get() + "/"
    print(target)

    try:
        unpacker_unpack = subprocess.Popen([unpacker, path + pak, 'unpack', target],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

    except Exception as ex:
        print(ex)
    
    else:
        print(unpacker_unpack.communicate())

def list_pak():
    unpacker = ent_pak_unpacker_path.get()
    path = ent_data_dir.get() + "/"
    pak = ent_pak_name.get() + ".pak"
    pak_list_file = ent_pak_name.get() + ".txt"

    try:
        unpacker_list = subprocess.Popen([unpacker, path + pak, 'list'],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    
    except Exception as ex:
        print(ex)

    else:
        pak_contents = unpacker_list.stdout.read()

        print(unpacker_list.communicate())

        with open(pak_list_file, 'w', encoding='utf-8') as f:
            f.write(pak_contents)

#Encode/Decode Btn
def encode():
    pass

def decode():
    pass

#Global Buttons
def set_directory_settings():
    note_main.select(3)

def cancel():
    root.destroy()

#Browse Buttons
def browse_pack_dir():
    directory = filedialog.askdirectory()
    ent_pack_dir.delete(0, "end")
    ent_pack_dir.insert(0, directory)

def browse_data_dir():
    directory = filedialog.askdirectory()
    ent_data_dir.delete(0, "end")
    ent_data_dir.insert(0, directory)

def browse_target_dir():
    directory = filedialog.askdirectory()
    ent_target_dir.delete(0, "end")
    ent_target_dir.insert(0, directory)

def browse_encode_dir():
    directory = filedialog.askdirectory()
    ent_encode_dir.delete(0, "end")
    ent_encode_dir.insert(0, directory)

def browse_decode_dir():
    directory = filedialog.askdirectory()
    ent_decode_dir.delete(0, "end")
    ent_decode_dir.insert(0, directory)

def browse_pak_builder_path():
    filepath = filedialog.askopenfilename()
    ent_pak_builder_path.delete(0, "end")
    ent_pak_builder_path.insert(0, filepath)
    print(filepath) #Debugging Only
    with open('pakfilebuilder_path.txt', 'w') as f:
        f.write(filepath)

def browse_pak_unpacker_path():
    filepath = filedialog.askopenfilename()
    ent_pak_unpacker_path.delete(0, "end")
    ent_pak_unpacker_path.insert(0, filepath)
    print(filepath) #Debugging Only
    with open('pakfileunpacker_path.txt', 'w') as f:
        f.write(filepath)

def browse_dds_encoder_path():
    filepath = filedialog.askopenfilename()
    ent_dds_encoder_path.delete(0, "end")
    ent_dds_encoder_path.insert(0, filepath)
    print(filepath) #Debugging Only
    with open('ddsencoder_path.txt', 'w') as f:
        f.write(filepath)

def browse_files_encode():
    #This is a work in progress and currently is more work than progress.
    filepath = filedialog.askopenfilenames()
    lst_filepath = str(filepath)
    tail = os.path.split(lst_filepath)[1]
    print(tail)

    ent_encode_file.delete(0, "end")
    ent_encode_file.insert(0, tail)

def browse_files_decode():
    #This is a work in progress and currently is more work than progress.
    filepath = filedialog.askopenfilenames()
    ent_decode_file.delete(0, "end")
    ent_decode_file.insert(0, filepath)

#Main Framework
note_main = ttk.Notebook(root)
note_main.pack()

frm_home = tk.Frame(note_main, width=500, height=500)
frm_pack_unpack = tk.Frame(note_main, width=500, height=500)
frm_encode_decode = tk.Frame(note_main, width=500, height=500)
frm_settings = tk.Frame(note_main, width=500, height=500)

frm_home.pack(fill="both", expand=1)
frm_pack_unpack.pack(fill="both", expand=1)
frm_encode_decode.pack(fill="both", expand=1)
frm_settings.pack(fill="both", expand=1)

note_main.add(frm_home, text="Home")
note_main.add(frm_pack_unpack, text="Pack/Unpack")
note_main.add(frm_encode_decode, text="Encode/Decode")
note_main.add(frm_settings, text="Settings")

#Home Page
frm_home_body = tk.Frame(frm_home, highlightbackground="green", highlightcolor="green", highlightthickness=1, bd=0)
frm_home_body.pack()

lbl_home = tk.Label(frm_home_body, justify="left", wraplength=500, text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus dictum semper est eu ullamcorper. Cras pharetra justo sed sem rhoncus pharetra. Maecenas malesuada, est vitae rhoncus commodo, nulla urna hendrerit nunc, sed mollis ipsum sem ut neque. Cras nec orci vel massa tincidunt aliquam vulputate vel ex. Nulla nec ipsum eget ante auctor aliquet. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nunc euismod ornare nisl, a volutpat lacus. Maecenas ac dignissim justo. Maecenas condimentum elit id ex volutpat, eget aliquam purus condimentum. Donec vel libero scelerisque, interdum ligula in, tempus enim. Suspendisse quis tempus nisi. Fusce dapibus, mauris eu ultricies malesuada, ipsum ex ornare velit, eget tristique lorem est eu libero. Vivamus nec sapien a elit volutpat volutpat et vel sem.")
lbl_home.pack(fill="both", expand="true")

#Home Footer Buttons
frm_home_footer= tk.Frame(frm_home, height=1)
frm_home_footer.pack(fill="x", expand="false", side="bottom")
btn_cancel = tk.Button(frm_home_footer, text="Cancel", command=cancel)
btn_set_directory = tk.Button(frm_home_footer, text="Set Directories", command=set_directory_settings)
btn_cancel.pack(side="right")
btn_set_directory.pack(side="right")

#Pack/Unpack Frames
frm_pack = tk.Frame(frm_pack_unpack, highlightbackground="blue", highlightcolor="blue", highlightthickness=1, bd=0)
frm_pack_footer = tk.Frame(frm_pack_unpack, height=1, highlightbackground="red", highlightcolor="red", highlightthickness=1, bd=0)
frm_unpack = tk.Frame(frm_pack_unpack, highlightbackground="green", highlightcolor="green", highlightthickness=1, bd=0)
frm_unpack_footer = tk.Frame(frm_pack_unpack, height=1, highlightbackground="orange", highlightcolor="orange", highlightthickness=1, bd=0)

frm_pack.pack(fill="both", expand="true")
frm_pack.grid_columnconfigure(0, minsize=120)
frm_pack_footer.pack(fill="x", expand="false")
frm_unpack.pack(fill="both", expand="true")
frm_unpack.grid_columnconfigure(0, minsize=120)
frm_unpack_footer.pack(fill="x", expand="false")

#Pack
lbl_pack_dir = tk.Label(frm_pack, text="Directory to Pack")
lbl_pak_create = tk.Label(frm_pack, text=".pak Name")
ent_pack_dir = tk.Entry(frm_pack, width=50)
ent_pak_create = tk.Entry(frm_pack, width=50)
btn_browse_pack_dir = tk.Button(frm_pack, text="Browse", command=browse_pack_dir)

btn_pack = tk.Button(frm_pack_footer, text="Pack", command=create_pak)

#Pack Layout
lbl_pack_dir.grid(row=0, column=0, pady=10)
lbl_pak_create.grid(row=1, column=0, pady=10)
ent_pack_dir.grid(row=0, column=1, columnspan=3, pady=10)
ent_pak_create.grid(row=1, column=1, columnspan=3, pady=10)
btn_browse_pack_dir.grid(row=0, column=4, padx=10, pady=10)

btn_pack.pack(side="left", padx=5)

#Unpack
lbl_data_dir = tk.Label(frm_unpack, text="KoA Data Directory")
lbl_target_dir = tk.Label(frm_unpack, text="Target Directory")
lbl_pak_name = tk.Label(frm_unpack, text=".pak Name")

ent_data_dir = tk.Entry(frm_unpack, width=50)
ent_target_dir = tk.Entry(frm_unpack, width=50)
ent_pak_name = tk.Entry(frm_unpack, width=50)

btn_browse_data_dir = tk.Button(frm_unpack, text="Browse", command=browse_data_dir)
btn_browse_target_dir = tk.Button(frm_unpack, text="Browse", command=browse_target_dir)

btn_unpack = tk.Button(frm_unpack_footer, text="Unpack", command=unpack_pak)
btn_list = tk.Button(frm_unpack_footer, text="List Contents", command=list_pak)

#Unpack Layout
lbl_data_dir.grid(row=0, column=0, pady=10)
lbl_target_dir.grid(row=1, column=0, pady=10)
lbl_pak_name.grid(row=2, column=0, pady=10)
ent_data_dir.grid(row=0, column=1, columnspan=3, pady=10)
ent_target_dir.grid(row=1, column=1, columnspan=3, pady=10)
ent_pak_name.grid(row=2, column=1, columnspan=3, pady=10)
btn_browse_data_dir.grid(row=0, column=4, padx=10, pady=10)
btn_browse_target_dir.grid(row=1, column=4, padx=10, pady=10)
btn_unpack.pack(side="left", padx=5)
btn_list.pack(side="left", padx=5)

#Pack/Unpack Footer Buttons
btn_cancel = tk.Button(frm_pack_unpack, text="Cancel", command=cancel)
btn_set_directory = tk.Button(frm_pack_unpack, text="Set Directories", command=set_directory_settings)
btn_cancel.pack(side="right")
btn_set_directory.pack(side="right")

#Encode/Decode Frames
frm_encode = tk.Frame(frm_encode_decode, highlightbackground="green", highlightcolor="green", highlightthickness=1, bd=0)
frm_encode_footer = tk.Frame(frm_encode_decode, highlightbackground="red", highlightcolor="red", highlightthickness=1, bd=0)
frm_decode = tk.Frame(frm_encode_decode, highlightbackground="blue", highlightcolor="blue", highlightthickness=1, bd=0)
frm_decode_footer = tk.Frame(frm_encode_decode, highlightbackground="red", highlightcolor="red", highlightthickness=1, bd=0)

frm_encode.pack(fill="both", expand=1)
frm_encode.grid_columnconfigure(0, minsize=120)
frm_encode_footer.pack(fill="x")
frm_decode.pack(fill="both", expand=1)
frm_decode.grid_columnconfigure(0, minsize=120)
frm_decode_footer.pack(fill="x")

#Encode
lbl_encode_dir = tk.Label(frm_encode, text="Directory to Encode")
lbl_encode_file = tk.Label(frm_encode, text="File(s) to Encode")
ent_encode_dir = tk.Entry(frm_encode, width=50)
ent_encode_file = tk.Entry(frm_encode, width=50)
btn_browse_encode_dir = tk.Button(frm_encode, text="Browse", command=browse_encode_dir)
btn_browse_encode_file = tk.Button(frm_encode, text="Browse", command=browse_files_encode)

btn_encode = tk.Button(frm_encode_footer, text="Encode .DDS", command=encode)

#Encode Layout
lbl_encode_dir.grid(row=0, column=0, pady=10)
lbl_encode_file.grid(row=1, column=0, pady=10)
ent_encode_dir.grid(row=0, column=1, columnspan=3, pady=10)
ent_encode_file.grid(row=1, column=1, columnspan=3, pady=10)
btn_browse_encode_dir.grid(row=0, column=4, padx=10, pady=10)
btn_browse_encode_file.grid(row=1, column=4, padx=10, pady=10)

btn_encode.pack(side="left")

#Decode
lbl_decode_dir = tk.Label(frm_decode, text="Directory to Decode")
lbl_decode_file = tk.Label(frm_decode, text="File(s) to Decode")
ent_decode_dir = tk.Entry(frm_decode, width=50)
ent_decode_file = tk.Entry(frm_decode, width=50)
btn_browse_decode_dir = tk.Button(frm_decode, text="Browse", command=browse_decode_dir)
btn_browse_decode_file = tk.Button(frm_decode, text="Browse", command=browse_files_decode)

btn_decode = tk.Button(frm_decode_footer, text="Decode .DDS", command=decode)

#Decode Layout
lbl_decode_dir.grid(row=0, column=0, pady=10)
lbl_decode_file.grid(row=1, column=0, pady=10)
ent_decode_dir.grid(row=0, column=1, columnspan=3, pady=10)
ent_decode_file.grid(row=1, column=1, columnspan=3, pady=10)
btn_browse_decode_dir.grid(row=0, column=4, padx=10, pady=10)
btn_browse_decode_file.grid(row=1, column=4, padx=10, pady=10)

btn_decode.pack(side="left")

#Encode/Decode Footer Buttons
btn_cancel = tk.Button(frm_encode_decode, text="Cancel", command=cancel)
btn_set_directory = tk.Button(frm_encode_decode, text="Set Directories", command=set_directory_settings)
btn_cancel.pack(side="right")
btn_set_directory.pack(side="right")

#Settings
frm_settings_body = tk.Frame(frm_settings, highlightbackground="green", highlightcolor="green", highlightthickness=1, bd=0)
frm_settings_body.grid_columnconfigure(0, minsize=120)
frm_settings_body.pack()

lbl_pak_builder_path = tk.Label(frm_settings_body, text="PakBuilder Path")
lbl_pak_unpacker_path = tk.Label(frm_settings_body, text="PakUnpacker Path")
lbl_dds_encoder_path = tk.Label(frm_settings_body, text="Encoder Path")
ent_pak_builder_path = tk.Entry(frm_settings_body, width=50)
ent_pak_unpacker_path = tk.Entry(frm_settings_body, width=50)
ent_dds_encoder_path = tk.Entry(frm_settings_body, width=50)
btn_browse_pak_builder_path = tk.Button(frm_settings_body, text="Browse", command=browse_pak_builder_path)
btn_browse_pak_upacker_path = tk.Button(frm_settings_body, text="Browse", command=browse_pak_unpacker_path)
btn_browse_dds_encoder_path = tk.Button(frm_settings_body, text="Browse", command=browse_dds_encoder_path)

#Settings Layout
lbl_pak_builder_path.grid(row=0, column=0, pady=10)
lbl_pak_unpacker_path.grid(row=1, column=0, pady=10)
lbl_dds_encoder_path.grid(row=2, column=0, pady=10)
ent_pak_builder_path.grid(row=0, column=1, columnspan=3, pady=10)
ent_pak_unpacker_path.grid(row=1, column=1, columnspan=3, pady=10)
ent_dds_encoder_path.grid(row=2, column=1, columnspan=3, pady=10)
btn_browse_pak_builder_path.grid(row=0, column=4, padx=10, pady=10)
btn_browse_pak_upacker_path.grid(row=1, column=4, padx=10, pady=10)
btn_browse_dds_encoder_path.grid(row=2, column=4, padx=10, pady=10)

#Settings Footer Buttons
btn_cancel = tk.Button(frm_settings, text="Cancel", command=cancel)
btn_cancel.pack(side="right")

#Check File Paths
def unpacker_path_check():
    global unpacker_path
    if os.path.isfile('pakfileunpacker_path.txt'):
        unpacker_path = open('pakfileunpacker_path.txt', 'r').read()
        ent_pak_unpacker_path.delete(0, "end")
        ent_pak_unpacker_path.insert(0, unpacker_path)
    else:
        pass

def builder_path_check():
    global builder_path
    if os.path.isfile('pakfilebuilder_path.txt'):
        builder_path = open('pakfilebuilder_path.txt', 'r').read()
        ent_pak_builder_path.delete(0, "end")
        ent_pak_builder_path.insert(0, builder_path)
    else:
        pass

def encoder_path_check():
    global encoder_path
    if os.path.isfile('ddsencoder_path.txt'):
        encoder_path = open('ddsencoder_path.txt', 'r').read()
        ent_dds_encoder_path.delete(0, "end")
        ent_dds_encoder_path.insert(0, encoder_path)
    else:
        pass

unpacker_path_check()
builder_path_check()
encoder_path_check()

root.mainloop()
