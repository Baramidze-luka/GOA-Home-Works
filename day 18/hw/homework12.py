# 13) მომხმარბელს შემოატანინეთ რიცხვი შემდეგ კი მომხმარებლის შემოტანილ რიცხვამდე დაბეჭდეთ მხოლოდ ხუთის ჯერადი რიცხვები 


num = int(input("Enter Number:"))


for i in range (num, 100):
    if i % 5 == 0:
        print(i)