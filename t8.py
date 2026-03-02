a = input("Enter text to write to the file: ")

with open("output.txt","at") as o:
	o.write(a)
	o.write("\n")
	
print("Data successfully written to output.txt.\n")

b = input("Enter additional text to append: ")

with open("output.txt","at") as u:
	u.write(b)
	u.write("\n")

print("Data successfully appended.\n")

with open("output.txt","rt") as r:
	c=r.readline()
	d=r.readline().strip("\n")
	
print(f"Final contents of the output.txt: \n{c}{d}")
