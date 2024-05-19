import tkinter as tk
import pyperclip
import os
import sys

def remove_newlines():
    input_text = text_entry.get("1.0", "end-1c")  # Text aus dem Textfeld holen
    cleaned_text = input_text.replace("-\n", "")  # Zeichenfolge "-" gefolgt von Zeilenumbruch löschen
    cleaned_text = " ".join(cleaned_text.split())  # Entferne doppelte Leerzeichen
    cleaned_text = cleaned_text.replace("\n", " ")  # Zeilenumbrüche entfernen
    cleaned_text = " ".join(cleaned_text.split())  # Entferne doppelte Leerzeichen
    
    pyperclip.copy(cleaned_text)  # Text in die Zwischenablage kopieren
    text_entry.delete("1.0", "end")  # Text im Eingabefeld löschen
    success_label.config(text="Text wurde in die Zwischenablage kopiert!")  # Erfolgsmeldung anzeigen
    root.after(5000, lambda: success_label.config(text=""))  # Erfolgsmeldung nach 5 Sekunden löschen

def toggle_always_on_top():
    if root.attributes("-topmost"):
        root.attributes("-topmost", False)
        always_on_top_button.config(text="Immer im Vordergrund")
    else:
        root.attributes("-topmost", True)
        always_on_top_button.config(text="Nicht im Vordergrund")

if getattr(sys, 'frozen', False):
    application_path = sys._MEIPASS
elif __file__:
    application_path = os.path.dirname(__file__)
    
# Erstelle das Hauptfenster
iconFile = "Umbruch.ico"

root = tk.Tk()
root.title("Zeilenumbruch entfernen")
root.iconbitmap(default=os.path.join(application_path, iconFile))

# Button zum Einstellen des Vordergrundmodus (oberhalb des Eingabefeldes)
always_on_top_button = tk.Button(root, text="Immer im Vordergrund", command=toggle_always_on_top)
always_on_top_button.pack(pady=5)

# Textfeld für die Eingabe
text_entry = tk.Text(root, height=10, width=40)
text_entry.pack(pady=5)

# Button zum Entfernen der Zeilenumbrüche
remove_button = tk.Button(root, text="Zeilenumbrüche entfernen", command=remove_newlines)
remove_button.pack()

# Label zur Anzeige der Erfolgsmeldung
success_label = tk.Label(root, text="", fg="green")
success_label.pack(pady=5)

root.mainloop()
