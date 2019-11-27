# from django.shortcuts import render
# from django.contrib.auth import get_user_model 
# from rest_framework import status
# from rest_framework.response import Response 
# from social.apps.django_app import load_strategy 
# from social.apps.django_app.utils import load_backend 
# from social.backends.oauth import BaseOAuth1, BaseOAuth2
# from social.exceptions import AuthAlreadyAssociated 

# User = get_user_model()


# class SocialSignUp(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = SocialSignUpSerializer
#     permission_classes = (IsAuthenticatedOrCreate,)

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         provider = request.data['provider']
#         authed_user = request.user if not request.user.is_anonymous() else None 
#         strategy = load_strategy(request)
#         backend = load_backend(strategy=strategy, name=provider, redirect_url=None)
#         if isinstance(backend, BaseOAuth1):
#             token = {
#                 'oauth_token': request.data['access_token'],
#                 'oauth_token_secret': request.data['access_token_secret'],
#             }
#         elif isinstance(backend, BaseOAuth2):
#             token = request.data['access_token']
#             try:
#                 user = backend.do_auth(token, user=authed_user)
#             except AuthAlreadyAssociated:
#                 return Response(("Errors: That social media account is already in use"), status = status.HTTP_400_BAD_REQUEST)
            
#             if user and user.is_active:
#                 auth_created = user.social_auth.get(provider=provider)
#                 if not auth_created.extra_data['access_token']:
#                     auth_created.extra_data['access_token'] = token
#                     auth_created.save()
#                 serializer.instance = user 
#                 headers = self.get_success_headers(serializer.data)
#                 return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#             else:
#                 return Response(("Errors: Error with social authentication"), status=status.HTTP_400_BAD_REQUEST)