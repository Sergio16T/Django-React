from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    text = serializers.CharField(max_length=256, required=True)
    status = serializers.BooleanField(required=True)

    def create(self, validated_data):
        # Once the request data has been validated, we can create a todo item instance in the database
        return Todo.objects.create(
            text=validated_data.get('text'),
            status=validated_data.get('status'),
        )

    def update(self, instance, validated_data):
        # Once the request data has been validated, we can update the todo item instance in the database
        instance.text = validated_data.get('text', instance.text)
        # use instance.text as default value to be returned in case key 'text' does not exist.
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        return instance

    class Meta:
        model = Todo
        fields = (
            'id',
            'text',
            'status',
        )
