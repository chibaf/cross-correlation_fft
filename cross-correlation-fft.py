import numpy as np
import sys
import matplotlib.pyplot as plt

def find_index(c):
  mc=np.amax(c)
  for i in range(len(c)):
    if c[i]==mc:
      im=i
      break
  return im

m=np.loadtxt(sys.argv[1],delimiter=',')  # convert a csv file to a matrix from file sys.argv[1]

mt=m.T #transpose matrix

#computing cross-correlation
v1=mt[1][10000:15000];v2=mt[2][10000:15000]
c=1.0/(np.linalg.norm(v1)*np.linalg.norm(v2))   # added on 16.Sep.2021
corr=np.empty(0)   #make nd.array of length zero
corr=np.append(corr,np.dot(v1,v2)*c)  # the first element of corr, modified on 16.Sep.2021
for i in range(1,len(v1)):
  v2=np.roll(v2,1)  # shift 1 to the right
  corr=np.append(corr,np.dot(v1,v2)*c)   # cross correlation, modified on 16.Sep.2021
print(np.amax(corr))
print(find_index(corr))

# plot the result
x=range(len(corr)) #plot array
plt.plot(x,corr)
plt.show()

v1=mt[1][10000:15000];v2=mt[2][10000:15000]
c=1.0/(np.linalg.norm(v1)*np.linalg.norm(v2)) 
fft_len=13
f1=np.fft.fft(v1)
f2=np.fft.fft(v2)
ff=f1*f2
corrf=np.real(np.fft.ifft(ff))*c
print(np.amax(corrf))
print(find_index(corrf))

x=range(len(corrf)) #plot array
plt.plot(x,corrf)
plt.show()

exit()
#output the result to file sys.argv[2]
#f = open(sys.argv[2], 'w') 
#st=str(corr[0])
#for i in range(1,len(corr)):
#  if i!=(len(corr)-1):
#    st=st+","+str(corr[i])
#  else:
#    st=st+str(corr[i])+"\n"
#f.write(st)
#f.write(str(ix))
#f.close()

