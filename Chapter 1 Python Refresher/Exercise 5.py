count = 0  

while True:
    yes = input("Do you want to continue? (Y/N): ")
    
    if yes == "Y" or yes == "y":
        count += 1
    elif yes == "N" or yes == "n":
        break 
    else:
        print("Error only use Y or N")

print(f"The loop was executed {count} times.")