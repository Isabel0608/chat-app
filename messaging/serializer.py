from rest_framework import serializers
from.models import Author, Message

class Authorserializer (serializers.ModelSerializer):
    profile_picture = serializers.ImageField(allow_empty_file=True, required=False)


    class Meta:
       model = Author
       fields = "__all__"


class Messageserializer (serializers.ModelSerializer):
    author = Authorserializer(read_only=True)
    class Meta: 
        model = Message
        fields = "__all__"
