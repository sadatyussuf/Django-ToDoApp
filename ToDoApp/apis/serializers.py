from rest_framework import serializers

from projectApp import models



class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            # 'description',
        )
        model = models.todoModel