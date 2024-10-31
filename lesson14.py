class Criminal:
    def __init__(self, name, id_number, crime, gender ):
        self.name = name
        self.id_number = id_number
        self.crime = crime
        self.gender = gender
    def show_details(self):
        print(f"Name: {self.name} \nID no: {self.id_number}\nIssue: {self.crime}\nGender: {self.gender}")

c1 = Criminal(name = "john", id_number ="656565", crime ="stealing books", gender= "male")
c1.show_details()