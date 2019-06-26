tickets = {}

def upload_data(name): # Заполняет импортированными данными словарь tickets
    global tickets
    with open(name) as file:
        k = 0
        for line in file:
            if k == 0: # Не рассматривает 1 строчку, показывающую столбцы
                k += 1
            else:
                try:
                    array = line.split(',')
                    array[-1] = array[-1][:-1]
                    country_key = array[2].lower() + '-' + array[3].lower()
                    date_key = array[4][:10]
                    array = array[4:]
                    array[3] = float(array[3])

                    if not country_key in tickets.keys():
                        tickets[country_key] = {date_key: [array]}
                    else:
                        if not date_key in tickets[country_key].keys():
                            tickets[country_key][date_key] = [array]
                        else:
                            if not array in tickets[country_key][date_key]:
                                tickets[country_key][date_key].append(array)
                except:
                    pass


def sorting_data(): # Сортировка пузырьком
    global tickets
    for country_key in tickets.keys():
        for date_key in tickets[country_key].keys():
            for i in range(len(tickets[country_key][date_key]) - 1):
                for j in range(len(tickets[country_key][date_key]) - i - 1):
                    if tickets[country_key][date_key][j][3] > tickets[country_key][date_key][j + 1][3]:
                        tickets[country_key][date_key][j], tickets[country_key][date_key][j + 1] = \
                        tickets[country_key][date_key][j + 1], tickets[country_key][date_key][j]
