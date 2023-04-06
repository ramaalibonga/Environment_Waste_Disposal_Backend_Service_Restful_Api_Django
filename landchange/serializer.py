from rest_framework import serializers
from .models import Landchange,Admin,Address,Comment

class CreateLandViewSerializer(serializers.ModelSerializer):
     class Meta:
          model = Landchange
          fields = '__all__'

class RetriveLandchangeViewSerializer(serializers.ModelSerializer):
       class Meta:
           model = Landchange
           fields = '__all__'
           depth=1

class RetrieveUpdateDestroyLandchangeViewSerializer(serializers.ModelSerializer):
       class Meta:
            model = Landchange
            fields = '__all__'
            depth=1

class CreateAdminSerializer(serializers.ModelSerializer):
       class Meta:
             model = Admin
             fields = '__all__'

class AdminUserSerializer(serializers.ModelSerializer):
       class Meta:
             model = Admin
             fields = '__all__'
             depth=1

class AdminUserRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
          class Meta:
             model = Admin
             fields = '__all__'
             depth=1

class CreateCommentSerializer(serializers.ModelSerializer):
          class Meta:
                model = Comment
                fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
           class Meta:
                model = Comment
                fields = '__all__'
                depth=1

class CommentRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
           class Meta:
                model = Comment
                fields = '__all__'
                depth=1


class CreateAddressSerializer(serializers.ModelSerializer):
          class Meta:
                model = Address
                fields = '__all__'


# class RetrieveAddressViewserializer(serializers.ModelSerializer):
#           class Meta:
#                 model = Address
#                 fields = '__all__'
                # depth=1
