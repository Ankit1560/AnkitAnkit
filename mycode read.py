import pickle
myfile=open("chem.dat","rb")
L=[]
try:
    while True:
        L=pickle.load(myfile)
        print(L)
      
    
except EOFError:
    myfile.close()  
