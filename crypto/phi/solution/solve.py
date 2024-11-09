from Crypto.Util.number import *

N=45109760255834684754983589295969725310626328534802429650039558168167072337918473534586289686536635992885101263834302951907737904559260123769463991894980774542481
e=65537
Cipher= 37358207842489278501844590204436061248784995840567905372310756710267273487596583866873282674084579361285279392052165188243528456115376968934859883995305365787773
# use https://factordb.com/ or https://www.alpertron.com.ar/ECM.HTM to factorize N
phi= (865092131**2)*( 865092131- 1)* (567438481 - 1)*( 606925769 - 1)*( 616037419 - 1)*( 632480843 - 1)*( 717907921 - 1)*( 830813623 - 1)*( 842597461 - 1)*( 878387431 - 1)*( 926136593 - 1)*( 957106811 - 1)*( 1046408651- 1)*( 1058492087- 1)*( 1058962693- 1)*( 1061140099- 1)*( 1066149767 - 1)
d= inverse(e, phi)
flag= pow(Cipher, d, N)
print(long_to_bytes(flag))