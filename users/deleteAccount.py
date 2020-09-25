import time
import hashlib
from mysql_conn import *


mail = str(input("Mail adresinizi veya kullanıcı adınızı giriniz")).strip()
username = mail

sql = "SELECT * FROM myusers WHERE (mail=%s or username=%s) and status=%s "
adr = (str(mail), str(username), 1)
cursor.execute(sql, adr)

result = cursor.fetchall()

if result == []:
    print("Kullanıcı bulunamadı veya aktif değil")
    exit()
else:
    for i in result:
        _id = i[0]
        _password = i[4]

while True:
    password = str(input("Parolanızı giriniz..")).strip()
    password_check = str(input("Parolanızı doğrulayınız..")).strip()
    result1 = hashlib.md5(password.encode())
    md5_pass = result1.hexdigest()

    if password != password_check or md5_pass != _password:
        print("Parolalar uyuşmuyor")
    else:
        try:
            sql2 = "UPDATE myusers SET status=%s WHERE id=%s "
            val = (0, str(_id))
            cursor.execute(sql2, val)
            connection.commit()
            print("İşlem yapılıyor")
            time.sleep(2)
            print(cursor.rowcount, "adet kayıt etkilendi..")
            break
        except Exception as ex:
            print(f'Değişiklik yapılmadı')
