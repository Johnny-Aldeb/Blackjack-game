
import random


cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def play():
  me = random.choices(cards, k=2)
  computer = random.choices(cards, k=2)


  print(f"your cards are: {me} ")
  print(f"computer card are: {computer} ")

  isd = True
  total_me =0
  total_computer = 0

  for num in me:
      total_me += num
  for num2 in computer:
      total_computer += num2

  while isd:
    hit = input("\npress 'y' if you want another card, or 'n' to stand: ")

    if hit == "n":


      if total_me > 21:
        print("\ncomputer win\n")
      if total_computer >21:
        print("\nyou win\n")
        continue

      if total_me > total_computer:
        print("\nyou win\n")
        isd = False
        play()
      else:
        print("\ncomputer win\n")
        isd = False
        play()

    else:
      x= random.choice(cards)
      me.append(x)
      print(f"your cards are: {me} ")



      total_me += x



      if total_computer < 12:
        y=random.choice(cards)
        computer.append(y)
        total_computer += y

      print(f"computer card are: {computer}")

      if total_me > 21:
        print("\ncomputer win\n")
        isd = False
        play()

      if total_computer > 21:
        print("\nyou win\n")
        isd = False
        play()


play()