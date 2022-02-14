tag=input()
n=len(tag)
sum12=int(tag[0])+int(tag[1])
sum45=int(tag[3])+int(tag[4])
sum56=int(tag[4])+int(tag[5])
sum89=int(tag[7])+int(tag[8])
if(tag[2]!='A' and tag[2]!='E' and tag[2]!='I' and tag[2]!='O' and tag[2]!='U' and tag[2]!='Y'  
   and sum12%2==0 and sum45%2==0 and sum56%2==0 and sum89%2==0):
  print("valid")
else:
  print("invalid")
