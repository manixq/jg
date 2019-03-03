text = input("Enter text: ")
endtext = []
for t in text:
	if t ==" ":
		endtext.append("   ")
	else:
		endtext.append(":regional_indicator_" + t + ": ")

print("".join(endtext))