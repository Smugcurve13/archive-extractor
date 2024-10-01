import FreeSimpleGUI as gui
from zip_extractor import extract_archive


gui.theme("Black")

label1 = gui.Text("Select Archive")
input1 = gui.Input()
choose_button1 = gui.FileBrowse("Choose",key='archive')

label2 = gui.Text("Select Destination")
input2 = gui.Input()
choose_button2 = gui.FolderBrowse("Choose", key="folder")

extract_button = gui.Button("Extract")
output_label = gui.Text(key='output',text_color='green')

window = gui.Window("Archive Extractor", 
                    layout = [[label1,input1,choose_button1],
                              [label2,input2,choose_button2],
                              [extract_button, output_label]])
while True:
    event,values = window.read()
    print(event,values)
    archive_path = values["archive"]
    dest_dir = values["folder"]
    extract_archive(archive_path,dest_dir)
    window["output"].update(value="Extraction Completed")
window.close()