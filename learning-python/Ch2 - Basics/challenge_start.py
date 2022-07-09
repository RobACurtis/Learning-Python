# define a function
# convert string to lowercase
# reverse word and test if equal to original string
# need to remove punctuation and spaces
# need to work with numbers or convert number to string... str()


def main():
  string=input("Enter String to test for palindrome or 'exit':")
  string = str(string).lower()
  new_string = ''.join(char for char in string if char.isalnum())
  if new_string== 'exit':
    return
  elif new_string == new_string[::-1]:
    print("Palindrome test:",True)
  else:
    print("Palindrome test:",False)

if __name__ == "__main__":
  main()
