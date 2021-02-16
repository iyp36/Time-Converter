'''
Exam Modul 1
16 Februari 2021
'''
print('Soal 1 - Time Converter')
print('='*30)

def timeConverter(seconds):
    if 0 <= seconds <= 359999:
        jam = int(seconds/3600)
        sjam = seconds%3600
        menit = int(sjam/60)
        smenit = sjam%60
        detik = smenit
        return f'Konversi : {"{0:0=2d}".format(jam)} : {"{0:0=2d}".format(menit)} : {"{0:0=2d}".format(detik)}'
    elif seconds < 0 :
        return 'Invalid Input!'
    else:
        return 'Invalid Input!'

try:
    seconds = int(input('Masukkan Detik : '))
    print(timeConverter(seconds))
except:
    print('Invalid Input!')
