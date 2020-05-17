import random
target_num=random.randint(1,10)
guess_num=0
while target_num!=guess_num:
  guess_num=int(input("Enter the gussed value you want between 1 to 10:"))
  if target_num==guess_num:
    print(target_num,"HurrAY!!!!!!your guess is right!")
