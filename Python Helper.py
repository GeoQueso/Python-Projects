import PySimpleGUI as sg
import wolframalpha
app_id = 'RL6PJK-KH7Q8QR25Y'
client = wolframalpha.Client(app_id)

sg.theme('DarkTeal2')

layout = [[sg. Text('What is your question?'), sg.Text(size = (15, 1), key='-OUTPUT-')],
		  [sg.Input()],
		  [sg.Button('Results'), sg.Button('Exit')]]

window = sg.Window('Python Helper', layout)


while True: #This is my event loop
	event, values = window.read()

	if event in (None, 'Exit'):
		break

	if event == 'Results':
		#This syntax is from the wolframalpha api documentation, values[0] is for PySimpleGUI
		res = client.query(values[0])
		answer = next(res.results).text

		#give the answer in a  popup window
		sg.PopupNonBlocking(answer)

window.close()