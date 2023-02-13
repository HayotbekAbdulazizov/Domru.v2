from rest_framework.response import Response
from main.models import Post
from .serializers import PostSerializer
from django.http import HttpResponse

from django.shortcuts import get_object_or_404
# generic view
from rest_framework.generics import CreateAPIView, GenericAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin


import json










class PostApiView(GenericAPIView, CreateModelMixin):
	serializer_class = PostSerializer
	queryset = Post.objects.all()



	def get(self, request):
		posts = Post.objects.all().order_by("-published")
		serializer = PostSerializer(posts, many=True)
		return Response(serializer.data)
		# return 200





	def post(self,request):
		title = request.data['title']
		slug = request.data['slug']
		category = request.data['category']
		price = request.data['price']
		priceCurrency = request.data['priceCurrency']
		pricePerMeter = request.data['pricePerMeter']
		city = request.data['city']
		аddress = request.data['address']
		description = request.data['description']
		offerId = request.data['offerId']
		contacts = request.data['contacts']
		body = request.data['body']
		source = request.data['source']
		# images_list = json.loads(request.data['images'])
		images_list = request.data['images']
		preview = request.data['preview']
		

		print(images_list)
		print(type(images_list))

		post = Post.objects.update_or_create(offerId=offerId, defaults={
			"title":title,
			"slug":slug,
			"category" :category,
			"price":price,
			"priceCurrency":priceCurrency,
			"pricePerMeter":pricePerMeter,
			"city":city,
			"address":аddress,
			"description":description,
			"offerId":offerId,
			"contacts":contacts,
			"body":body,
			"source":source,
			"preview":preview,
			"images": images_list
		})
		
		print("=== Creating post in api section ===")
		print(post[1])
		
		serializer = PostSerializer(post)


		return Response(serializer.data)
		# return HttpResponse(200)


















class PostContactApiView(GenericAPIView):
	serializer_class = PostSerializer
	queryset = Post.objects.all()

	def get(self,request):
		posts = Post.objects.filter(contacts=False).order_by("-published")
		serializer = PostSerializer(posts, many=True)
		return Response(serializer.data)







class PostContactGetView(GenericAPIView):
	serializer_class = PostSerializer
	queryset = Post.objects.all()

	def get(self,request):
		posts = Post.objects.filter(contacts=False).order_by("-published")[:20]
		serializer = PostSerializer(posts, many=True)
		return Response(serializer.data)















class PostContactDetailApiView(GenericAPIView):
	serializer_class = PostSerializer
	queryset = Post.objects.all()


	def get(self,request, pk):
		posts = Post.objects.get(id=pk)
		serializer = PostSerializer(posts)
		return Response(serializer.data)




	def post(self,request,pk):
		print("=== IN POST ===")
		print("PK = ", pk)


		post = Post.objects.get(id=pk)
		serializer = PostSerializer(post)
		
		# post_images = post.images.all()

		# Previous Images Deletion
		if request.data['imagesStatus']:
			post.imagesProp = request.data['images']




			# for i in post_images:
			# 	i.delete()
				
			# for i in request.data['images']:
			# 	print('NEW Image: ',i)
			# 	post_image = post.images.create(post=post, url=i).save()
			# 	print(post_image)


		#   bodyHtml = post.body + request.data['contact']
		post.contact_body = request.data['contact']
		#   post.body = bodyHtml



		post.contacts = True
		post.save()

		return Response(serializer.data)




















class PostDeleteApiView(GenericAPIView):
	def get(self,request):
		for i in Post.objects.all():
			print("=== Post deleting === : ", i.id)
			i.delete()

		return HttpResponse(200)





import time

class PostContactFalse(GenericAPIView):
	def get(self, request):
		posts = Post.objects.filter(contacts=True)
		print(len(posts))
		for i in posts:
			i.contacts = False
			i.contact_body = ""
			i.save()
			time.sleep(0.3)
			print("==== CONTACTS ARE ALL FALSE ====")
		return HttpResponse(200)