from django.contrib import admin
from django.urls import path,include
from .views import CreateLandChangeView,RetriveLandchangeView,\
RetriveUpdateDestroyLandchangeView,CreateAdminView,AdminUserView,AdminUserRetrieveUpdateDestroyView,\
CreateCommentView,CommentView,CommentRetrieveUpdateDestroyView,CreateAddressView

urlpatterns = [
    path('createlandchange/',CreateLandChangeView.as_view()),
    path('landchange/',RetriveLandchangeView.as_view()),
    path('landchange/<int:pk>',RetriveUpdateDestroyLandchangeView.as_view()),
    path('createadminuser/',CreateAdminView.as_view()),
    path('adminuser/',AdminUserView.as_view()),
    path('adminuser/<int:pk>',AdminUserRetrieveUpdateDestroyView.as_view()),
    path('createcomment/',CreateCommentView.as_view()),
    path('comment/',CommentView.as_view()),
    path('comment/<int:pk>',CommentRetrieveUpdateDestroyView.as_view()),
    path('createaddress/',CreateAddressView.as_view()),
    # path('address/',AddressView.as_view())

]