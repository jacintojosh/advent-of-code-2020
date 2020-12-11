f = open('input.txt', 'r')
passwords = [line.strip('\n') for line in f]

# Part1
def getNumPasswordsWithValidNumChars(passwords):
  validPass = 0
  for password in passwords:
    minChar, maxChar, char, passwordToCheck = getPasswordParams(password)
    charsInPass = 0
    for c in passwordToCheck:
      if c == char:
        charsInPass += 1
    if charsInPass >= minChar and charsInPass <= maxChar:
      validPass+=1
  return validPass

def getPasswordParams(password):
  minChar, _, cut = password.partition('-')
  maxChar, _, cut = cut.partition(' ')
  char, _, passwordToCheck = cut.partition(': ')
  return int(minChar), int(maxChar), char, passwordToCheck

# Part2
def getNumPasswordsWithValidPosChars(passwords):
  validPass = 0
  for password in passwords:
    minChar, maxChar, char, passwordToCheck = getPasswordParams(password)
    if passwordToCheck[minChar - 1] == char and passwordToCheck[maxChar - 1] == char:
      continue
    elif passwordToCheck[minChar - 1] == char or passwordToCheck[maxChar - 1] == char:
      validPass+=1
  return validPass

print(getNumPasswordsWithValidNumChars(passwords))
print(getNumPasswordsWithValidPosChars(passwords))