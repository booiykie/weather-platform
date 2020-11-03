from rest_framework import serializers
# from weather.models import Weather

class WeatherSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    date = serializers.DateField()
    high = serializers.IntegerField()
    low = serializers.IntegerField()

    # def create(self, validated_data):
    #     return Weather(id=None, **validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance