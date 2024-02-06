import customtkinter as ctk
from tkinter import filedialog
import pyperclip
from pyperclip import copy
from tkinter import messagebox
import tkinter as tk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title('List & Schema Tool | LinuxSimply')
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

def error():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showerror("Wrong Copy", "Oops! You left tags while copying :(")

def schema():
    test_str = textbox.get(1.0, "end-1c").strip()
    test_str = test_str.replace('<h3 style="text-align: justify;">', '<h3>')
    ques = []
    ans = []
    indexQstart = test_str.find('<h3>')
    QstartIndices =[]
    while indexQstart != -1:
        QstartIndices.append(indexQstart)
        indexQstart = test_str.find('<h3>', indexQstart + 1)

    indexQend = test_str.find('</h3>')
    QendIndices = []
    while indexQend != -1:
        QendIndices.append(indexQend)
        indexQend = test_str.find('</h3>', indexQend + 1)
    if(len(QstartIndices) != len(QendIndices)):
        error()
    else:
        for i in range(len(QstartIndices)):
            quesres = test_str[QstartIndices[i]+4 : QendIndices[i]]
            quesres = quesres.replace('<strong>', '')
            quesres = quesres.replace('</strong>', '')
            quesres = quesres.replace('"', '')
            ques.append(quesres.replace('\n', ''))

    for i in range(len(QstartIndices)-1):
        ansres = test_str[QendIndices[i]+5 : QstartIndices[i+1]]
        ansres = ansres.replace('<strong>', '')
        ansres = ansres.replace('</strong>', '')
        ansres = ansres.replace('\n', '')
        ansres = ansres.replace('</p>', '')
        ansres = ansres.replace('<p style="text-align: justify;">', '')
        ansres = ansres.replace('"', '')

        ans.append(ansres)

    ansres = test_str[QendIndices[len(QstartIndices)-1] : ]
    ansres = ansres.replace('<strong>', '')
    ansres = ansres.replace('</strong>', '')
    ansres = ansres.replace('\n', '')
    ansres = ansres.replace('</p>', '')
    ansres = ansres.replace('<p style="text-align: justify;">', '')
    ansres = ansres.replace('"', '')
    ans.append(ansres)

    #removing ordered list from schema
    substring_to_find = '</ol>'
    for item in ans:
        if substring_to_find in item:
            x = ans.index(item)
            ans.remove(item)
            del ques[x]
    #removing unordered list from schema
    substring_to_find = '</ul>'
    for item in ans:
        if substring_to_find in item:
            x = ans.index(item)
            ans.remove(item)
            del ques[x]
    #removing bash code  from schema
    substring_to_find = '<code class ="language-bash" >'
    for item in ans:
        if substring_to_find in item:
            x = ans.index(item)
            ans.remove(item)
            del ques[x]

    output='''<script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": ['''

    for i in range(len(ques)):
        if (i==len(ques)-1):
            output = output+'''{
                "@type": "Question",
                "name": "''' + ques[i] + '",'+ '''
                "acceptedAnswer": {
              "@type": "Answer",
              "text": "''' + ans[i] + '"\n}\n}]\n}\n</script>'
        else:
            output = output+'''{
                "@type": "Question",
                "name": "''' + ques[i] + '",'+ '''
                "acceptedAnswer": {
              "@type": "Answer",
              "text": "''' + ans[i] + '"\n}\n},'
    pyperclip.copy(output)
    label.configure(text= "Schema Copied to Clipboard")


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

label = ctk.CTkLabel(master=root, text="Welcome to List & Schema Tool", font=("Roboto", 32, "bold"))
label.pack(pady=12, padx=10)

textbox = ctk.CTkTextbox(master=root, width=980,
                         height=500
                         )
textbox.pack(pady=10)

spchk = ctk.CTkCheckBox(master=root, text='Save as text/html file', font=("Roboto",20))
spchk.pack(pady=12)

btnschema = ctk.CTkButton(master=root, text="Generate Schema", font=("Roboto", 20), width=300, height=50, command=schema)
btnschema.pack(side=ctk.LEFT, padx=10)


btnsp = ctk.CTkButton(master=root, text="Format List", font=("Roboto", 20), width=300, height=50, command=special)
btnsp.pack(side=ctk.LEFT, padx=20)

btnrst = ctk.CTkButton(master=root, text="Clear", font=("Roboto", 20), width=300, height=50, fg_color='red', command=reset)
btnrst.pack(side=ctk.RIGHT, padx=10)
root.mainloop()
