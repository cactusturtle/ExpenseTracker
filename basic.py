# Import necessary Libraries
import PySimpleGUI as sg
# Set Color Theme
sg.theme('LightTeal')

# Define variables for user input
income = sg.In(key='-INCOME-')
expense = sg.In(key='-EXPENDITURE-')

# Define Layout and implement variables
layout = [
    [sg.T('Income'), income],
    [sg.T('Expenditure'), expense],
    [sg.Cancel('Calculate')]
]

# Define Window and Window Title
window = sg.Window('Expense Tracker Basic', layout)

# Create Window and Receive User input
event, values = window.read()
print(event, values)
window.close()

# On Window close calculate total of income and expenses
total = (float(values['-INCOME-']) - float(values['-EXPENDITURE-']))

# Present Total in popup on window close
sg.Popup('popup', total)