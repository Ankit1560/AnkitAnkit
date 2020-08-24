import pickle
L=[]
ans="y"
change=input("Enter 'S' if you have sold an item; 'B' if you have got some new stock : ")
myfile=open("chem.dat","rb+")
try:
            while change in "SB":
                 
          
                  if change=="S":
                          while ans=="Y" or ans =="y":
                              rpos=myfile.tell()
                              N=input("Enter the Name of your chemist shop : ")
                              M=input("Enter the name of the medecine you have sold : ")
                              Q=int(input("Enter the quantity of the medicine sold : "))
                              W={M:Q}
                              L=pickle.load(myfile)
                              for i in L:
                                  if i[0]==N:
                                        i[3][M]-=Q
                                        myfile.seek(rpos)      
                                        pickle.dump(L,myfile)
                              ans=input("If you have sold another item, enter 'Y', else any key : ")
                          
                  elif change=="B": 
                       while ans=="Y" or ans =="y":
                              rpos=myfile.tell() 
                              N=input("Enter the Name of your chemist shop : ")
                              M=input("Enter the name of the medecine you have sold : ")
                              Q=int(input("Enter the quantity of the medicine sold : "))
                              L=pickle.load(myfile)
                              for i in L:
                                  if i[0]==N:
                                        i[3][M]+=Q
                                        myfile.seek(rpos)
                                        pickle.dump(L,myfile)
                              ans=input("If you have sold another item, enter 'Y', else any key : ")           
                  else : 
                       print("ivalid choice!! you have to enter 'B' or 'S'")  
                  change=input("if you want to make another change:Enter 'S' if you have sold an item; 'B' if you have got some new stock; Else press any key : ")          
                  
            print(L)
                
except EOFError:
            
            myfile.close()
           
        
    
        
                
                
    