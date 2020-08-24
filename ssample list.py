import pickle 
with open("chem.dat","wb") as myfile:

        ch=[["Rajac",15,"op",{"Para":20,"Cal4U":40,"Ibujesic":35}],["medi",40,"cl",{"Cal4U":30,"Ibujesic":45,"Para":20}],["life",35, "op" ,{"Ibujesic":25, "Cal4U":10, "Para":50}] ]
        pickle.dump(ch,myfile)
myfile.close()