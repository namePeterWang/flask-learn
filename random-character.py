import random

zimu = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
shuzi = "1234567890"
teshufuhao = "`~!@#$%^&*()-=_+,./;'<>?:\|"
#print random.random()

def tiaoxuanzifu(zifuji, changdu):
    mimazifu = ""
    for i in range(1,changdu+1):
        mimazifu = mimazifu + zifuji[int(random.random()*len(zifuji))]
    return(mimazifu)

def mimashengcheng(leixing, changdu):
#### 111 (分别代表 字母 数字 特殊符号)
    if leixing == 7:
        zifujihe = zimu + shuzi + teshufuhao
        print tiaoxuanzifu(zifujihe,changdu)
    elif leixing == 6:
        zifujihe = zimu + shuzi
        tiaoxuanzifu(zifujihe,changdu)
    elif leixing == 5:
        zifujihe = zimu + teshufuhao
        print tiaoxuanzifu(zifujihe,changdu)
    elif leixing == 4:
        zifujihe = zimu
        tiaoxuanzifu(zifujihe,changdu)
    elif leixing == 3:
        zifujihe = shuzi + teshufuhao
        tiaoxuanzifu(zifujihe,changdu)
    elif leixing == 2:
        zifujihe = shuzi
        print tiaoxuanzifu(zifujihe,changdu)
    elif leixing == 1:
        zifujihe = teshufuhao
        tiaoxuanzifu(zifujihe,changdu)

mimashengcheng(9,7)
