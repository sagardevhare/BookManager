from rest_framework import serializers
from .models import Book,Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'date_of_birth', 'nationality']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()


    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre', 'published_date']

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        author = Author.objects.create(**author_data)
        book = Book.objects.create(author=author, **validated_data)
        return book  

    def update(self, instance, validated_data):
        author_data = validated_data.pop('author', None)
        if author_data:
            author_instance, _ = Author.objects.get_or_create(**author_data)
            instance.author = author_instance

        instance.title = validated_data.get('title', instance.title)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.save()
        return instance  