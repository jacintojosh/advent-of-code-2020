import re

f = open('input.txt', 'r')
data = [line.strip('\n') for line in f]

# Part1
def countValidPassports(data):
  expectedFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
  numValidPassports = 0
  fieldCheck = expectedFields.copy()
  for line in data:
    if line != '':
      if len(line.split(' ')) > 1:
        for field in line.split(' '):
          key = field.split(':')[0]
          if key in fieldCheck:
            fieldCheck.remove(key)
      else:
        key = line.split(':')[0]
        if key in fieldCheck:
            fieldCheck.remove(key)
    else:
      if not fieldCheck:
        numValidPassports+=1
      fieldCheck = expectedFields.copy()

  return numValidPassports

# Part2
def countNumberValidatedPassports(data):
  expectedFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
  numValidPassports = 0
  fieldCheck = expectedFields.copy()
  for line in data:
    if line != '':
      if len(line.split(' ')) > 1:
        for field in line.split(' '):
          key, value = field.split(':')
          if key in fieldCheck and isFieldValid(key, value):
            fieldCheck.remove(key)
      else:
        key, value = line.split(':')
        if key in fieldCheck and isFieldValid(key, value):
            fieldCheck.remove(key)
    else:
      if not fieldCheck:
        numValidPassports+=1
      fieldCheck = expectedFields.copy()

  return numValidPassports

def isFieldValid(field, value):
  eyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
  if field == 'byr':
    val = numerize(value)
    if val: return (len(value) == 4 and val >= 1920 and val <= 2002)
    else: return False
  elif field == 'iyr':
    val = numerize(value)
    if val: return (len(value) == 4 and val >= 2010 and val <= 2020)
    else: return False
  elif field == 'eyr':
    val = numerize(value)
    if val: return (len(value) == 4 and val >= 2020 and val <= 2030)
    else: return False
  elif field == 'hgt':
    measurement = re.search('cm\Z|in\Z', value)
    if measurement: measurement = measurement.group()
    else: return False
    val, _ = value.split(measurement)
    val = numerize(val)
    cm = (measurement == 'cm')
    if val: return (val >= 150 and val <= 193 if cm else val >= 59 and val <= 76)
    else: return False
  elif field == 'hcl':
    _, hashT, hcl = value.partition('#')
    if not re.search("[G-Zg-z]", hcl): return (hashT == '#' and len(hcl) == 6)
    else: return False
  elif field == 'ecl':
    return (value in eyeColors)
  elif field == 'pid':
    val = numerize(value)
    if val: return (len(value) == 9)
    else: return False

def numerize(string):
  if not re.search("[a-zA-Z#]", string): return int(string)
  else: return None

print(countValidPassports(data))
print(countNumberValidatedPassports(data))