from  django.db.models.signals import post_save,pre_save,post_delete,pre_delete
from django.dispatch import receiver 
from .models import Category
from  src  import settings
import requests

# @receiver(post_save, sender=None)
# def test_signal(sender,instance,created,*args,**kwargs):
#     print("\n")
#     print("Sender:",sender)
#     print("Instance:",instance)
#     print("Created:",created)
#     print("\n")
@receiver(post_save,sender=Category)
def category_signal(sender,instance,created,*args,**kwargs):
    if created:
        message = f"Yangi Kategoriya Qoshildi\nNomi:{instance.cat_name}  \nSlug: {instance.slug}\n Menu Holati: {instance.is_menu}"
        user_ids =  [7472610771,5520980915,5375398149,8239401111]
        token = settings.TG_BOT
        for user_id in user_ids:
            url  =  f"https://api.telegram.org/bot{token}/sendMessage?chat_id={user_id}&text={message}&parse_mode=HTML"
            requests.get(url)



