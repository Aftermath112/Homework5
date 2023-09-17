from collections import UserDict


class Field:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value=None):
        super().__init__(value)
        self.validate_phone()

    def validate_phone(self):
        if self.value and (not self.value.isdigit() or len(self.value) != 10):
            raise ValueError("Phone number should consist of 10 digits.")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone_obj = Phone(phone)
        self.phones.append(phone_obj)

    def remove_phone(self, phone):
        for phone_obj in self.phones[:]:
            if phone_obj.value == phone:
                self.phones.remove(phone_obj)

    def edit_phone(self, old_phone, new_phone):
        validation = Phone(new_phone)
        for phone_obj in self.phones:
            if phone_obj.value == old_phone:
                phone_obj.value = new_phone
                return
        raise ValueError

    def find_phone(self, phone):
        phone_obj = Phone(phone)
        for p in self.phones:
            if p.value == phone_obj.value:
                return p
        return None

    def __str__(self):
        phone_str = "; ".join(map(str, self.phones))
        return f"Name: {self.name}, Phones: {phone_str}"


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]


if __name__ == "__main__":
    address_book = AddressBook()

    while True:
        command = input("Enter a command: ").strip().lower()

        if command == "add":
            name = input("Enter name: ")
            record = Record(name)
            while True:
                phone = input("Enter phone (or leave empty to finish): ").strip()
                if not phone:
                    break
                try:
                    record.add_phone(phone)
                except ValueError as e:
                    print(e)
            address_book.add_record(record)
        elif command == "find":
            name = input("Enter name to find: ")
            record = address_book.find(name)
            if record:
                print(record)
            else:
                print("Contact not found.")
        elif command == "delete":
            name = input("Enter name to delete: ")
            address_book.delete(name)
        elif command == "exit":
            break
        else:
            print("Invalid command. Try again.")
