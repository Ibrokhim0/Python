# Indexlar haqida
ozgaruvchi = 'Hello world'
print(ozgaruvchi[2])#ya`niy bu yerda ozgaruvchining 2 - raqamli elementni konsol oynasiga chop etadi
print(ozgaruvchi[3:-1:2]) # ya`niy bu qatorda 3 - indeksdan toki -1 chi indeksgacha bo`lgan matinni ikkiga bo`lim konsol oynasiga ushbu elementlarni chop etadi
print(ozgaruvchi[::2]) # bu index ikkitadan qator tashlab ketadi
print(ozgaruvchi[-1]) # bu elementni o`ndan chapga o`qiy boshlaydi
print(ozgaruvchi[::-1])
print(ozgaruvchi[-1])
#upper metodi
upper1 ='bu metod orqali matinlar kattartiriladi'
print(upper1.upper())
print(upper1.isupper())#bu metod matinni kichiklikga tekshiradi to`g`ri bo`lsa True aks holda False qiymati beriladi
lower = 'BU METOD MATNLARNI KICHIRAYTIRISH UCHUN YORDAM BERADI'
print(lower.lower())
print(lower.islower())#bu metod ham huddi shunday shartni to`gri yoki noto`g`riligiga bajaradi
capitalize1 ='bu metod matinni bosh harfini katta qilib chiqarib beradi'
print(capitalize1.capitalize())
title1 = 'bu metod har bir matinning bosh harfini katta qilib beradi'
print(title1.title())
print(title1.istitle())#bu esa har bir matinning har bir harflari katta yoki kichigligiga tekshiradi
digit1 = '99'#bu metod faqatgina raqamlarni to`g`riliiga tekshiradi agarda string tipidagi ma`lumot o`zgaruvchilari berilsa False qiymatini beradi
print(digit1.isdigit())
startwith1 = 'bu metod orqali matndagi bosh harfni to`g`ri yoki noto`g`rilikga tekshiradi'
print(startwith1.startswith('b'))
endwith1 = 'bu metod matinning oxxiridagi harfni to`g`ri youki noto`g`rilikga tekshiradi'
print(endwith1.endswith('i'))
strip1 = '    bu element bo`sh qatordagi yoki elementlarni joylarni qirqib tashlaydi     '
print(strip1.strip())
print(strip1.lstrip(''))#chap qatordan qirqishni boshlaydi
print(strip1.rstrip(''))#o`ng qatordan qirqishni boshlaydi
count1 = 'bu metod faqatgina harfalrni nechtaligini sanash iuchun ishlatiladi'
print(count1.count('a'))
replace1 = 'bu metod matinning joyini almshtirish uchun ishlatiladi'
print(replace1.replace("bu","aynan shu"))
find1 = 'bu metod faqatgina matinlardagi harflarni topish uchun ishlatiladi'
print(find1.find('a'))
split1 = 'bu metod matndagi harflarni olib tashlash uchun ishlatiladi'
print(split1.split("a"))
join1 = 'bu metod elementlarni bo`sh joyiga amal qo`shish uchun ishlatiladi'
join1 = '_'.join(join1)
print(join1)
format1 = 'bu element bo`sh joylarga tekst qo`yish imkonini beradi misol uchun u tarmoq administratorligida juda qo`l keladi'
format2 = 'mening ismim {}'#yani gulli qavis orqali matn kiritiladi
print(format2.format('Ibrohim'))

#misol uchun
print('='*60)
tarmoq = """
nmci con mod {0} ipv4.adress {1}/{2}
nmci con mod {0} ipv4.gateway {3}
nmci con mod {0} ipv4.dns {4}
nmci con up {0}
"""
print(tarmoq.format('eth0', '196.168.100.1', '28', '196.168.10', '8.8.8.8'))
le1 = 'harf yoki raqamlarni qanchaligiuni anniqlabberadi'
print(len(le1))
