from twilio.rest import Client
import os,random,math

digits="0123456789"
OTP = ""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
    
client = Client("AC540bf10a6f57e4ca5d1e35809692f9c4","65f94a63f500c24872992e0eb1c2abbc")

message = client.messages \
                .create(
                     body='Your OTP Verification for app is '+OTP+'.',
                     from_='+17402793164',
                     to='+919834101715'
                 )
file2=open("otp.txt","w")
file2.write(OTP)
file2.close()
print(OTP)
os.system("second.py")
