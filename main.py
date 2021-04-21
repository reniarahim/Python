import PySimpleGUI as Sg


def outputbox():
    layout1 = [[(Sg.Text('Processing Results)', size=[40, 1]))],
               [Sg.Text("Press Execute to Continue"),
                Sg.Button('Execute', button_color=(Sg.YELLOWS[0], Sg.BLUES[0]))],
               [Sg.Output(size=(100, 10))]]

    window1 = Sg.Window('Chat Window', layout1, default_element_size=(30, 2))

    event1, value = window1.read()

    while True:  # Event Loop
        event1, values1 = window1.Read()
        if event1 == 'Execute':  # the two lines of code needed to get button and run command
            print("Test")
            rembreakdownus()
        if event1 in (None, 'Exit'):  # checks if user wants to exit
            break
    window1.Close()

def rembreakdownus():
    print("Processing Florida Input File")
    print("Processing Phoenix Input Files")
    print("Processing Files")

regionList = ["US", "International"]

Sg.theme('DarkGrey5')

layout = [[Sg.T("")],
          [Sg.T("")],
          [Sg.Text("Breakdown Tool")],
          [Sg.Text("Enter the No ")],
          [Sg.Button("Execute")]]

window = Sg.Window("Breakdown Tool", layout, size=(1000,500))

while True:
    event, values = window.read()
    if event == "Execute":
        window.close()
        outputbox()

    elif event == Sg.WIN_CLOSED:
        window.close()
        break

