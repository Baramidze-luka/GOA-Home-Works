# 3)
# შეამოწმეთ, არის თუ არა მოცემული ციფრი დადებითი ან ნული, თუმცა არ არის უარყოფითი.

num = int(input("Enter Number:"))

if num >= 0:
    print("დადებითია")
elif num < 0:
    print("უარყოფითია")