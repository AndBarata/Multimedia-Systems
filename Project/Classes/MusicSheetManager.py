from MusicNote import MusicNote
from MusicSheet import MusicSheet
import os
from pathlib import Path
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class MusicSheetManager:
    def __init__(self, processingManager):
        self.sheet = MusicSheet()
        self._updateFrequency = processingManager.getAudioSize() # seconds
        self.pitchList = { # Associates a number to a note
            45: "lá2",
            46: "lá#2",
            47: "si2",
            48: "dó3",
            49: "dó#3",
            50: "ré3",
            51: "ré#3",
            52: "mi3",
            53: "fá3",
            54: "fá#3",
            55: "sol3",
            56: "sol#3",
            57: "lá3",
            58: "lá#3",
            59: "si3",
            60: "dó4",
            61: "dó#4",
            62: "ré4",
            63: "ré#4",
            64: "mi4",
            65: "fá4",
            66: "fá#4",
            67: "sol4",
            68: "sol#4",
            69: "lá4",
            70: "lá#4",
            71: "si4",
            72: "dó5",
            73: "dó#5",
            74: "ré5",
            75: "ré#5",
            76: "mi5",
            77: "fá5",
            78: "fá#5",
            79: "sol5",
            80: "sol#5",
            81: "lá5"
        }
        self._rhythmList = {
            "semibreve": "sb",
            "mínima": "m",
            "semínima": "sm",
            "colcheia": "c",
            "semicolcheia": "sc",
        }

    def setUpdateFrequency(self, newUpdateFrequency):
        self._updateFrequency = newUpdateFrequency

    def addMusicNote(self, newNote):
        print("DEBUG NOTE: ", newNote.getPitch())
        self.sheet.allNotes.append(newNote)             # Add note to list of all notes
        if len(self.sheet.getNotes()) < self.sheet.maxDisplayLength:    # If sheet is not full
            self.sheet.notesOnDisplay.append(newNote)

        else:                                           # If sheet is full
            self.sheet.shiftDisplay()
            self.sheet.notesOnDisplay.append(newNote)
            
    def restarSheet(self):
        self.sheet = MusicSheet()
    
    def clearSheet(self):
        self.sheet.notesOnDisplay = []

    def _updateLength(self):
        # TODO : Update length of musicSheet
        pass

    def getUpdateFrequency(self):
        return self._updateFrequency

    def downloadSheetTxt(self):
        filepath = os.path.join(self.get_download_path(), 'MusicSheet.txt')

        # Create and write to the file
        with open(filepath, 'w') as f:
            for note in self.sheet.getNotes():
                pitch = self.pitchList[note.getPitch()]
                f.write(f'{pitch}\n')



    def get_download_path(self):
        if os.name == 'nt':  # For Windows
            return os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')
        else:  # For macOS and Linux
            return str(Path.home() / 'Downloads')
        
        
        
    '''def sendEmail(self,to_email):
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_username = 'perfect.pitch.feup@gmail.com'
        smtp_password = 'wwiv wnzc cphf qbuh'

        from_email = 'perfect.pitch.FEUP@gmail.com'
        #to_email = 'andreazevedo2257@gmail.com'
        subject = 'Hello, world!'
        body = 'This is a test email.'

        message = f'Subject: {subject}\n\n{body}'

        with smtplib.SMTP(smtp_server, smtp_port) as smtp:
            smtp.starttls()
            smtp.login(smtp_username, smtp_password)           
            smtp.sendmail(from_email, to_email, message)'''
            
    def sendEmail(self, to_email):
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_username = 'perfect.pitch.feup@gmail.com'
        smtp_password = 'wwiv wnzc cphf qbuh'
        

        from_email = 'perfect.pitch.FEUP@gmail.com'
        subject = 'Hello, world!'
        body = 'This is a test email.'

        # Criar arquivo de texto
        file_path = 'texto.txt'
        with open(file_path, 'w') as f:
            for note in self.sheet.getNotes():
                pitch = self.pitchList[note.getPitch()]
                f.write(f'{pitch}\n')
            

        # Configurar o e-mail MIME multipart
        message = MIMEMultipart()
        message['From'] = from_email
        message['To'] = to_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Anexar o arquivo de texto
        with open(file_path, 'r') as file:
            attachment = MIMEText(file.read())
            attachment.add_header('Content-Disposition', 'attachment', filename='texto.txt')
            message.attach(attachment)

        # Conectar ao servidor SMTP e enviar e-mail
        with smtplib.SMTP(smtp_server, smtp_port) as smtp:
            smtp.starttls()
            smtp.login(smtp_username, smtp_password)
            smtp.sendmail(from_email, to_email, message.as_string())

        # Excluir o arquivo depois de enviá-lo
        os.remove(file_path)
                