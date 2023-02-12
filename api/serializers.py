from rest_framework import fields, serializers
from main.models import  Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = ['title','price', 'offerId', 'priceCurrency',"pricePerMeter","city","address","description","offerId","body", "source"]
        fields = ['title','source', 'offerId', 'id']