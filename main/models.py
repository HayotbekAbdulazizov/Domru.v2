# from tinymce.models import HTMLField
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.



class Post(models.Model):
	title = models.CharField("Title", max_length=300, blank=True)
	slug = models.SlugField("*", unique=True, blank=True)
	category = models.CharField("Category", max_length=200 ,blank=True)
	price = models.PositiveIntegerField("Price", default=0, blank=True)
	priceCurrency = models.CharField("Currency", max_length=20, blank=True)
	pricePerMeter = models.CharField("Price Per Meter", max_length=100, blank=True)
	city = models.CharField("City", max_length=200, blank=True)
	address = models.CharField("Address", max_length=200, blank=True)
	description = models.TextField("Description", blank=True)
	offerId = models.IntegerField("Offer Id", unique=True, blank=True, null=True)
	contacts = models.BooleanField("Contacts", default=False)
	body = RichTextField("Body" , blank=True)
	contact_body = RichTextField("ContactBody" , blank=True, null=True)
	published = models.DateTimeField(auto_now_add=True)
	source = models.URLField(max_length=200, blank=True)


	def __str__(self):
		return f"{self.title}"

	class Meta:
		ordering = ["-published",]
		verbose_name_plural = 'Posts'






class PostImages(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images",blank=True, null=True)
	image = models.ImageField(upload_to=None, height_field=None, blank=True, null=True)
	url = models.URLField("Image url", max_length=400, blank=True, null=True)

	def __str__(self):
		return self.post.title







class Contact(models.Model):
	post_id = models.ForeignKey(Post, max_length=20, on_delete=models.CASCADE,blank=True)
	done = models.BooleanField("Status", default=False, blank=True)
	date = models.DateTimeField("date ", auto_now_add=True, blank=True)

	def __str__(self):
		return self.post_id.title
