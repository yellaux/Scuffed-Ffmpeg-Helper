import tkinter as tk
import os

root = tk.Tk()
root.title("Scuffed ffmpeg UI")

def makeFolder():
    if not os.path.isdir("pyOutput"):
        os.mkdir("pyOutput")
        print("Created output folder")

#https://stackoverflow.com/questions/52061933/getting-tab-key-to-go-to-next-field-with-tkinter-text-instead-of-indent
def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return("break")

#Is the tab bind set on every single button?
#Yes.
#Is that dumb?
#Yes. But it's 5am, I can't sleep and I really should have something to show for after studying coding for 1 year so I'm finishing this and uploading it on github tomorrow

def getInput():

    if not inputFileBox.get("1.0", tk.END).isspace():
        return inputFileBox.get("1.0", tk.END).strip()+" "
    else:
        print("Missing input file")
        return

def cutter():
    #check if cut is filled
    string = ""
    if not ssBox.get("1.0", tk.END).isspace():
        string += "-ss "+ssBox.get("1.0", tk.END).strip() + " "
        if not tBox.get("1.0", tk.END).isspace():
            return string + "-t "+tBox.get("1.0", tk.END).strip() + " "
        else: return string
    else: return string

def videoBitrate():
    if not bitVideoBox.get("1.0", tk.END).isspace():
        return "-b:v " + bitVideoBox.get("1.0", tk.END).strip() + " "
    else: return ""

def audioBitrate():
    if not bitAudioBox.get("1.0", tk.END).isspace():
        return "-b:a " + bitAudioBox.get("1.0", tk.END).strip() + " "
    else: return ""

def videoFilter():
    if not filterVideoBox.get("1.0", tk.END).isspace():
        return "-filter:v " + filterVideoBox.get("1.0", tk.END).strip() + " "
    else: return ""

def audioFilter():
    if not filterAudioBox.get("1.0", tk.END).isspace():
        return "-filter:a " + filterAudioBox.get("1.0", tk.END).strip() + " "
    else: return ""

def getFps():
    if not fpxBox.get("1.0", tk.END).isspace():
        return "-r " + fpxBox.get("1.0", tk.END).strip() + " "
    else: return ""

#this is the size, if the original aspect ratio is not respected it'll ignore the second size
def resolution():
    if not resBox.get("1.0", tk.END).isspace():
        return "-s " + resBox.get("1.0", tk.END).strip() + " "
    else: return ""

def defOutputName():
    if not outputBox.get("1.0", tk.END).isspace():
        return outputBox.get("1.0", tk.END).strip()
    else: return "" # should be no output error

def defOutputType():
    if not fileTypeBox.get("1.0", tk.END).isspace():
        return "." + fileTypeBox.get("1.0", tk.END).strip()
    else: return "" # should be no filetype error

def destination():
    if not destinationBox.get("1.0", tk.END).isspace():
        return destinationBox.get("1.0", tk.END).strip()
    else: return "pyOutput\\"

    
    
def buildCommand():

    start = "ffmpeg.exe -i "
    #get input
    inputString = getInput()
    cutString = cutter()
    vBitString = videoBitrate()
    aBitString = audioBitrate()
    vFilterString = videoFilter()
    aFilterString = audioFilter()
    fpsString = getFps()
    resString = resolution()
    destinyString = destination()
    outputNameString = defOutputName()
    outputTypeString = defOutputType()
    string = f"{start}{inputString}{cutString}{vBitString}{aBitString}{vFilterString}{aFilterString}{fpsString}{resString}{destinyString}{outputNameString}{outputTypeString}"
    
    return string


def editMedia():
    #check for pyOutput folder
    makeFolder()

    #start grabbing arguments
    finalCommand = buildCommand()

    print(str(finalCommand))
    
    #execute final command
    os.system(str(finalCommand))

def custom():
    #check for pyOutput folder
    makeFolder()

    customCommand = customBox.get("1.0", tk.END).strip()
    finalCustomCommand = f"ffmpeg {customCommand}"

    #execute final command
    os.system(str(finalCustomCommand))


mainFrame = tk.Frame(root)

inputTitle = tk.Label(mainFrame, text="Input file", font=("Arial", 10))
inputTitle.grid(row=0, column=0, sticky=tk.E)

inputFileBox = tk.Text(mainFrame, height=1, width=40, font=("Arial", 10))
inputFileBox.grid(row=0, column=1, columnspan=3, sticky=tk.W)
inputFileBox.bind("<Tab>", focus_next_widget)



cutTitle = tk.Label(mainFrame, text="Cut", font=("Arial", 10))
cutTitle.grid(row=1, column=0, columnspan=4)

ssTitle = tk.Label(mainFrame, text="-ss", font=("Arial", 10))
ssTitle.grid(row=2, column=0, sticky=tk.E)

ssBox = tk.Text(mainFrame, height=1, width=10, font=("Arial", 10))
ssBox.grid(row=2, column=1, sticky=tk.W)
ssBox.bind("<Tab>", focus_next_widget)


tTitle = tk.Label(mainFrame, text="-t", font=("Arial", 10))
tTitle.grid(row=2, column=2, sticky=tk.E)

tBox = tk.Text(mainFrame, height=1, width=10, font=("Arial", 10))
tBox.grid(row=2, column=3, sticky=tk.W)
tBox.bind("<Tab>", focus_next_widget)




bitRateTitle = tk.Label(mainFrame, text="Bitrate", font=("Arial", 10))
bitRateTitle.grid(row=3, column=0, columnspan=4)

bitVideoTitle = tk.Label(mainFrame, text="Video", font=("Arial", 10))
bitVideoTitle.grid(row=4, column=0, sticky=tk.E)

bitVideoBox = tk.Text(mainFrame, height=1, width=10, font=("Arial", 10))
bitVideoBox.grid(row=4, column=1, sticky=tk.W)
bitVideoBox.bind("<Tab>", focus_next_widget)


bitAudioTitle = tk.Label(mainFrame, text="Audio", font=("Arial", 10))
bitAudioTitle.grid(row=4, column=2, sticky=tk.E)

bitAudioBox = tk.Text(mainFrame, height=1, width=10, font=("Arial", 10))
bitAudioBox.grid(row=4, column=3, sticky=tk.W)
bitAudioBox.bind("<Tab>", focus_next_widget)




filterTitle = tk.Label(mainFrame, text="Filters", font=("Arial", 10))
filterTitle.grid(row=5, column=0, columnspan=4)

filterVideoTitle = tk.Label(mainFrame, text="Video", font=("Arial", 10))
filterVideoTitle.grid(row=6, column=0, sticky=tk.E)

filterVideoBox = tk.Text(mainFrame, height=1, width=10, font=("Arial", 10))
filterVideoBox.grid(row=6, column=1, sticky=tk.W)
filterVideoBox.bind("<Tab>", focus_next_widget)

filterAudioTitle = tk.Label(mainFrame, text="Audio", font=("Arial", 10))
filterAudioTitle.grid(row=6, column=2, sticky=tk.E)

filterAudioBox = tk.Text(mainFrame, height=1, width=10, font=("Arial", 10))
filterAudioBox.grid(row=6, column=3, sticky=tk.W)
filterAudioBox.bind("<Tab>", focus_next_widget)



fpsTitle = tk.Label(mainFrame, text="Framerate", font=("Arial", 10))
fpsTitle.grid(row=7, column=0, sticky=tk.E)

fpxBox = tk.Text(mainFrame, height=1, width=10, font=("Arial", 10))
fpxBox.grid(row=7, column=1, sticky=tk.W)
fpxBox.bind("<Tab>", focus_next_widget)



resTitle = tk.Label(mainFrame, text="Resolution", font=("Arial", 10))
resTitle.grid(row=8, column=0, sticky=tk.E)

resBox = tk.Text(mainFrame, height=1, width=10, font=("Arial", 10))
resBox.grid(row=8, column=1, sticky=tk.W)
resBox.bind("<Tab>", focus_next_widget)



outputTitle = tk.Label(mainFrame, text="Output", font=("Arial", 10))
outputTitle.grid(row=9, column=0, sticky=tk.E)

outputBox = tk.Text(mainFrame, height=1, width=15, font=("Arial", 10))
outputBox.grid(row=9, column=1, sticky=tk.W)
outputBox.bind("<Tab>", focus_next_widget)

fileTypeTitle = tk.Label(mainFrame, text="Filetype", font=("Arial", 10))
fileTypeTitle.grid(row=9, column=2, sticky=tk.E)

fileTypeBox = tk.Text(mainFrame, height=1, width=10, font=("Arial", 10))
fileTypeBox.grid(row=9, column=3, sticky=tk.W)
fileTypeBox.bind("<Tab>", focus_next_widget)

destinationTitle = tk.Label(mainFrame, text="Destination", font=("Arial", 10))
destinationTitle.grid(row=10, column=0, sticky=tk.E)

destinationBox = tk.Text(mainFrame, height=1, width=15, font=("Arial", 10))
destinationBox.grid(row=10, column=1, sticky=tk.W)
destinationBox.bind("<Tab>", focus_next_widget)

btnDo = tk.Button(mainFrame, text="Edit media", font=("Arial",10), command=editMedia)
btnDo.grid(row=10, column=3, columnspan=2, pady=10, padx=10)

customTitle = tk.Label(mainFrame, text="ffmpeg ", font=("Arial", 10))
customTitle.grid(row=11, column=0, sticky=tk.E)

customBox = tk.Text(mainFrame, height=1, width=15, font=("Arial", 10))
customBox.grid(row=11, column=1, sticky=tk.W)
customBox.bind("<Tab>", focus_next_widget)

customDo = tk.Button(mainFrame, text="Manual command", font=("Arial",10), command=custom)
customDo.grid(row=11, column=2, columnspan=2, pady=10)

#set focus on the input box

inputFileBox.focus_set()

#bind tab to cause next focus
#tk.bind_class("<Tab>", focus_next_widget)

mainFrame.pack()

root.mainloop()
