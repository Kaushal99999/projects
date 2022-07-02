from random import randint
print("Hello welcome to Rock Paper and Scissors")
p_w=0
c_w=0
win_s=3
while(p_w<win_s and c_w<win_s):
	c1=input("Enter your choice player.Enter quit to forfeit").lower()
	if c1=="quit":
		break
	rand_num=randint(0,2)
	if rand_num==0:
		c2="rock"
	elif(rand_num==1):
		c2="scissor"
	else:
		c2="paper" 
	print(f"computer picks{c2}")
	if(c1!=c2):
		if((c1=="rock" and c2=="scissor") or(c1=="scissor" and c2=="paper") or (c1=="paper"and c2=="rock")):
			print("You win")
			p_w+=1
			print(f"Your score:{p_w},Computer score:{c_w}")
		else:
			print("Computer wins")
			c_w+=1
			print(f"Your score:{p_w},Computer score:{c_w}")
	else:
		print("It's a tie")
		print(f"Your score:{p_w},Computer score:{c_w}")


if(p_w>c_w):
	print("Congratulations you won the game")
elif(p_w==c_w):
	print("It's a tie")
else:
	print("Sorry You lost the game")