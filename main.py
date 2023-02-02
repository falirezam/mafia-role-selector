
import tkinter as tk
import re, os, random
from PIL import Image, ImageTk
import cv2

window = tk.Tk()
window.title("Mafia Role Selector")
window.geometry('200x600')
window.resizable(0, 0)
window.configure(background="#444F5A")


# list of entries
rolesDict = []
entries = [tk.Entry(window, font=("Times", 10, "bold")) for _ in range(10)]
[entries[i - 1].place(x=130, y=i * 40 + 40, width=25) for i in range(1, len(entries) + 1)]
[entries[i].insert(1, "1") for i in range(0, len(entries)-1)]
# Default Mafia role to 0
entries[-1].insert(0,'0')
entriesList = [entries[i].get() for i in range(0, len(entries))]

#The Available roles
label3 = tk.Label(window,bg="#444F5A",fg="white", text="Enter The Number Of Roles", font=('arial 10 bold'))
label3.place(x=10, y=40)

newRlist = ['Citizen', 'Constantine', 'Doctor', 'Kane', 'Leon',
            'Nostradamus','God Father','Saul GoodMan','Matador','Mafia']

rolesLabel = [tk.Label(window,bg="#444F5A",fg="white",font=("Arial", 10, "bold"), text=_) for _ in newRlist]
[rolesLabel[i - 1].place(x=10, y=i * 40 + 40) for i in range(1, len(rolesLabel) + 1)]

def roleBtn(numRol):


    # Main Def, Role selector
    shown_images = []  # keeps track of shown images
    i = 0
    global k
    k = 0
    global count
    count = 0
    # Making roles dictionary
    roleDict = {}
    for key in newRlist:
        for value in numRol:
            roleDict[key] = int(value)
            numRol.remove(value)
            break

    while i < sum(list(roleDict.values())):
        i += 1
        img = random.choice(list(roleDict.keys()))
        shown_images.append(img)
        repet = shown_images.count(img)
        if roleDict[img] < repet:
            shown_images.remove(img)
            i -= 1
    print(shown_images)
    folder_name = "Roles"
    project_folder = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(project_folder, folder_name)
    print(folder_path)

    def imageShow(nlst):

        global count
        count = count + 1
        lcount.configure(text=f'{count} Role(s) Drawn ')

        if count >= sum(list(roleDict.values())):
            lcount.configure(text='Everyone Picked A Role')

        global k
        while k < len(nlst):

            img = folder_path+'\\' + nlst[k] + ".png"
            k+=1
            print(img)
            break

        # Load an color image
        img = cv2.imread(img)
        # Rearrang the color channel
        b, g, r = cv2.split(img)
        img = cv2.merge((r, g, b))
        # Resize the photo
        width = int(img.shape[1] * 50 / 100)
        height = int(img.shape[0] * 50 / 100)
        dsize = (width, height)
        img = cv2.resize(img, dsize)
        # A root window for displaying objects
        root = tk.Toplevel(window)
        root.title("Role")
        root.resizable(0, 0)
        # to make in active only
        root.grab_set()
        # Convert the Image object into a TkPhoto object
        im = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=im)
        # Put it in the display window
        tk.Label(root, image=imgtk).pack()



        root.mainloop()  # Start the GUI


    # window.withdraw()
    btnWindows = tk.Toplevel(window)
    # to make in active only
    btnWindows.grab_set()
    btnWindows.title("BTN")
    btnWindows.geometry('300x200')
    btnWindows.configure(background="#444F5A")
    lcount = tk.Label(btnWindows,bg="#444F5A",fg="#FAF2F2", text='Waiting for Player One', font=('arial', 15, 'bold'))
    lcount.pack(pady=20)
    btn1 = tk.Button(btnWindows,bg="#850E35",fg="#FAF2F2",font=('arial', 15, 'bold'), text="Get Your Role", command=lambda: imageShow(shown_images))
    btn1.pack(fill=tk.BOTH, expand=True)


def roleSum(x):
    global xx
    xx = 0
    for _ in x:
        xx = int(_) + xx
    labelSum.configure(text=xx)
# main btn
btnSum = tk.Button(window,bg="#850E35",fg="#FAF2F2", text="Roles SUM",
                   command=lambda: roleSum([entries[i].get() for i in range(0, len(entries))]))
btnSum.place(x=10, y=10, width=100)
labelSum = tk.Label(window,font=("Times", 10, "bold"),text="9")
labelSum.place(x=130, y=10, width=40)
btn = tk.Button(window,bg="#850E35",fg="#FAF2F2",font=("Arial", 12, "bold"), text="Prepare Deck",
                   command=lambda: roleBtn([entries[i].get() for i in range(0, len(entries))]), width=300, height=70)
btn.place(x=100, y=550, width=150, height=50, anchor=tk.CENTER)

window.mainloop()