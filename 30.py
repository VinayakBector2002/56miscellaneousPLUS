import pickle
import os
print(" telephone directory program")
while True:
    print(" 1) Add New Record \n 2) Display All Records \n 3) Search Telephone Number \n 4) Search Name \n 5) Update Telephone Number \n 6) Delete a record ")
    options=int(input("Enter one of the options"))
    if options == "5":
        fin = open("Records.dat", "rb+")
        while True:
            try:
                pos = fin.tell()
                rec = pickle.load(fin)
                if rec['number']== int(input("number to be changed")):
                    rec['number'] = int(input("New number"))
                    fin.seek(pos)
                    pickle.dump(rec, fin)

            except EOFError:
                break
        print("Record Updated")
        fin.close()

    elif options == "2":
        fin = open("Records.dat",'rb')
        while True:
            try:
                rec = pickle.load(fin)
                print(rec)
            except EOFError:
                break
        fin.close()
    elif options == "3":
        fin = open("Records.dat",'rb')
        while True:
            try:
                rec = pickle.load(fin)
                for i,j in list(rec.items()):
                    if j == int(input("Enter number to be searched")):
                        print(list(rec.items()))
                        break
            except EOFError:
                break
        fin.close()

    elif options == "4":
        fin = open("Records.dat",'rb')
        while True:
            try:
                rec = pickle.load(fin)
                for i,j in list(rec.items()):
                    if i == int(input("Enter name to be searched")):
                        print(list(rec.items()))
                        break
            except EOFError:
                break
        fin.close()

    elif options == "1":
        d = {}
        for i in range(int(input("number of records to be added"))):
            name = input("name of the person")
            number = int(input("The number to be added"))
            d[name]= number

        fout = open("Records.dat", 'wb')
        pickle.dump(d, fout)
        fout.close()

    elif options == "6":
        fin = open("Records.dat", "rb")
        fout = open("temp.dat", "wb")
        while True:
            try:
                rec = pickle.load(fin)
                if rec['number'] == int(input("Number to be deleted ")):
                    pass
                else:
                    pickle.dump(rec,fout)
            except EOFError:
                break
        fin.close()
        fout.close()
        os.remove("Records.dat")
        os.rename("temp.dat","Records.dat")
        print("Record deleted")

    else:
        continue 