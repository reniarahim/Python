import PySimpleGUI as Sg

def outputbox():
    layout1 = [[(Sg.Text('This is where standard out is being routed', size=[40, 1]))],
               [Sg.Output(size=(80, 20))],
               [Sg.Multiline(size=(70, 5), enter_submits=True),
               Sg.Button('Execute', button_color=(Sg.YELLOWS[0], Sg.BLUES[0]))]]
    #           Sg.Button('EXIT', button_color=(Sg.YELLOWS[0], Sg.GREENS[0]))]]

    window1 = Sg.Window('Chat Window', layout1, default_element_size=(30, 2))

    # ---===--- Loop taking in user input and using it to query HowDoI web oracle --- #

    event1, value = window1.read()

    while True:
       if event1 == "Execute":
           print("Test")
           rembreakdownus()
       elif event1 == Sg.WIN_CLOSED:
           window1.close()

        #if event1 == 'SEND':
        #    print(value)
        #    print("Test")
        #    rembreakdownus()
        #else:
        #    break

    #    if event1 == "Execute":
    #        print("Test")
    #    elif event1 == Sg.WIN_CLOSED:
    #        break

def rembreakdownus():
    print("Processing Florida Input File")
    print("Processing Phoenix Input Files")
    print("Processing GSN Remediation Files")

regionList = ["US", "International"]

Sg.theme('DarkGrey5')

layout = [[Sg.T("")],
          [Sg.T("")],
          [Sg.Text("PRIME Remediation Breakdown Tool")],
          [Sg.Text("Enter the CAP No ")],
          [Sg.Button("Execute")]]

window = Sg.Window("Remediation Breakdown Tool", layout, size=(1000,500))

while True:
    event, values = window.read()
    if event == "Execute":
        window.close()
        outputbox()

    elif event == Sg.WIN_CLOSED:
        window.close()
        break

