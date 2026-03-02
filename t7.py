import os
try:
	with open("sample.txt","rt") as sam:
		a=sam.readline()
		b=sam.readline().strip("\n")
		
	if os.path.exists("sample.txt"):
		print(f"Reading file content: \nLine 1: {a}Line 2: {b}")
except FileNotFoundError:
	raise OSError("The file 'sample.txt' was not found.")

