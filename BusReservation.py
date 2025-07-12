class savebusinfo:

    busno = ['']
    arrival = ['']
    type = ['']
    to = ['']
    from_ = ['']
    temp = 1
    tempfornum = 1
    tempforavail = 1
    tempforindex = 1
    yes = "yes"
    no = "no"

    def __init__(self):
        
        self.from_.append("Bhuj")
        self.from_.append("Matana madh")
        self.from_.append("Bhuj")
        self.from_.append("Bhuj")
        self.from_.append("Narayan sarovar")

        self.to.append("Sarangpur")
        self.to.append("Amreli")
        self.to.append("Kodinar")
        self.to.append("Porbandar")
        self.to.append("Ghandhinagar")

        self.type.append("Sleeper")
        self.type.append("Luxary")
        self.type.append("Luxary")
        self.type.append("AC Sleeper")
        self.type.append("Sleeper")

        self.busno.append("GJ-18-Z-9951")
        self.busno.append("GJ-18-Z-9983")
        self.busno.append("GJ-18-Z-8522")
        self.busno.append("GJ-18-Z-7626")
        self.busno.append("GJ-18-Z-9591")

        self.arrival.append("6:30 PM")
        self.arrival.append("9:00 PM")
        self.arrival.append("9:15 PM")
        self.arrival.append("10:00 PM")
        self.arrival.append("7:15 PM")


    def displayinfo(self):

        for i in range(1, 6):

            print(self.temp)
            self.temp += 1
            print(f"{self.from_[i]} to {self.to[i]}")
            print(f"Bus No. : {self.busno[i]}")
            print(f"Type : {self.type[i]}")
            print(f"Arrival time : {self.arrival[i]}")
            print()

class booking(savebusinfo):

    def __init__(self):

        self.avail = ["Available", "Booked"]
        self.booked = [0, 0, 0, 0, 0]

        self.formatname = "First Name"
        self.formatlastname = "Last Name"
        self.formatage = "Age"
        self.formatpno = "Phone No."
        self.formatfrom = "From"
        self.formatto = "To"
        self.formatseatno = "Seat No."
        self.formatticketno = "Ticket No."
        global ticketno
        ticketno = 3

        self.allbusroute = [""]
        self.busroute1 = ["Bhuj", "Anjar", "Adipur", "Ghandhidham", "Bhachau", "Samkhyali", "Malia", "Halvad", "Dangadra", "Sanand", "Ahemdabad", "Ghandhinagar"]
        self.busroute2 = ["Mata Na Madh", "Ravapar", "Nakhatrana", "Bhuj", "Anjar", "Adipur", "Ghandhidham", "Bhachau", "Samakhyali", "Morbi", "Tankara", "Rajkot", "Amreli"]
        self.busroute3 = ["Bhuj", "Anjar", "Adipur", "Ghandhidham", "Bhachau", "Samkhyali", "Morbi", "Tankara", "Junagadh", "Veraval", "Somnath", "Kodinar"]
        self.busroute4 = ["Bhuj", "Anjar", "Adipur", "Ghandhidham", "Bhachau", "Samkhyali", "Morbi", "Dhrol", "Jamnagar", "Lalpur", "Porbandar"]
        self.busroute5 = ["Bhuj", "Anjar", "Adipur", "Ghandhidham", "Bhachau", "Samkhyali", "Malia", "Halvad", "Dangadra", "Sanand", "Ahemdabad", "Ghandhinagar"]

        self.allbusroute.append(self.busroute1)
        self.allbusroute.append(self.busroute2)
        self.allbusroute.append(self.busroute3)
        self.allbusroute.append(self.busroute4)
        self.allbusroute.append(self.busroute5)

    def userchoice(self):

        # self.flagchoice = True
        global choice
        self.choice = int(input("Enter bus info no. to book : "))

        if self.choice > len(self.from_)-1:

            while True:

                self.choice = int(input("plese enter valid input : "))

                if self.choice <= len(self.from_)-1:
                    
                    break

        choice = self.choice

        # while self.flagchoice:
        #     match (self.tempchoice):
        #         case 1:
        #             self.choice = self.tempchoice
        #             self.flagchoice = False
        #         case 2:
        #             self.choice = self.tempchoice
        #             self.flagchoice = False
        #         case 3:
        #             self.choice = self.tempchoice
        #             self.flagchoice = False
        #         case 4:
        #             self.choice = self.tempchoice
        #             self.flagchoice = False
        #         case 5:
        #             self.choice = self.tempchoice
        #             self.flagchoice = False
        #         case _:
        #             self.tempchoice = int(input("Plese enter valid input : "))

    def getfiledata(self):

        global read_lines
        global filebooked
        self.count2 = 1
        filebooked = []
        k = 0
        for i in range(1, 6):
            if i == choice:
                self.f = open(f'bus{i}.txt', 'r')
                read_lines = self.f.readlines()

                self.f.close()

        for j in range(int((len(read_lines)/9))):

            tempbooked = (read_lines[self.count2].split(" "))
            filebooked = filebooked + tempbooked
            self.count2 += 9

        for i in range(len(filebooked)):
            filebooked[k] = int(filebooked[k])
            k += 1

        # global ticketno
        self.f1 = open("ticketno.txt", "r")
        self.ticketno = (self.f1.read())
        print(self.ticketno)
        ticketno = int(self.ticketno)
        print(type(ticketno))


    def dischoice(self):
            
        print("-------------------------------------------")
        print(self.choice)
        print(f"{self.from_[self.choice]} to {self.to[self.choice]}")
        print(f"Bus No. : {self.busno[self.choice]}")
        print(f"Type : {self.type[self.choice]}")
        print(f"Arrival time : {self.arrival[self.choice]}")
        print("-------------------------------------------")
        print()

    def disroute(self):

        # if (self.choice == 1):
        #     print("Mata No Madh\nRavapar\nNakhatrana\nBhuj\nAnjar\nAdipur\nGandhidham\nBhachau\nSamakhyali\nMorbi\nTankara\nRajkot\nAmreli")
        # elif (self.choice == 2):
        #     print("Bhuj\nAnjar\nAdipur\nGandhidham\nBhachau\nSamakhyali\nMorbi\nTankara\nRajkot\nVirpur\nJetpur\nJunagadh\nVeraval\nSomnath\nKodinar")
        # elif (self.choice == 3):
        #     print("Bhuj\nAnjar\nAdipur\nGandhidham\nBhachau\nSamakhyali\nMorbi\nDhrol\nJamnagar\nLalpur\nPorbandar")
        # elif (self.choice == 4):
        #     print("Bhuj\nAnjar\nAdipur\nGandhidham\nBhachau\nSamakhyali\nMalia\nHalvad\nDangadra\nSanand\nAhemdabad\nGandhinagar")
        # elif (self.choice == 5):
        #     print("Bhuj\nAnjar\nAdipur\nGandhidham\nBhachau\nSamakhyali\nMalia\nHalvad\nDangadra\nSanand\nAhemdabad\nGandhinagar")
        # print()

        for i in self.allbusroute[choice]:

            print(f"-> {i}")

        print()

    def seatdis(self):

        for j in range(11):

            for i in range(5):

                central_padding = ('{: ^19}'.format(self.tempfornum))
                print(f'{central_padding}', end = "")
                self.tempfornum += 1

            print()

            for i in range(5):

                # if (self.tempforavail == self.booked[0] or self.tempforavail == self.booked[1] or self.tempforavail == self.booked[2] or self.tempforavail == self.booked[3] or self.tempforavail == self.booked[4]):
                if (self.tempforavail in self.booked) or (self.tempforavail in filebooked):

                    central_padding = ('{: ^19}'.format(self.avail[1]))
                    print(f'{central_padding}', end = "")

                else:

                    central_padding = ('{: ^19}'.format(self.avail[0]))
                    print(f'{central_padding}', end = "")

                self.tempforavail += 1

            print()

        print("\n")

class userinfo(booking):

    def getseatno(self):

        self.flaggetseatno = True
        self.seatno = int(input("Enter total seat to book : "))

        if self.seatno > 5:

            print("------------------------------------")
            print("You can only book maximum \"5\" seats")
            print("------------------------------------")

            while self.seatno > 5:

                self.seatno = int(input("Plese enter the total seat AGAIN! : "))

        print("Enter seat no. to book : ")

        for i in range(self.seatno):

            self.tempadd = int(input(""))

            if (self.tempadd >=1) and (self.tempadd <= 55) and (self.tempadd not in filebooked):

                    self.booked.insert(i, self.tempadd)

            else:

                print("------------------------------------")
                print("INVALID SEAT NO.!!")
                print("------------------------------------")

                while self.flaggetseatno == True:

                    self.tempadd = int(input("PLESE ENTER SEAT NO. AGAIN    : "))

                    if (self.tempadd >=1) and (self.tempadd <= 55) and (self.tempadd not in filebooked):

                        self.booked.insert(i, self.tempadd)
                        self.flaggetseatno = False

        write_lines.append(f"{self.seatno}\n")
        write_lines.append(f"{self.booked[0]} {self.booked[1]} {self.booked[2]} {self.booked[3]} {self.booked[4]}\n")

    def inuserinfo(self):

        print()
        self.name = input("Enter your first name : ")
        self.lastname = input("Enter your last name : ")
        self.age = int(input("Enter your age : "))

        self.pno = int(input("Enter your phone number : "))
        print()

        if len(str(self.pno)) < 10 or len(str(self.pno)) > 10:

            print("------------------------------------")
            print("INVALID PHONE NO.")
            print("------------------------------------")

            while True:

                self.pno = int(input("PLESE ENTER PHONE NO. AGAIN : "))

                if len(str(self.pno)) == 10:

                    print()
                    break

        write_lines.append(f"{self.name}\n")
        write_lines.append(f"{self.lastname}\n")
        write_lines.append(f"{self.age}\n")
        write_lines.append(f"{self.pno}\n")

    def userfrom(self): 

        self.uformindex = 0
        self.flagufrom = 0
        self.ufrom = input("Enter place \'From\' : ")

        for i in self.allbusroute[choice]:

            self.uformindex += 1

            if i.lower() == self.ufrom.lower():

                self.flagufrom = 1
                break

            else:
                self.flagufrom = 0

        if self.flagufrom == 0:

            print("------------------------------------")
            print("INVALID \'FROM\'")
            print("------------------------------------")
            print()


        while self.flagufrom == 0:

            self.uformindex = 0
            self.ufrom = input("Enter valid \'From\' : ")

            for i in self.allbusroute[choice]:

                self.uformindex += 1

                if i.lower() == self.ufrom.lower():
                    self.flagufrom = 1
                    break

        write_lines.append(f"{self.ufrom}\n")

    def userto(self): 

        self.utoindex = 0
        self.flagufrom = 0
        self.uto = input("Enter place \'To\' : ")

        for i in self.allbusroute[choice]:

            self.utoindex += 1

            if i.lower() == self.uto.lower():

                self.flagufrom = 1
                break

            else:
                self.flagufrom = 0

        if self.flagufrom == 0:
            print("------------------------------------")
            print("INVALID \'TO\'")
            print("------------------------------------")
            print()


        while self.flagufrom == 0:

            self.utoindex = 0
            self.uto = input("Enter valid \'To\' : ")

            for i in self.allbusroute[choice]:

                self.utoindex += 1

                if i.lower() == self.uto.lower():

                    self.flagufrom = 1
                    break

        write_lines.append(f"{self.uto}\n")

    def rate(self):

        self.fare = (((self.utoindex - self.uformindex) * 50) + 100) * self.seatno
        print() 
        print("------------------------------------")
        print(f"Your total cost {self.fare}")
        print("------------------------------------")
        print()

        write_lines.append(f"{self.fare}\n")

    def confirmtic(self):

        self.confirm = input("Enter \"YES\" for confirm or \"NO\" : ")
        print()

    def finaldetail(self):

        if self.confirm.lower() == self.yes:
                
            print("------------------------------------")
            right_padding = ('{: <12}'.format(self.formatname))
            print(f'{right_padding}', end = "")
            print(":", self.name.upper())

            right_padding = ('{: <12}'.format(self.formatlastname))
            print(f'{right_padding}', end = "")
            print(":", self.lastname.upper())

            right_padding = ('{: <12}'.format(self.formatage))
            print(f'{right_padding}', end = "")
            print(":", self.age)

            right_padding = ('{: <12}'.format(self.formatpno))
            print(f'{right_padding}', end = "")
            print(":", self.pno)

            right_padding = ('{: <12}'.format(self.formatfrom))
            print(f'{right_padding}', end = "")
            print(":", self.ufrom.upper())

            right_padding = ('{: <12}'.format(self.formatto))
            print(f'{right_padding}', end = "")
            print(":", self.uto.upper())

            right_padding = ('{: <12}'.format(self.formatseatno))
            print(f'{right_padding}', end = "")
            print(": ", end = "")

            for j in range(self.seatno):

                print(self.booked[j], end=",")

            # self.ticket = ticketno

            print()
            right_padding = ('{: <12}'.format(self.formatticketno))
            print(f'{right_padding}', end = "")
            print(":", ticketno)

            ticketno = ticketno + 1

            print()
            print("------------------------------------")
            print()
            print("* Your Ticket is booked *")


                
        elif self.confirm == self.no:

            print("* Your ticket is canceled *")
            exit()

    def printbooked(self):

        for j in range(11):

            for i in range(5):

                central_padding = ('{: ^19}'.format(self.tempfornum))
                print(f'{central_padding}', end = "")
                self.tempfornum += 1

            print()

            for i in range(5):

                # if (self.tempforavail == self.booked[0] or self.tempforavail == self.booked[1] or self.tempforavail == self.booked[2] or self.tempforavail == self.booked[3] or self.tempforavail == self.booked[4]):
                if (self.tempforavail in self.booked) or (self.tempforavail in filebooked):

                    central_padding = ('{: ^19}'.format(self.avail[1]))
                    print(f'{central_padding}', end = "")

                else:

                    central_padding = ('{: ^19}'.format(self.avail[0]))
                    print(f'{central_padding}', end = "")

                self.tempforavail += 1

            print()

        print("\n")

class saveuserfile(booking):

    def writefile(self):

        for i in range(1, 6):
            if i == choice:
                self.f = open(f'bus{i}.txt', 'a')
                self.f.writelines(write_lines)

                self.f.close()

        self.f = open('ticketno.txt', 'w')
        self.f.write(str(ticketno))
            

a = savebusinfo()
b = booking()
c = userinfo()
d = saveuserfile()
write_lines = []
flag = True


while flag:
    a.displayinfo()
    b.userchoice()
    b.dischoice()
    b.getfiledata()
    b.disroute()
    temp = input("Press enter to continue!")

    if temp == "":
        b.seatdis()

    c.getseatno()
    c.inuserinfo()
    c.disroute()
    c.userfrom()
    c.userto()
    c.rate()
    c.confirmtic()
    c.finaldetail()
    temp = input("Press enter to continue!")

    if temp == "":
        c.printbooked()

    temp2 = input("Press enter to book again or \'NO\' : ")
    temp2.lower()

    if temp2 == "no":
        flag = False

    d.writefile()
        