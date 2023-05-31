from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
import uuid
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from django.conf import settings



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True, blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default='user-default.png')
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key = True, editable=False)
    qrcode = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return str(self.first_name)
    
    def save(self, *args, **kwargs):
        qrcode_img= qrcode.make(f'{self.first_name} http://127.0.0.1:8000/users/edit-balance/{self.id}')
        # qrcode_img.save()
        # file_stream = io.BytesIO()
        # qrcode_img.save(file_stream)
        # file_stream.seek(0)
        # file_name = f'qrcode_{self.id}.png'
        # file = InMemoryUploadedFile(file_stream, None, file_name, 'image/png', file_stream.getbuffer().nbytes, None)
        # self.qrcode_image.save(file_name, file)
        # super().save(*args, **kwargs)
        # --------------------------------------------
        canvas = Image.new('RGB', (500,500), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.first_name}.' + 'png'
        buffer =  BytesIO()
        canvas.save (buffer,'PNG')
        self.qrcode.save(fname, File(buffer), save=False )
        canvas.close()
        super().save(*args, **kwargs)

# ------------------------------------------------------------------------

# class Income(models.Model):
#     account = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='acount_1', null=True)
#     amount = models.DecimalField(max_digits=15, decimal_places=2)
#     description = models.CharField(max_length=200)
#     date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return f"Income of {self.amount} on {self.date}"

# class Expense(models.Model):
#     account = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='acount_2',null=True) 
#     amount = models.DecimalField(max_digits=15, decimal_places=2)
#     description = models.CharField(max_length=200)
#     date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return f"Expense of {self.amount} on {self.date}"
    
class Account(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, )
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    
    # incomes = models.ForeignKey(Income, on_delete=models.CASCADE, null=True, blank=True,related_name='acount_3')
    # expences =  models.ForeignKey(Expense, on_delete=models.CASCADE, null=True, blank=True, related_name='acount_4')

    def __str__(self):
        return self.owner.username
    


class Transaction(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE )
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=0, null=True)
    created = models.DateTimeField(auto_now_add=True)
    is_deposit = models.BooleanField(default=True)


    def __str__(self) -> str:
        return f" {'+' if self.is_deposit else '-'} {self.owner.username}  {self.title}" 




