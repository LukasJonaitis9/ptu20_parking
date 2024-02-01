import PySimpleGUI as sg

##tarifu listas(list /create/ update /delete)
##cars list(list/ create/ delete)
##arrival(choose/create car; create parking entry with  datetime.now() as arival time)
##departure (chose from cars without departure,
    ##update parking entry with datetime.now() as departure time, 
    ##calculate total_price)
##reports
    ##find parking bills by specific cars
    ##total parking revenue by between dates with list
## main window
main_layout = [
    [
        sg.Button('Tariffs,', key='-TARIFFS-', size = 10),
        sg.Button('Cars,', key='-CARS-', size = 10),
     ],
     
        [
        sg.Button('Arrivals,', key='-ARRIVALS-', size = 10),
        sg.Button('Departure,', key='-DEPARTURE-', size = 10),
     ],

         [
        sg.Button('Reports,', key='-REPORTS-', size = 21),
        
     ],
]
main_window = sg.Window('Parking PTU20', main_layout, font = 'sans-serif 20', element_justification='center', size = 400, 300)

while True:
    event, vlues = main_window.read()
    if event == sg.WIN_CLOSED:
        break