from captcha.image import ImageCaptcha

pattern = 'AbraCadabra'

captcha = ImageCaptcha(width=300, height=150)

captcha.write(pattern, 'captcha.png')