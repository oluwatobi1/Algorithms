
def decrypt(word):
  # 97-122
  # [int of ascii value]
  # ord(a)=97
  out = ''
  
  ascii_values = []
  for i in word:
    ascii_values.append(ord(i))
  prev = 1
  temp = 0
  for i in range(len(ascii_values)):
    temp = ascii_values[i]
    ascii_values[i]-=prev
    while ascii_values[i]<97:
      ascii_values[i]+=26
    prev = temp
    out+=chr(ascii_values[i])
  return out


print(decrypt('dnotq'))
