# Write a program that reads multiple lines of input from the user until they 
# enter an empty line, then prints all the lines.

def main():
    lines = []
    
    print("Enter your lines of text (press Enter to finish):")
    
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    print("\nYou entered:")
    for line in lines:
        print(line)

if __name__ == "__main__":
    main()
