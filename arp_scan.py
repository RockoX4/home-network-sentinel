#Fase 4 Bootcamp Python aplicado a ciberseguridad
from scapy.all import ARP, Ether, srp
import json
import requests
with open("white_list.json") as f:
    contenido = json.load(f)
def cargar_oui_db(ruta_archivo):
    oui_db = {}
    archivo = open(ruta_archivo, "r")
    
    for linea in archivo:
        if "(hex)" in linea:
            partes = linea.split("(hex)")
            codigo_oui = partes[0].strip()      # "00-0C-29"
            fabricante = partes[1].strip()      # "VMware, Inc."
            oui_db[codigo_oui] = fabricante
    
    archivo.close()
    return oui_db
objetivo = "192.168.100.0/24"
arp = ARP(pdst=objetivo)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
paquete = ether/arp
resultado = srp(paquete, timeout=3, verbose=True, iface="eth0")
#resultado = srp(paquete, timeout=2, verbose=False, iface="eth0")
respuestas = resultado[0]
oui_db = cargar_oui_db("oui.txt")
#fabricante= requests.get(f"https://api.macvendors.com/{elemento[1].hwsrc}").text
for elemento in respuestas:
    clave = elemento[1].hwsrc[:8].replace(":", "-").upper()
    fabricante = oui_db.get(clave, "Desconocido")
    #print(f"IP: {elemento[1].psrc} | MAC: {elemento[1].hwsrc} | Fabricante: {fabricante}")
    if elemento[1].hwsrc in contenido:
        print(f"dispositivo conocido {elemento[1].hwsrc} | {contenido[elemento[1].hwsrc]} | {fabricante} ✅")
    else:
        print(f"intruso {elemento[1].psrc} |  {elemento[1].hwsrc} | {fabricante}🚨")


""" def cargar_oui_db(ruta_archivo):
    oui_db = {}
    archivo = open(ruta_archivo, "r")
    
    for linea in archivo:
        if "(hex)" in linea:
            partes = linea.split("(hex)")
            codigo_oui = partes[0].strip()      # "00-0C-29"
            fabricante = partes[1].strip()      # "VMware, Inc."
            oui_db[codigo_oui] = fabricante
    
    archivo.close()
    return oui_db """