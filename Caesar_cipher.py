
def Encrypt(text):
  
   
   
    # take a string from user and represent next 3rd value 
    n=field1.get()
   
    sz=len(n)
    char=[] 
    for i in range(0,sz):
        ascii=ord(n[i])
        # print(f"ascii of {n[i]} is {ascii}")
        ascii=ascii+3
        if (ascii >= 90 and n[i].isupper()) or (ascii >= 122 and n[i].islower()):
            if n[i].isupper():
                
                ascii=ascii-26
            
            elif n[i].islower():
            
                ascii=ascii-26
    

        char.append(chr(ascii))
    t_val=""
    
    for i in char:
       t_val=t_val+i
    
       en_var.set(t_val)
 
        




def Decrypt(value):
    # take a string from user and represent last 3rd values
   
    n=field1.get()
    sz=len(n)
    char=[] 
    for i in range(0,sz):
        ascii=ord(n[i])
        # print(f"ascii of {n[i]} is {ascii}")
        ascii=ascii-3
        if (ascii <= 64 and n[i].isupper()) or (ascii <= 96 and n[i].islower()):
            if n[i].isupper():
                
                ascii=ascii+26
            
            elif n[i].islower():
            
                ascii=ascii+26
    

        char.append(chr(ascii))
    t_val=""
    for i in char:
        t_val=t_val+i
        en_var.set(t_val)
    
    
    
    
    
    
    
import tkinter as tk

root=tk.Tk()
root.title("Caesar Cipher Converter")                                           #for setting title of screen
root.configure(bg="#08115c")                                                    # for setting color 
root.geometry("500x500")
en_var=tk.StringVar()


label1=tk.Label(root,text="Caesar Cipher",font=("Calibri",18,"bold"),bg="#08115c" , foreground="white")
label1.pack(pady=10)   #this will make label visible

field1=tk.Entry(background="#79abd9",foreground="white",font=("Calibri",18,"bold"),textvariable=en_var)
field1.place(height=300,width=400,x=50,y=60)

value=field1.get()
btn=tk.Button(root,bg="#79abd9",text="Encrypt",command=lambda:Encrypt(value))
btn.place(x=50,y=400,width=150,height=40)
value=field1.get()
btn=tk.Button(root,bg="#79abd9",text="Decrypt",command=lambda: Decrypt(value))
btn.place(x=300,y=400,width=150,height=40)



root.mainloop()                                                      #for displaying frame 