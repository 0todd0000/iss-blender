
s = '''aaa


<center>
    <img src="ss/xxx.jpg" alt="image" width="800"/>
    <br>
    <br>
    <br>
</center>
'''

n = 32
pref = 'im'
for i in range(n):
    ss = s.replace('xxx.jpg', f'{pref}{i:02d}.jpg')
    print( ss )




