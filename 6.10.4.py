class InvitedList:

    def __init__(self):
        self.list_of_guests = []

    def add_guest(self, name, city, status):
        self.name = name
        self.city = city
        self.status = status
        self.guest = f'{self.name}, г. {self.city}, статус {self.status}'
        print(self.guest)
        return self.list_of_guests.append(self.guest)

    def show_list(self):
        return self.list_of_guests


list1 = InvitedList()
list1.add_guest('Tom Cruse', 'Los Angeles', 'Trainer')
list1.add_guest('Boris Johnson', 'London', 'Coach')
print(list1.show_list())