from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from openpyxl import load_workbook
import time
import datetime
from datetime import datetime, timedelta
import pandas as pd
from selenium.webdriver.support.ui import Select
import numpy as np
import pandas as pd
import gspread
import df2gspread as d2g
import pygsheets

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(executable_path=r'chromedriver.exe', options=options)
driver.get("https://www.hiperlibertad.com.ar")
driver.maximize_window()
time.sleep(5)

time.sleep(3)
sectores = driver.find_element_by_xpath("//*[@id='home-root']/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(2) 

# -------------------------------------------------------------------------------------------------------------------
# CARNES
# -------------------------------------------------------------------------------------------------------------------
carnes = driver.find_element_by_xpath("//*[@id='home-root']/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[8]").click()
time.sleep(2)
# -------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------
# VACA
carnevac = driver.find_element_by_xpath("//*[@id='department-root']/div[2]/div/div/ul/div[1]/li/div/a").click()
time.sleep(2)

carnvac = driver.find_elements_by_xpath("//div[@class='styles__Container-sc-1tfhldk-1 erxMjP']")
time.sleep(3)
carvac = []
for dato in carnvac:
    carvac.append(dato.text)
carvac = [line.split("\n") for line in carvac]
dfcarvac = pd.DataFrame(carvac)
dfcarvac = dfcarvac.drop(columns=3)
dfcarvac.columns = ['Marca_o_Sector','Producto','Precio']
dfcarvac
time.sleep(3)

sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
carnes = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[8]/p").click()
time.sleep(5)
# -------------------------------------------------------------------------------------------------------------------
# CERDO
carnecerd = driver.find_element_by_xpath("/html/body/main/div[2]/div/div[2]/ul/div[2]/li/a/a").click()
time.sleep(2)

carncer = driver.find_elements_by_xpath("//div[@class='styles__Container-sc-1tfhldk-1 erxMjP']")
time.sleep(3)
carcer = []
for dato in carncer:
    carcer.append(dato.text)
carcer = [line.split("\n") for line in carcer]
dfcarcer = pd.DataFrame(carcer)
dfcarcer = dfcarcer.drop(columns=3)
dfcarcer.columns = ['Marca_o_Sector','Producto','Precio']
dfcarcer
time.sleep(3)

sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
carnes = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[8]/p").click()
time.sleep(5)

# -------------------------------------------------------------------------------------------------------------------
# POLLO
carnespoll = driver.find_element_by_xpath("/html/body/main/div[2]/div/div[2]/ul/div[3]/li/a/a").click()
time.sleep(2)

carnpollo = driver.find_elements_by_xpath('//div[@class="styles__Container-sc-1tfhldk-1 erxMjP"]')
time.sleep(3)
carpoll = []
for dato in carnpollo:
    carpoll.append(dato.text)
carpoll = [line.split("\n") for line in carpoll]
dfcarpoll = pd.DataFrame(carpoll)
dfcarpoll = dfcarpoll.drop(columns=3)
dfcarpoll.columns = ['Marca_o_Sector','Producto','Precio']
dfcarpoll
time.sleep(3)

sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
carnes = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[8]/p").click()
time.sleep(5)

# -------------------------------------------------------------------------------------------------------------------
# EMBUTIDOS
embutidos = driver.find_element_by_xpath("//*[@id='department-root']/div[2]/div/div[2]/ul/div[4]/li/a/a").click()
time.sleep(2)

embut = driver.find_elements_by_xpath("//div[@class='styles__Container-sc-1tfhldk-1 erxMjP']")
time.sleep(3)
emb = []
for dato in embut:
    emb.append(dato.text)
emb = [line.split("\n") for line in emb]
dfemb = pd.DataFrame(emb)
dfemb = dfemb.drop(columns=3)
dfemb.columns = ['Marca_o_Sector','Producto','Precio']
dfemb
time.sleep(3)

sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
carnes = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[8]/p").click()
time.sleep(5)

# -------------------------------------------------------------------------------------------------------------------
# PESCADOS
carnepesc = driver.find_element_by_xpath("//*[@id='department-root']/div[2]/div/div[2]/ul/div[5]/li/a/a").click()
time.sleep(2)

carnpes = driver.find_elements_by_xpath("//div[@class='styles__Container-sc-1tfhldk-1 erxMjP']")
time.sleep(3)
carpes = []
for dato in carnpes:
    carpes.append(dato.text)
carpes = [line.split("\n") for line in carpes]
dfcarpes = pd.DataFrame(carpes)
dfcarpes = dfcarpes.drop(columns=3)
dfcarpes.columns = ['Marca_o_Sector','Producto','Precio']
dfcarpes
time.sleep(3)

sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
carnes = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[8]/p").click()
time.sleep(5)

# -------------------------------------------------------------------------------------------------------------------
# MARISCOS
mariscos = driver.find_element_by_xpath("//*[@id='department-root']/div[2]/div/div[2]/ul/div[6]/li/a/a").click()
time.sleep(2)

maris = driver.find_elements_by_xpath("//div[@class='styles__Container-sc-1tfhldk-1 erxMjP']")
time.sleep(3)
mar = []
for dato in maris:
    mar.append(dato.text)
mar = [line.split("\n") for line in mar]
dfmar = pd.DataFrame(mar)
dfmar = dfmar.drop(columns=3)
dfmar.columns = ['Marca_o_Sector','Producto','Precio']
dfmar
time.sleep(3)

sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
carnes = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[8]/p").click()
time.sleep(5)

# -------------------------------------------------------------------------------------------------------------------
fecha = datetime.today()
fecha = str(fecha.strftime('%d/%m/%Y'))
time.sleep(5)
carnes_lib = pd.concat([dfcarvac,dfcarcer,dfcarpoll,dfcarpes,dfemb,dfmar],ignore_index=True)
carnes_lib.rename(columns={'Marca_o_Sector':'Marca'})
carnes_lib['Sector'] = 'Carnes'
carnes_lib['Fecha'] = fecha
carnes_lib = carnes_lib.reindex(columns=['Fecha','Marca','Sector','Producto','Precio'])
carnes_lib
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------
# ALMACEN
# -------------------------------------------------------------------------------------------------------------------
time.sleep(3)
sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
almacen = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[4]/p").click()
time.sleep(5)

# -------------------------------------------------------------------------------------------------------------------
# ACEITE Y VINAGRES
acyvin = driver.find_element_by_xpath("//*[@id='department-root']/div[2]/div/div[2]/ul/div[1]/li/a/a").click()
time.sleep(2)

acyvi = driver.find_elements_by_xpath("//div[@class='styles__Container-sc-1tfhldk-1 erxMjP']")
time.sleep(3)
ayv = []
for dato in acyvi:
    ayv.append(dato.text)
ayv = [line.split("\n") for line in ayv]
dfayv = pd.DataFrame(ayv)
dfayv = dfayv.drop(columns=3)
dfayv = dfayv.drop(columns=4)
dfayv.columns = ['Marca','Producto','Precio']
dfayv
time.sleep(3)

sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
almacen = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[4]/p").click()
time.sleep(5)

# -------------------------------------------------------------------------------------------------------------------
# ACEITUNAS Y ENCURTIDOS
acyenc = driver.find_element_by_xpath('//*[@id="department-root"]/div[2]/div/div[2]/ul/div[2]/li/a/a').click()
time.sleep(2)

acyen = driver.find_elements_by_xpath("//div[@class='styles__Container-sc-1tfhldk-1 erxMjP']")
time.sleep(3)
aye = []
for dato in acyen:
    aye.append(dato.text)
aye = [line.split("\n") for line in aye]
dfaye = pd.DataFrame(aye)
dfaye = dfaye.drop(columns=3)
dfaye = dfaye.drop(columns=4)
dfaye.columns = ['Marca','Producto','Precio']
dfaye
time.sleep(3)

sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
almacen = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[4]/p").click()
time.sleep(5)


# -------------------------------------------------------------------------------------------------------------------
# ADEREZOS
aderezos = driver.find_element_by_xpath('//*[@id="department-root"]/div[2]/div/div[2]/ul/div[3]/li/a/a').click()
time.sleep(2)

aderez = driver.find_elements_by_xpath("//div[@class='styles__Container-sc-1tfhldk-1 erxMjP']")
time.sleep(3)
ader = []
for dato in aderez:
    ader.append(dato.text)
ader = [line.split("\n") for line in ader]
dfader = pd.DataFrame(ader)
dfader = dfader.drop(columns=3)
dfader = dfader.drop(columns=4)
dfader.columns = ['Marca','Producto','Precio']
dfader
time.sleep(3)

sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
almacen = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[4]/p").click()
time.sleep(5)

# -------------------------------------------------------------------------------------------------------------------
# ARROZ Y LEGUMBRES
arryleg = driver.find_element_by_xpath('//*[@id="department-root"]/div[2]/div/div[2]/ul/div[4]/li/a/a').click()
time.sleep(2)

aryle = driver.find_elements_by_xpath("//div[@class='styles__Container-sc-1tfhldk-1 erxMjP']")
time.sleep(3)
ayl = []
for dato in aryle:
    ayl.append(dato.text)
ayl = [line.split("\n") for line in ayl]
dfayl = pd.DataFrame(ayl)
dfayl = dfayl.drop(columns=3)
dfayl = dfayl.drop(columns=4)
dfayl.columns = ['Marca','Producto','Precio']
dfayl
time.sleep(3)

sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
almacen = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[4]/p").click()
time.sleep(5)

# -------------------------------------------------------------------------------------------------------------------
# CALDOS, SOPAS Y PURE
caldsopypur = driver.find_element_by_xpath('//*[@id="department-root"]/div[2]/div/div[2]/ul/div[5]/li/a/a').click()
time.sleep(2)

casoypu = driver.find_elements_by_xpath("//div[@class='styles__Container-sc-1tfhldk-1 erxMjP']")
time.sleep(3)
csyp = []
for dato in casoypu:
    csyp.append(dato.text)
csyp = [line.split("\n") for line in csyp]
dfcsyp = pd.DataFrame(csyp)
dfcsyp = dfcsyp.drop(columns=3)
dfcsyp = dfcsyp.drop(columns=4)
dfcsyp.columns = ['Marca','Producto','Precio']
dfcsyp
time.sleep(3)

sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
almacen = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[4]/p").click()
time.sleep(5)

# -------------------------------------------------------------------------------------------------------------------
# CONSERVAS
conservas = driver.find_element_by_xpath('//*[@id="department-root"]/div[2]/div/div[2]/ul/div[6]/li/a/a').click()
time.sleep(2)

conserv = driver.find_elements_by_xpath("//div[@class='styles__Container-sc-1tfhldk-1 erxMjP']")
time.sleep(3)
cons = []
for dato in conserv:
    cons.append(dato.text)
cons = [line.split("\n") for line in cons]
dfcons = pd.DataFrame(cons)
dfcons = dfcons.drop(columns=3)
dfcons = dfcons.drop(columns=4)
dfcons.columns = ['Marca','Producto','Precio']
dfcons
time.sleep(3)

sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
almacen = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[4]/p").click()
time.sleep(5)

# -------------------------------------------------------------------------------------------------------------------
# DESAYUNO Y MERIENDA
desaymer = driver.find_element_by_xpath('//*[@id="department-root"]/div[2]/div/div[2]/ul/div[7]/li/a/a').click()
time.sleep(2)

desyme = driver.find_elements_by_xpath("//div[@class='styles__Container-sc-1tfhldk-1 erxMjP']")
time.sleep(3)
dym = []
for dato in desyme:
    dym.append(dato.text)
dym = [line.split("\n") for line in dym]
dfdym = pd.DataFrame(dym)
dfdym = dfdym.drop(columns=3)
dfdym = dfdym.drop(columns=4)
dfdym.columns = ['Marca','Producto','Precio']
dfdym
time.sleep(3)

sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
almacen = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[4]/p").click()
time.sleep(5)

# -------------------------------------------------------------------------------------------------------------------
# GOLOSINAS Y CHOCOLATES
goloychoc = driver.find_element_by_xpath('//*[@id="department-root"]/div[2]/div/div[2]/ul/div[8]/li/a/a').click()
time.sleep(2)

golycho = driver.find_elements_by_xpath("//div[@class='styles__Container-sc-1tfhldk-1 erxMjP']")
time.sleep(3)
gyc = []
for dato in golycho:
    gyc.append(dato.text)
gyc = [line.split("\n") for line in gyc]
dfgyc = pd.DataFrame(gyc)
dfgyc = dfgyc.drop(columns=3)
dfgyc = dfgyc.drop(columns=4)
dfgyc.columns = ['Marca','Producto','Precio']
dfgyc
time.sleep(3)

sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
almacen = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[4]/p").click()
time.sleep(5)

# -------------------------------------------------------------------------------------------------------------------
# HARINAS
harinas = driver.find_element_by_xpath('//*[@id="department-root"]/div[2]/div/div[2]/ul/div[9]/li/a/a').click()
time.sleep(2)

harin = driver.find_elements_by_xpath("//div[@class='styles__Container-sc-1tfhldk-1 erxMjP']")
time.sleep(3)
har = []
for dato in harin:
    har.append(dato.text)
har = [line.split("\n") for line in har]
dfhar = pd.DataFrame(har)
dfhar = dfhar.drop(columns=3)
dfhar = dfhar.drop(columns=4)
dfhar.columns = ['Marca','Producto','Precio']
dfhar
time.sleep(3)

sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
almacen = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[4]/p").click()
time.sleep(5)

# -------------------------------------------------------------------------------------------------------------------
# SIN TACC
sintacc = driver.find_element_by_xpath('//*[@id="department-root"]/div[2]/div/div[2]/ul/div[10]/li/a/a').click()
time.sleep(2)

sita = driver.find_elements_by_xpath("//div[@class='styles__Container-sc-1tfhldk-1 erxMjP']")
time.sleep(3)
st = []
for dato in sita:
    st.append(dato.text)
st = [line.split("\n") for line in st]
dfst = pd.DataFrame(st)
dfst = dfst.drop(columns=3)
dfst = dfst.drop(columns=4)
dfst.columns = ['Marca','Producto','Precio']
dfst
time.sleep(3)

sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
almacen = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[4]/p").click()
time.sleep(5)

# -------------------------------------------------------------------------------------------------------------------
# PANIFICADOS
panificados = driver.find_element_by_xpath('//*[@id="department-root"]/div[2]/div/div[2]/ul/div[11]/li/a/a').click()
time.sleep(2)

panif = driver.find_elements_by_xpath("//div[@class='styles__Container-sc-1tfhldk-1 erxMjP']")
time.sleep(3)
pan = []
for dato in panif:
    pan.append(dato.text)
pan = [line.split("\n") for line in pan]
dfpan = pd.DataFrame(pan)
dfpan = dfpan.drop(columns=3)
dfpan = dfpan.drop(columns=4)
dfpan.columns = ['Marca','Producto','Precio']
dfpan
time.sleep(3)

sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
almacen = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[4]/p").click()
time.sleep(5)

# -------------------------------------------------------------------------------------------------------------------
# PARA PREPARAR
paraprep = driver.find_element_by_xpath('//*[@id="department-root"]/div[2]/div/div[2]/ul/div[12]/li/a/a').click()
time.sleep(2)

parapre = driver.find_elements_by_xpath("//div[@class='styles__Container-sc-1tfhldk-1 erxMjP']")
time.sleep(3)
parap = []
for dato in parapre:
    parap.append(dato.text)
parap = [line.split("\n") for line in parap]
dfparap = pd.DataFrame(parap)
dfparap = dfparap.drop(columns=3)
dfparap = dfparap.drop(columns=4)
dfparap.columns = ['Marca','Producto','Precio']
dfparap
time.sleep(3)

sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
almacen = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[4]/p").click()
time.sleep(5)

# -------------------------------------------------------------------------------------------------------------------
# PASTAS Y SALSAS
pastysal = driver.find_element_by_xpath('//*[@id="department-root"]/div[2]/div/div[2]/ul/div[13]/li/a/a').click()
time.sleep(2)

pasysa = driver.find_elements_by_xpath("//div[@class='styles__Container-sc-1tfhldk-1 erxMjP']")
time.sleep(3)
pys = []
for dato in pasysa:
    pys.append(dato.text)
pys = [line.split("\n") for line in pys]
dfpys = pd.DataFrame(pys)
dfpys = dfpys.drop(columns=3)
dfpys = dfpys.drop(columns=4)
dfpys.columns = ['Marca','Producto','Precio']
dfpys
time.sleep(3)

sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
almacen = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[4]/p").click()
time.sleep(5)

# -------------------------------------------------------------------------------------------------------------------
# SAL, PIMIENTA Y ESPECIAS
salpimyesp = driver.find_element_by_xpath('//*[@id="department-root"]/div[2]/div/div[2]/ul/div[14]/li/a/a').click()
time.sleep(2)

sapiyes = driver.find_elements_by_xpath("//div[@class='styles__Container-sc-1tfhldk-1 erxMjP']")
time.sleep(3)
spye = []
for dato in sapiyes:
    spye.append(dato.text)
spye = [line.split("\n") for line in spye]
dfspye = pd.DataFrame(spye)
dfspye = dfspye.drop(columns=3)
dfspye = dfspye.drop(columns=4)
dfspye.columns = ['Marca','Producto','Precio']
dfspye
time.sleep(3)

sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
almacen = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[4]/p").click()
time.sleep(5)


# -------------------------------------------------------------------------------------------------------------------
# SNACKS
snacks = driver.find_element_by_xpath('//*[@id="department-root"]/div[2]/div/div[2]/ul/div[15]/li/a/a').click()
time.sleep(2)

snac = driver.find_elements_by_xpath("//div[@class='styles__Container-sc-1tfhldk-1 erxMjP']")
time.sleep(3)
sna = []
for dato in snac:
    sna.append(dato.text)
sna = [line.split("\n") for line in sna]
dfsna = pd.DataFrame(sna)
dfsna = dfsna.drop(columns=3)
dfsna = dfsna.drop(columns=4)
dfsna.columns = ['Marca','Producto','Precio']
dfsna
time.sleep(3)

# -------------------------------------------------------------------------------------------------------------------
time.sleep(5)
almacen_lib = pd.concat([dfayv,dfaye,dfader,dfayl,dfcsyp,dfcons,dfdym,dfgyc,dfhar,dfst,dfpan,dfparap,dfpys,dfspye,dfsna],ignore_index=True)
almacen_lib['Sector'] = 'Almacen'
almacen_lib['Fecha'] = fecha
almacen_lib = almacen_lib.reindex(columns=['Fecha','Marca','Sector','Producto','Precio'])
almacen_lib

# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------
# BEBIDAS
# -------------------------------------------------------------------------------------------------------------------
sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
bebidas = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[5]/p").click()
time.sleep(5)

# -------------------------------------------------------------------------------------------------------------------
# APERITIVOS
aperitivos = driver.find_element_by_xpath('//*[@id="department-root"]/div[2]/div/div[2]/ul/div[1]/li/a/a').click()
time.sleep(2)

aperit = driver.find_elements_by_xpath("//div[@class='styles__Container-sc-1tfhldk-1 erxMjP']")
time.sleep(3)
aper = []
for dato in aperit:
    aper.append(dato.text)
aper = [line.split("\n") for line in aper]
dfaper = pd.DataFrame(aper)
dfaper = dfaper.drop(columns=3)
dfaper = dfaper.drop(columns=4)
dfaper.columns = ['Marca','Producto','Precio']
dfaper
time.sleep(3)

sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
bebidas = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[5]/p").click()
time.sleep(5)

# -------------------------------------------------------------------------------------------------------------------
# CERVEZAS
cervezas = driver.find_element_by_xpath('//*[@id="department-root"]/div[2]/div/div[2]/ul/div[2]/li/a/a').click()
time.sleep(2)

cervez = driver.find_elements_by_xpath("//div[@class='styles__Container-sc-1tfhldk-1 erxMjP']")
time.sleep(3)
cerv = []
for dato in cervez:
    cerv.append(dato.text)
cerv = [line.split("\n") for line in cerv]
dfcerv = pd.DataFrame(cerv)
dfcerv = dfcerv.drop(columns=3)
dfcerv = dfcerv.drop(columns=4)
dfcerv.columns = ['Marca','Producto','Precio']
dfcerv
time.sleep(3)

sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
bebidas = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[5]/p").click()
time.sleep(5)

# -------------------------------------------------------------------------------------------------------------------
# GASEOSAS
gaseosas = driver.find_element_by_xpath('//*[@id="department-root"]/div[2]/div/div[2]/ul/div[3]/li/a/a').click()
time.sleep(2)

gaseo = driver.find_elements_by_xpath("//div[@class='styles__Container-sc-1tfhldk-1 erxMjP']")
time.sleep(3)
gase = []
for dato in gaseo:
    gase.append(dato.text)
gase = [line.split("\n") for line in gase]
dfgase = pd.DataFrame(gase)
dfgase = dfgase.drop(columns=3)
dfgase = dfgase.drop(columns=4)
dfgase.columns = ['Marca','Producto','Precio']
dfgase
time.sleep(3)

sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
bebidas = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[5]/p").click()
time.sleep(5)

# -------------------------------------------------------------------------------------------------------------------
# JUGOS
jugos = driver.find_element_by_xpath('//*[@id="department-root"]/div[2]/div/div[2]/ul/div[4]/li/a/a').click()
time.sleep(2)

jugo = driver.find_elements_by_xpath("//div[@class='styles__Container-sc-1tfhldk-1 erxMjP']")
time.sleep(3)
jug = []
for dato in jugo:
    jug.append(dato.text)
jug = [line.split("\n") for line in jug]
dfjug = pd.DataFrame(jug)
dfjug = dfjug.drop(columns=3)
dfjug = dfjug.drop(columns=4)
dfjug.columns = ['Marca','Producto','Precio']
dfjug
time.sleep(3)

sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
bebidas = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[5]/p").click()
time.sleep(5)

# -------------------------------------------------------------------------------------------------------------------
# AGUAS
aguas = driver.find_element_by_xpath('//*[@id="department-root"]/div[2]/div/div[2]/ul/div[5]/li/a/a').click()
time.sleep(2)

agua = driver.find_elements_by_xpath("//div[@class='styles__Container-sc-1tfhldk-1 erxMjP']")
time.sleep(3)
agu = []
for dato in agua:
    agu.append(dato.text)
agu = [line.split("\n") for line in agu]
dfagu = pd.DataFrame(agu)
dfagu = dfagu.drop(columns=3)
dfagu = dfagu.drop(columns=4)
dfagu.columns = ['Marca','Producto','Precio']
dfagu
time.sleep(3)

sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
bebidas = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[5]/p").click()
time.sleep(5)

# -------------------------------------------------------------------------------------------------------------------
# VINOS Y ESPUMANTES
vinyesp = driver.find_element_by_xpath('//*[@id="department-root"]/div[2]/div/div[2]/ul/div[6]/li/a/a').click()
time.sleep(2)

viyes = driver.find_elements_by_xpath("//div[@class='styles__Container-sc-1tfhldk-1 erxMjP']")
time.sleep(3)
vye = []
for dato in viyes:
    vye.append(dato.text)
vye = [line.split("\n") for line in vye]
dfvye = pd.DataFrame(vye)
dfvye = dfvye.drop(columns=3)
dfvye = dfvye.drop(columns=4)
dfvye.columns = ['Marca','Producto','Precio']
dfvye
time.sleep(3)

sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
bebidas = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[5]/p").click()
time.sleep(5)

# -------------------------------------------------------------------------------------------------------------------
# ISOTONICAS Y ENERGIZANTES
isotyener = driver.find_element_by_xpath('//*[@id="department-root"]/div[2]/div/div[2]/ul/div[7]/li/a/a').click()
time.sleep(2)

isoyene = driver.find_elements_by_xpath("//div[@class='styles__Container-sc-1tfhldk-1 erxMjP']")
time.sleep(3)
iye = []
for dato in isoyene:
    iye.append(dato.text)
iye = [line.split("\n") for line in iye]
dfiye = pd.DataFrame(iye)
dfiye = dfiye.drop(columns=3)
dfiye = dfiye.drop(columns=4)
dfiye.columns = ['Marca','Producto','Precio']
dfiye
time.sleep(3)

sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
bebidas = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[5]/p").click()
time.sleep(5)

# -------------------------------------------------------------------------------------------------------------------
# BEBIDAS BLANCAS Y LICORES
bebblaylic = driver.find_element_by_xpath('//*[@id="department-root"]/div[2]/div/div[2]/ul/div[8]/li/a/a').click()
time.sleep(2)

beblayli = driver.find_elements_by_xpath("//div[@class='styles__Container-sc-1tfhldk-1 erxMjP']")
time.sleep(3)
bbyl = []
for dato in beblayli:
    bbyl.append(dato.text)
bbyl = [line.split("\n") for line in bbyl]
dfbbyl = pd.DataFrame(bbyl)
dfbbyl = dfbbyl.drop(columns=3)
dfbbyl = dfbbyl.drop(columns=4)
dfbbyl.columns = ['Marca','Producto','Precio']
dfbbyl
time.sleep(3)

# -------------------------------------------------------------------------------------------------------------------
time.sleep(5)
bebidas_lib = pd.concat([dfaper,dfcerv,dfgase,dfjug,dfagu,dfvye,dfiye,dfbbyl],ignore_index=True)
bebidas_lib['Sector'] = 'Bebidas'
bebidas_lib['Fecha'] = fecha
bebidas_lib = bebidas_lib.reindex(columns=['Fecha','Marca','Sector','Producto','Precio'])
bebidas_lib

# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------
# LACTEOS
# -------------------------------------------------------------------------------------------------------------------
sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
lacteos = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[6]/p").click()
time.sleep(5)

# -------------------------------------------------------------------------------------------------------------------
# DULCE DE LECHE
dulcedeleche = driver.find_element_by_xpath('//*[@id="department-root"]/div[2]/div/div[2]/ul/div[1]/li/a/a').click()
time.sleep(2)

dulcedlech = driver.find_elements_by_xpath("//div[@class='styles__Container-sc-1tfhldk-1 erxMjP']")
time.sleep(3)
ddl = []
for dato in dulcedlech:
    ddl.append(dato.text)
ddl = [line.split("\n") for line in ddl]
dfddl = pd.DataFrame(ddl)
dfddl = dfddl.drop(columns=3)
dfddl = dfddl.drop(columns=4)
dfddl.columns = ['Marca','Producto','Precio']
dfddl
time.sleep(3)

sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
lacteos = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[6]/p").click()
time.sleep(5)

# -------------------------------------------------------------------------------------------------------------------
# LECHES
leches = driver.find_element_by_xpath('//*[@id="department-root"]/div[2]/div/div[2]/ul/div[2]/li/a/a').click()
time.sleep(2)

leche = driver.find_elements_by_xpath("//div[@class='styles__Container-sc-1tfhldk-1 erxMjP']")
time.sleep(3)
lech = []
for dato in leche:
    lech.append(dato.text)
lech = [line.split("\n") for line in lech]
dflech = pd.DataFrame(lech)
dflech = dflech.drop(columns=3)
dflech = dflech.drop(columns=4)
dflech.columns = ['Marca','Producto','Precio']
dflech
time.sleep(3)

sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
lacteos = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[6]/p").click()
time.sleep(5)

# -------------------------------------------------------------------------------------------------------------------
# CREMAS
cremas = driver.find_element_by_xpath('//*[@id="department-root"]/div[2]/div/div[2]/ul/div[3]/li/a/a').click()
time.sleep(2)

crema = driver.find_elements_by_xpath("//div[@class='styles__Container-sc-1tfhldk-1 erxMjP']")
time.sleep(3)
crem = []
for dato in crema:
    crem.append(dato.text)
crem = [line.split("\n") for line in crem]
dfcrem = pd.DataFrame(crem)
dfcrem = dfcrem.drop(columns=3)
dfcrem = dfcrem.drop(columns=4)
dfcrem.columns = ['Marca','Producto','Precio']
dfcrem
time.sleep(3)

sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
lacteos = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[6]/p").click()
time.sleep(5)

# -------------------------------------------------------------------------------------------------------------------
# YOGURES
yogures = driver.find_element_by_xpath('//*[@id="department-root"]/div[2]/div/div[2]/ul/div[4]/li/a/a').click()
time.sleep(2)

yogur = driver.find_elements_by_xpath("//div[@class='styles__Container-sc-1tfhldk-1 erxMjP']")
time.sleep(3)
yog = []
for dato in yogur:
    yog.append(dato.text)
yog = [line.split("\n") for line in yog]
dfyog = pd.DataFrame(yog)
dfyog = dfyog.drop(columns=3)
dfyog = dfyog.drop(columns=4)
dfyog.columns = ['Marca','Producto','Precio']
dfyog
time.sleep(3)

sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
lacteos = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[6]/p").click()
time.sleep(5)

# -------------------------------------------------------------------------------------------------------------------
# MANTECAS Y MARGARINAS
mantecymarg = driver.find_element_by_xpath('//*[@id="department-root"]/div[2]/div/div[2]/ul/div[5]/li/a/a').click()
time.sleep(2)

manymar = driver.find_elements_by_xpath("//div[@class='styles__Container-sc-1tfhldk-1 erxMjP']")
time.sleep(3)
mym = []
for dato in manymar:
    mym.append(dato.text)
mym = [line.split("\n") for line in mym]
dfmym = pd.DataFrame(mym)
dfmym = dfmym.drop(columns=3)
dfmym = dfmym.drop(columns=4)
dfmym.columns = ['Marca','Producto','Precio']
dfmym
time.sleep(3)

sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
lacteos = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[6]/p").click()
time.sleep(5)

# -------------------------------------------------------------------------------------------------------------------
# POSTRES Y FLANES
postyflan = driver.find_element_by_xpath('//*[@id="department-root"]/div[2]/div/div[2]/ul/div[6]/li/a/a').click()
time.sleep(2)

posyfla = driver.find_elements_by_xpath("//div[@class='styles__Container-sc-1tfhldk-1 erxMjP']")
time.sleep(3)
pyf = []
for dato in posyfla:
    pyf.append(dato.text)
pyf = [line.split("\n") for line in pyf]
dfpyf = pd.DataFrame(pyf)
dfpyf = dfpyf.drop(columns=3)
dfpyf = dfpyf.drop(columns=4)
dfpyf.columns = ['Marca','Producto','Precio']
dfpyf
time.sleep(3)

sectores = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div/button").click()
time.sleep(5)
lacteos = driver.find_element_by_xpath("/html/body/main/div[1]/header/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div/a[6]/p").click()
time.sleep(5)

# -------------------------------------------------------------------------------------------------------------------
time.sleep(5)
lacteos_lib = pd.concat([dfddl,dflech,dfcrem,dfyog,dfmym,dfpyf],ignore_index=True)
lacteos_lib['Sector'] = 'Bebidas'
lacteos_lib['Fecha'] = fecha
lacteos_lib = lacteos_lib.reindex(columns=['Fecha','Marca','Sector','Producto','Precio'])
lacteos_lib

# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------


time.sleep(1)
driver.quit()
