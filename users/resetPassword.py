import re
import time
import hashlib
from mysql_conn import *
# check_password eklenecek..

username = str(input("Kullanıcı adınızı veya mailinizi giriniz..")).strip()
mail = username

sql = "SELECT * FROM myusers WHERE (mail=%s or username=%s) "
adr = (str(mail), str(username))
cursor.execute(sql, adr)

result = cursor.fetchall()

if result == []:
    print("Kullanıcı bulunamadı..")
    exit()
else:
    for i in result:
        id = i[0]
        status = i[6]

if status == 0:
    print("Aktif kullanıcı değilsiniz..")
    exit()

else:
    while True:
        try:
            if bool(id) is True:
                password = str(input("Parolanızı giriniz")).strip()
                password_check = str(input("Tekrar parola giriniz..")).strip()
                result = hashlib.md5(password.encode())
                md5_password = result.hexdigest()

                if password == password_check:
                    try:
                        # update sorgusu yer alacak ve parola kontrolü yapılacak
                        sql = "UPDATE myusers SET password=%s WHERE id=%s and status=%s "
                        val = (md5_password, str(id), 1)  # md5 lenecek
                        cursor.execute(sql, val)
                        connection.commit()
                        print(cursor.rowcount, "adet kayıt etkilendi..")
                    except Exception as ex:
                        print(f'Parola değiştirilmedi')

                    break
                else:
                    print("Parolalar uyuşmuyor..")
            else:
                print("Kullanıcı bulunamadı..")
        except Exception as ex:
            print(f'hata: {ex}')
