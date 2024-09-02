import sys
import unicodedata
from tabulate import tabulate

unicodeList = [chr(i) for i in range(1000000) if chr(i).isprintable() and not chr(i).isspace()]
unicodeList[0:25] = unicodeList[15:25] + list(' ') + unicodeList[0:14]


def main():
  unicodeList = [chr(i) for i in range(1000000) if chr(i).isprintable() and not chr(i).isspace()]
  unicodeList[0:25] = unicodeList[15:25] + list(' ') + unicodeList[0:14]
  if len(sys.argv) == 1:
    query(unicodeList)
  else:
     option = sys.argv[1]
     option = option.strip()
     value = sys.argv[2]
     value = value.strip()
     match option:
        case "1":
            print(convertToBase(value, unicodeList))
        case "2":
            print(convertToDenary(value, unicodeList))
        case "3":
            print(digitInfo(value, unicodeList))
        case _:
            pass

def query(unicodeList):
    while True:
        option = input("Select an option (or quit with !):\n1 for base10 to base144515\n2 for base144515 to base10\n3 for querying base144515 values\n")
        option = option.strip()
        if option == "!":
            break
        value = input("Select a value: ")
        match option:
            case "1":
                print(convertToBase(value, unicodeList))
            case "2":
                print(convertToDenary(value, unicodeList))
            case "3":
                print(digitInfo(value, unicodeList))
            case _:
                pass

def convertToBase(value, characters):
  totalNum = ""
  value = int(value)

  while value > 0:
    index = value % 144515
    value = value // 144515
    nextDigit = characters[index]
    totalNum += nextDigit

  totalNum = totalNum[::-1]
  return totalNum

def convertToDenary(value, characters):
  multiplier = 1
  totalNum = 0
  value = str(value)
  value = value[::-1]

  for x in range(len(value)):
    index = characters.index(value[x])
    totalNum += index * multiplier
    multiplier = multiplier * 144515

  return totalNum

def digitInfo(value, characters):
  value = sorted(list(set(list(value))))
  charList = []
  for x in range(len(value)):
    charName = unicodedata.name(value[x])
    charUniId = f"U+{ord(value[x]):04x}"
    try:
      charValue = characters.index(value[x])
    except:
      charValue = "not in base 144515"
    charList.append([charName, charUniId, charValue])

  return tabulate(charList, headers=["name", "id", "value in base144515"], tablefmt="grid")

if __name__ == "__main__":
    main()
