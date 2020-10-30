  
from rest_framework import serializers 
from api.models import Delivery
 
 
class DeliverySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Delivery
        fields = ('id',
                  'x',
                  'y')