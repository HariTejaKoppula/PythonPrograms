import qrcode
img = qrcode.make('https://github.com/HariTejaKoppula')
img.save('MyGitHubQRcode.png')
img.show()