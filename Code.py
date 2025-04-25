import qrcode
from PIL import Image
#Taking UPI Id as a input
upi_id = input("Enter your UPI ID")
#parameters for payment
#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=Currency&tn=MESSAGE
#this above gives the information to payment app for payment
#Defining the payment URL based on the UPI ID and the payment app
# You can modify these URLs based on the payment apps you want to support

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
#mc is merchant code since i dont have so i used 1234 but we can skip also

#create QR code for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#saving qrcode to image file
phonepe_qr.save('Phonepe_qr.png')
paytm_qr.save('Paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

#Displaying the qrcode by using pillow library
# phonepe_qr.show()
# paytm_qr.show()
# google_pay_qr.show()

Image.open('Phonepe_qr.png').show()
Image.open('Paytm_qr.png').show()
Image.open('google_pay_qr.png').show()
