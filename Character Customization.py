print("This is a character customization simulator!")
gender =input("Choose your gender(male,female): ")
age=int(input("Choose your age:"))
name=input("What is your name ")
height=float(input("How tall are you(feat,inch) "))
hairstyle=input("What hair style would you like ")
haircolour=input("What colour is your hair ")
eye=input("What eye colour would you like ")
top=input("What do you want to wear on top ")
topcolour=input("What colour top do you want ")
bottom=input("What bottom would you like to wear ")
bottomcolour=input("What Colour do you want your bttom to be ")
shoe=input("what footwear do you want to wear ")
if gender=="male ":
    Tattoo=input("what tattoo do you want ")
else:
    Makeup=input("Do you want makeup(y/n) ")
    if Makeup=="y":
        makeup2=input("What makeup do you want ")
print("I am ",name, ",and I am a ",gender, "who is ",age,"years old and my height is",height,".")
print("I have ",hairstyle,"which is",haircolour,"and my eyes are",eye,"in colour")
print("I am wearing a ",top,"which is ",topcolour,"and a ",bottom,"which is ",bottomcolour,".I am wearing ",shoe,)
if gender=="male ":
    print("I have a ",Tattoo,"for a tattoo")
if gender=="female":
    print("I have ",makeup2,"on")





