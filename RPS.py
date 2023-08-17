import random

inputs=["rock","paper","scissor"]
print("""
    -------------------------------------
                ROCK PAPER SCISSOR
    -------------------------------------    
      
      """)
#player one
p1=0
p2=0

def player1():
   
    while True:
        try:
            x= input("Please choose an option Rock ,Paper ,Scissor")
            x=x.lower()
            list1=['rock','paper','scissor']
            if x not in list1:
                raise ValueError
            else:
                break

        except ValueError as v:
            print("please enter a valid option")
    
    
    
    return x     
        
        

# x=player1()

def computer():
    y=random.choice(inputs)
    return y

# y=computer()

        
        
while True:
    print("""
          1)PLAY - >
          2)END - x
          """)     
    
    op=int(input("----->"))  
    
    if op==1:
        x=player1()
        y=computer()
        print('You choose ', x)
        print('Computer choose',y)
        
        if x==y:
            print("!!!!  >> DRAW <<  !!!!")
        elif x=="rock" and y=="paper" :
            print(">>>>> COMPUTER WIN  <<<<<<")
            p2=p2+1
        elif x=="rock" and y=="scissor": 
            print(">>>>> PLAYER 1 WIN  <<<<<<")
            p1=p1+1
        elif x=="paper" and y=="rock":
            print(">>>>> PLAYER 1 WIN  <<<<<<")
            p1=p1+1
        elif x=="paper" and y=="scissor":
            print(">>>>> Computer WIN  <<<<<<")
            p2=p2+1
        elif x=="scissor" and y=="paper":
            print(">>>>> PLAYER 1 WIN  <<<<<<")
            p1=p1+1
        elif x=="scissor" and y=="rock":
            print(">>>>> Computer WIN  <<<<<<")
            p2=p2+1
    elif op==2:
        if p1>p2:
            print(f"""
                    !> PLAYER 1 is the WINNER <!
                            SCORE : {p1}
                  """)
                 
            break
        elif p1<p2:
            print(f"""
                    !> COMPUTER is the WINNER <!
                            SCORE :{p2}
                  """)
            
            break
        else:
            print(">>>>>>> NO WINNERS <<<<<<<") 
            break
            
    
    
         
                 
         



