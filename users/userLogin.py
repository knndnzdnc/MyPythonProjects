from mysql_conn import *
import hashlib

while True:
    try:
        morUsername = str(input("Mail veya kullanıcı adınızı giriniz..")).strip()
        username = morUsername
        password = str(input("Parolanızı giriniz")).strip()
        convertToPass = hashlib.md5(password.encode())
        md5_pass = convertToPass.hexdigest()  # the last pass with md5

        # kullanıcının status'unu çekmek
        sql = "SELECT * FROM myusers WHERE (mail=%s or username=%s) and password=%s "
        adr = (str(morUsername), str(username), str(md5_pass))
        cursor.execute(sql, adr)

        result = cursor.fetchall()
        for i in result:
            status = i[6]
            name = i[1]

        sql = "SELECT * FROM myusers WHERE (mail=%s or username=%s) and password=%s "
        adr = (str(morUsername), str(username), str(md5_pass))
        cursor.execute(sql, adr)

        result = cursor.fetchall()
        if bool(result) is True and status == 1:
            print(f'Sayın {name}. Hoşgeldiniz...')
            break
        elif bool(result) is not True:
            print("Kullanıcı adı, mail veya parolanızı kontrol ediniz..")

        elif status == 0:
            print("Üyeliğiniz aktif değil..\nLütfen mailinize gelen aktifleştirme linkine tıklayınız..")
            break
        else:
            print("Mail adresi veya parola hatalı\nYeniden deneyiniz..")

    except Exception as ex:
        print(f'Hata sebebi : {ex}')
