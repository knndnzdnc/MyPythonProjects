import re
import time
import hashlib
import random
from mysql_conn import *  # db bağlantısını sabit tuttuk
from smtplib import SMTP


class Conditions:
    def check_password(self, psw):
        if len(psw) < 8:
            raise Exception("Parola 8 karakterden az olamaz")
        elif not re.search("[A-Z]", psw):
            raise Exception("Parola içerisinde en az 1 büyük harf olmalı")
        elif not re.search("[a-z]", psw):
            raise Exception("Parola içerisinde en az 1 küçük harf olmalı")
        elif re.search("\s", psw):
            raise Exception("Parola içerisinde boşluk karakteri olamaz")
        else:
            print(f'Parola oluşturma başarılı def/check')

    def check_username(self, _name):
        cursor.execute('Select * from users.myusers')
        result = cursor.fetchall()
        vbUsernameList = []
        for i in result:
            vbUsernameList = (i[3])
            if _name in vbUsernameList:
                raise Exception("Kullanıcı Adı mevcut")

    def check_mail(self, _mail):

        cursor.execute('Select * from users.myusers')
        result = cursor.fetchall()
        vbUsernameList = []
        for i in result:
            vbUsernameList = (i[2])
            if _mail in vbUsernameList:
                raise Exception("Mail adresi mevcut")
            else:
                pass

        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if not (re.search(regex, _mail)):
            raise Exception("Geçersiz Email")
        else:
            pass

    def hash_generator(self):
        characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        numbers = '0123456789'

        hash_generate = ''
        list = numbers + characters
        for i in range(13):
            hash_generate += random.choice(list)

        self.hash = hash_generate.upper()
        return self.hash

    def send_mail(self, _username, _password, _mail, _hash):
        self.username = _username
        self.password = _password
        self.hash = _hash
        subject = "Mail adresi onaylama"
        message = (f'Kullanıcı adınız: {username}\nŞifreniz: {self.password}\nOnay kodunuz: {hash}')
        content = "Subject : {0}\n\n{1}".format(subject, message)

        myMailAdres = "mailadresi"
        password = "parola"
        self.sendTo = _mail

        mail = SMTP("smtp.gmail.com", 587)
        mail.ehlo()
        mail.starttls()

        mail.login(myMailAdres, password)

        try:
            mail.sendmail(myMailAdres, self.sendTo, content.encode("utf-8"))
            print("Başarılı")
        except Exception as ex:
            print(f'hata : {ex}')


hash = Conditions.hash_generator(Conditions)

name = str(input("Adınızı giriniz...")).strip()  # sağ ve soldaki kullanıcı tarafınan girilen boşlukları sil
while True:
    try:
        mail = str(input("Mail giriniz...")).strip()
        username = str(input("Kullanmak istediğiniz kullanıcı adını giriniz...")).strip()
        password = str(input("Parola giriniz..."))

        Conditions.check_mail(Conditions, mail)
        Conditions.check_username(Conditions, username)
        Conditions.check_password(Conditions, password)

        print(f'Parolanız başarıyla oluşturuldu..\nBir sonraki adıma geçiliyor..')
        time.sleep(2)
        md5_pass = hashlib.md5(password.encode())
        md5_pass = md5_pass.hexdigest()
        # print(f'Veritabanında gözüken parolanız.. {md5_pass}')
        # db insert burada yapılacak //

        sql = "INSERT INTO users.myusers(name, mail, username, password, hash, status) values (%s,%s,%s,%s,%s,%s)"
        values = (str(name), str(mail), str(username), str(md5_pass), str(hash), 0)

        cursor.execute(sql, values)
        try:
            connection.commit()
            print(f'{cursor.rowcount} tane kayıt eklendi')
            Conditions.send_mail(Conditions, username, password, mail, hash)
            print(f'{mail} adresine mail gönderildi..\nLütfen kontrol ediniz')
        except Exception as ex:
            print(f'hata {ex}')
        finally:
            connection.close()
            print("Db Bağlantısı sonlandırıldı")
            break

    except Exception as ex:
        print(f'Hata mesajı: {ex}')
    finally:
        connection.close()