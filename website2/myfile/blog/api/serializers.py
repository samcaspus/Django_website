from rest_framework import serializers
from blog.models import Article

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["name","data",]     