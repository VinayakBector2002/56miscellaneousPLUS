import pickle
def search():
    with open("Cinema.dat","r") as fin:
        while True:
            try:
                rec = pickle.load(fin)
                for i,j,k in list(rec.items()):
                    if k == 'Comedy':
                        print(list(rec.items()))
                        break
            except EOFError:
                break
