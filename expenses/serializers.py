from rest_framework import serializers

from expenses import models


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Expense
        fields = "__all__"


# class ExpenseSerializer(serializers.Serializer):
#     amount = serializers.IntegerField()
#     title = serializers.CharField()
#     active = serializers.BooleanField()
#     date = serializers.DateField()
#     colors = serializers.ListSerializer(child=serializers.CharField())
