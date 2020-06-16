from django.db import models
from django.contrib.auth.models import User
from PIL import Image

#add picture to profile for users, dont forget to register with admin.py so you can see in the admin panel
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default1.jpg', upload_to = 'profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    #resize photos with Pillow to use locally, must remove for AWS buckets!
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
        
    #     img = Image.open(self.image.path)
        
    #     if img.height > 300 or img.width >300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
            
