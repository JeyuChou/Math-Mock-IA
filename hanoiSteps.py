import matplotlib.pyplot as plt

#num = number of disks
#initial = initial position
#helper = the middle peg that'll handle n-1 peg
#target = the last peg
#for the n-1 peg, the target peg becomes the helper peg

def hanoi(num,original_num,i,aux,final):
  if num ==1:
    print(f'move disk 1 from rod {str(i)} to rod {str(final)}')
    temp = original_num-1
    return 2*(2**temp)-1
  else:
    hanoi(num-1,original_num,i,final,aux)
    print(f'move disk {str(num)} from rod {str(i)} to rod {str(final)}')
    hanoi(num-1,original_num,aux,i,final)
if __name__=='__main__':
  num = int(input('how many disks do you have? \t'))
  hanoi(num,num,'A','B','C')
