#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib 
SUBJECT = 'Rapor'
TEXT = "Klavyeden yasaklı kelime ya da kelimelerden girildi."
content = 'Subject: %s\n\n%s' % (SUBJECT, TEXT)
mail = smtplib.SMTP('smtp.live.com',587) 
mail.ehlo()
mail.starttls()
mail.login('sd@hotmail.com' , '123456' )
mail.sendmail ('sd@gmail.com' , 'sd@gmail.com' , content)
mail.quit()
print("yess")
#deneme amaçlı gönderildi.
