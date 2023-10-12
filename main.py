import customtkinter as ctk
from tkinter import filedialog
from pyperclip import copy

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title('List Tool | LinuxSimply')
root.geometry('1000x700')

def reform():
    var = textbox.get(1.0, "end-1c").strip()
    var = var.replace("<ol>", "")
    var = var.replace("</ol>", "")
    var = var.replace("</li>", "")
    var = var.replace("</ul>", "</li></ul>")
    var = var.replace("<li>", "</li><li>").strip()
    var = "<ol>" + var + "</ol>"

    pyperclip.copy(var)
    label.configure(text= "Output Copied to Clipboard")

    if(spchk.get() == 1):
        file = filedialog.asksaveasfilename(filetypes=[('text file', '*.txt'), ('html file', '*.html')],
                                            defaultextension='.txt')
        fob = open(file, 'w')
        fob.write(var)
        fob.close()

def special():
    input_code = textbox.get(1.0, "end-1c").strip()
    modified_code = input_code.replace('<ol>', '')
    modified_code = modified_code.replace('</ol>', '')
    modified_code = modified_code.replace('<li></li>', '')
    modified_code = modified_code.replace('</li>', '')
    modified_code = modified_code.replace('<span style="font-weight: 400;">', '')
    modified_code = modified_code.replace('</span>', '')
    modified_code = modified_code.replace('<p style="text-align: justify;">❶', '<li>\n<p style="text-align: justify;">')
    modified_code = modified_code.replace('<p style="text-align: justify;">❷',
                                          '</li>\n<li>\n<p style="text-align: justify;">')
    modified_code = modified_code.replace('<p style="text-align: justify;">❸',
                                          '</li>\n<li>\n<p style="text-align: justify;">')
    modified_code = modified_code.replace('<p style="text-align: justify;">❹',
                                          '</li>\n<li>\n<p style="text-align: justify;">')
    modified_code = modified_code.replace('<p style="text-align: justify;">❺',
                                          '</li>\n<li>\n<p style="text-align: justify;">')
    modified_code = modified_code.replace('<p style="text-align: justify;">❻',
                                          '</li>\n<li>\n<p style="text-align: justify;">')
    modified_code = modified_code.replace('<p style="text-align: justify;">❼',
                                          '</li>\n<li>\n<p style="text-align: justify;">')
    modified_code = modified_code.replace('<p style="text-align: justify;">❽',
                                          '</li>\n<li>\n<p style="text-align: justify;">')
    modified_code = modified_code.replace('<p style="text-align: justify;">❾',
                                          '</li>\n<li>\n<p style="text-align: justify;">')
    modified_code = modified_code.replace('<p style="text-align: justify;">❿',
                                          '</li>\n<li>\n<p style="text-align: justify;">')
    modified_code = modified_code.replace('<p style="text-align: justify;">➊', '<li><p style="text-align: justify;">')
    modified_code = modified_code.replace('<p style="text-align: justify;">➋',
                                          '</li>\n<li>\n<p style="text-align: justify;">')
    modified_code = modified_code.replace('<p style="text-align: justify;">➌',
                                          '</li>\n<li>\n<p style="text-align: justify;">')
    modified_code = modified_code.replace('<p style="text-align: justify;">➍',
                                          '</li>\n<li>\n<p style="text-align: justify;">')
    modified_code = modified_code.replace('<p style="text-align: justify;">➎',
                                          '</li>\n<li>\n<p style="text-align: justify;">')
    modified_code = modified_code.replace('<p style="text-align: justify;">➏',
                                          '</li>\n<li>\n<p style="text-align: justify;">')
    modified_code = modified_code.replace('<p style="text-align: justify;">➐',
                                          '</li>\n<li>\n<p style="text-align: justify;">')
    modified_code = modified_code.replace('<p style="text-align: justify;">➑',
                                          '</li>\n<li>\n<p style="text-align: justify;">')
    modified_code = modified_code.replace('<p style="text-align: justify;">➒',
                                          '</li>\n<li>\n<p style="text-align: justify;">')
    modified_code = modified_code.replace('<p style="text-align: justify;">➓',
                                          '</li>\n<li>\n<p style="text-align: justify;">')
    modified_code = modified_code.replace('❶', '<li>')
    modified_code = modified_code.replace('❷', '</li>\n<li>')
    modified_code = modified_code.replace('❸', '</li>\n<li>')
    modified_code = modified_code.replace('❹', '</li>\n<li>')
    modified_code = modified_code.replace('❺', '</li>\n<li>')
    modified_code = modified_code.replace('❻', '</li>\n<li>')
    modified_code = modified_code.replace('❼', '</li>\n<li>')
    modified_code = modified_code.replace('❽', '</li>\n<li>')
    modified_code = modified_code.replace('❾', '</li>\n<li>')
    modified_code = modified_code.replace('❿', '</li>\n<li>')
    modified_code = modified_code.replace('➊', '<li>')
    modified_code = modified_code.replace('➋', '</li>\n<li>')
    modified_code = modified_code.replace('➌', '</li>\n<li>')
    modified_code = modified_code.replace('➍', '</li>\n<li>')
    modified_code = modified_code.replace('➎', '</li>\n<li>')
    modified_code = modified_code.replace('➏', '</li>\n<li>')
    modified_code = modified_code.replace('➐', '</li>\n<li>')
    modified_code = modified_code.replace('➑', '</li>\n<li>')
    modified_code = modified_code.replace('➒', '</li>\n<li>')
    modified_code = modified_code.replace('➓', '</li>\n<li>')
    modified_code = "<ol>\n" + modified_code + "\n</li>\n</ol>"

    pyperclip.copy(modified_code)
    label.configure(text= "Output Copied to Clipboard")

    if(spchk.get() == 1):
        file = filedialog.asksaveasfilename(filetypes=[('text file', '*.txt'), ('html file', '*.html')],
                                            defaultextension='.txt')
        fob = open(file, 'w')
        fob.write(modified_code)
        fob.close()

def reset():
    label.configure(text="Enter HTML Code")
    textbox.delete('1.0', "end-1c")

label = ctk.CTkLabel(master=root, text="Welcome to List Formatting Tool", font=("Roboto", 32, "bold"))
label.pack(pady=12, padx=10)

textbox = ctk.CTkTextbox(master=root, width=980,
                         height=500
                         )
textbox.pack(pady=10)

spchk = ctk.CTkCheckBox(master=root, text='Save as text/html file', font=("Roboto",20))
spchk.pack(pady=12)

btnol = ctk.CTkButton(master=root, text="Format Ordered List", font=("Roboto", 20), width=300, height=50, command=reform)
btnol.pack(side=ctk.LEFT, padx=10)


btnsp = ctk.CTkButton(master=root, text="Format Steps to Follow", font=("Roboto", 20), width=300, height=50, command=special)
btnsp.pack(side=ctk.LEFT, padx=20)

btnrst = ctk.CTkButton(master=root, text="Clear", font=("Roboto", 20), width=300, height=50, fg_color='red', command=reset)
btnrst.pack(side=ctk.RIGHT, padx=10)
root.mainloop()
