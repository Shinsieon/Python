class Contact:
    def __init__(self, name, phone_number,e_mail, addr):
        self.name= name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        print("Name : " , self.name)
        print("Phone number : ", self.phone_number)
        print("E mail : ", self.e_mail)
        print("Address : ", self.addr)
def set_contact():
    name = input("Name : ")
    phone_number = input("Phone Number : ")
    e_mail = input("E-mail : ")
    addr = input("Address : ")
    contact = Contact(name,phone_number,e_mail,addr)
    return contact
def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()
def run() :
    contact_list = []
    contact = set_contact()
    contact_list.append(contact)
    print_contact(contact_list)

run()