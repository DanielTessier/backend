from rest_framework import serializers
from .models import Connection, Entrer_code

class PageConnection(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = ['username', 'password']
        
class CodePython(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entrer_code
        fields = [
            'code'
        ]
