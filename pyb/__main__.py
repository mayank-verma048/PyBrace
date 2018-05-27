import argparse as ap


def main():
 p = ap.ArgumentParser(description = 'Transpile PyBrace files to vanilla Python scripts')
 p.add_argument('target',help='File to be transpiled')
 p.add_argument('indent',nargs='?',default = 6,help = 'No of spaces to indent with. Default is 6.')
 args = p.parse_args()
 
 I = int(args.indent)

 target = open(args.target)
 content = target.readlines()
 if(args.target[-3:] != 'pyb'):
  print 'Error: Wrong extension.\nExiting.'
  exit()
 else:
  dest = open(args.target.rstrip('b'),'w')
 sline_count = 0
 mline_count = 0
 sline = False
 mline = False
 prev = 'nil'
 prev2 = 'nil'
 indent = 0

 for line in content:
  for c in line:

   if( c == '#' and not (sline or mline)): break

   if( c == '\''):
    #print 'prev:'+prev
    if(prev == '\'' and prev2 != '\\'):
     sline_count = 0
     sline = False
     mline_count += 1
    elif(prev == '\'' and prev2 == '\\'):
     pass
    else:
     sline_count = 1
     mline_count = 1

    if(sline_count == 1):
     if(sline == False): sline = True
     else: sline = False

    if((mline_count % 3) == 0 and mline_count != 0):
     if(mline == False): mline = True
     else: mline = False
     
   if( c == '"'):
    if(prev == '"' and prev2 != '\\'):
     sline_count = 0
     sline = False
     mline_count += 1
    elif(prev == '"' and prev2 == '\\'):
     pass
    else:
     sline_count = 1
     mline_count = 1

    if(sline_count == 1):
     if(sline == False): sline = True
     else: sline = False

    if((mline_count % 3) == 0 and mline_count != 0):
     if(mline == False): mline = True
     else: mline = False
   
   prev2 = prev
   prev = c


  if(line.strip()[-2:] == ':{' and not(sline or mline)):
   o =  ' '*I*indent+line.lstrip().rstrip('{\n')
   dest.write(o)
   dest.write('\n')
   indent +=1
  elif(line.strip() == '}' and not(sline or mline)):
   o = ' '*I*indent+line.lstrip().rstrip('}\n')
   dest.write(o)
   dest.write('\n')
   indent -=1
  else:
   o = ' '*I*indent+line.lstrip().rstrip('\n')
   dest.write(o)
   dest.write('\n')
  #print indent,sline_count,sline,mline_count,mline,line[-3:]

 if(indent != 0):
  print 'No of open and close braces don\'t match.\nUndefined behavior'
 target.close()
 dest.close()



if __name__ == '__main__':
 main()
