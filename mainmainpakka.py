dtmak()
ans="y"
change="S"

while change in "SB": 
    
              change=input("if you want to make a change:Enter 'S' if you have sold an item; 'B' if you have got some new stock; Else press any key : ") 
             
                        
              if change=="S":
                      
                      while ans=="Y" or ans =="y":
                          
                          N=input("Enter the Name of your chemist shop : ")
                          M=input("Enter the name of the medecine you have sold : ")
                          Q=int(input("Enter the quantity of the medicine sold : "))
                          
                          
                          for i in L:
                              if i[0]==N:
                                    i[3][M]-=Q
                                    
                                    
                                
                                   
                          ans=input("If you have sold another item, enter 'Y', else any key : ")
                      
              elif change=="B": 
                   
                   while ans=="Y" or ans =="y":
                      
                          N=input("Enter the Name of your chemist shop : ")
                          M=input("Enter the name of the medecine you have sold : ")
                          Q=int(input("Enter the quantity of the medicine sold : "))
                          
                          for i in L:
                              if i[0]==N:
                                    i[3][M]+=Q
                                    
                          ans=input("If you have sold another item, enter 'Y', else any key : ")         
              else : 
                   
                   print("Updation Completed!!")  
                   
              ans="y"
      
print(L)
                

           
        
    
        
                
                
    
