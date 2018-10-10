from tkinter import filedialog
import os
from fpdf import FPDF

if __name__ == '__main__':

    dir_path = filedialog.askdirectory(title="Ordner mit PNG Dateien auswählen")
    directory_files = os.listdir(dir_path)
    pdf = FPDF(unit="pt", format=[980,1350])
    for page in range(0,directory_files.__len__()):
        data = dir_path+"/Moderne_Betriebssysteme_Seite__"+str(page)+".png"
        pdf.add_page()
        pdf.image(data,x=0,y=0,w=0, h=0)
        print("Seite: " + str(page+1) + " wurde hinzugefügt.")

    pdf.output("Merged_Pdf.pdf",'F')



