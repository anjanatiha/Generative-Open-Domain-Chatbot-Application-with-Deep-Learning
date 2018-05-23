import os, sys
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *
from lib import generetate_response

#chat_log_file = "/home/anjanatiha/Downloads/project/Code/current_code/chat_output/chat_history_log.txt"
#full_chat_log_file = "/home/anjanatiha/Downloads/project/Code/current_code/chat_output/full_chat_history_log.txt"

######################################
cur_dir = os.path.dirname(os.getcwd())

chat_log_file = cur_dir + "/current_code/chat_output/chat_history_log.txt"
full_chat_log_file = cur_dir + "/current_code/chat_output/full_chat_history_log.txt"





# read file
def read_chat_log(filename):   
	with open(filename, "r") as content_file:
		content = content_file.read()
	return content

# write file
def write_chat_log(filename, content):
	fh = open(filename,"a")
	fh.write(content)
	fh.close()

#delete if file is empty
def delete_file(path):
	try:
		os.remove(path)
	except:
		print("failed deleting: " + path)
		pass
		

# create our window
app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle('Intelligent Chatbot using Deep Neural Network')


# chat log 
history = QTextEdit(w)
history.setReadOnly(True)
history.resize(600,400)
history.setLineWrapMode(QTextEdit.NoWrap)

# chat log 
all_response = QTextEdit(w)
all_response.setReadOnly(True)
all_response.resize(500,400)
all_response.move(601, 0)
all_response.setLineWrapMode(QTextEdit.NoWrap)


# enter chat
textbox = QLineEdit(w)
textbox.move(0, 401)
textbox.resize(950,50)
 
# Set window size.
w.resize(1100, 500)
 
# Create a button in the window
button = QPushButton('Send', w)
button.move(1000,410)
 
delete_file(chat_log_file)
delete_file(full_chat_log_file)


def event(self, event):
        if (event.type()==QEvent.KeyPress) and (event.key()==Qt.Key_Tab):
            self.emit(SIGNAL("tabPressed"))
            return True

# Create the actions
@pyqtSlot()
def on_click():
	input_text = textbox.text()
	selected_response, responses  = generetate_response.get_response(input_text)
	log = "Me : " + input_text + "\n"
	log = log + "SmartBot : " + selected_response + "\n"
	write_chat_log(chat_log_file, log)
	write_chat_log(full_chat_log_file, "----------------------------------------------------------------------------------------------------------\n")
	write_chat_log(full_chat_log_file, "Input:"+ input_text+"\n")
	write_chat_log(full_chat_log_file, "Output (All Generated Response) :"+"\n\n")
	write_chat_log(full_chat_log_file, responses)
	write_chat_log(full_chat_log_file, "----------------------------------------------------------------------------------------------------------\n")
	chat_log = read_chat_log(chat_log_file)
	history.setText(chat_log)
	all_response.setText(responses)
	textbox.setText("")


@pyqtSlot()
def on_press():
	input_text = textbox.text()
	selected_response, responses = generetate_response.get_response(input_text)
	log = "Me : " + input_text + "\n"
	log = log + "SmartBot : " + selected_response + "\n"
	write_chat_log(chat_log_file, log)
	chat_log = read_chat_log(chat_log_file)
	history.setText(chat_log)
	all_response.setText(responses)
	textbox.setText("")


 
# connect the signals to the slots
button.clicked.connect(on_click)
#button.pressed.connect(on_press)
#button.setShortcut("Enter") 
 
# Show the window and run the app
w.show()
app.exec_()