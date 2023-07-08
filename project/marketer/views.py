from .serializer import MarkterSerializers
from rest_framework import status,generics,permissions
from .models import marketer
from django.http import JsonResponse
from rest_framework.response import Response


class MarketerView(generics.CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = MarkterSerializers
    def post(self, request):
        try:
            serializers = MarkterSerializers(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(status=status.HTTP_200_OK, data = ({'status':status.HTTP_200_OK,
                             "data":serializers.data,
                             "message":"the Marketer is added"
                             }))
            return Response(status=status.HTTP_400_BAD_REQUEST, data =({'status':status.HTTP_400_BAD_REQUEST,
                             "error":serializers.errors,
                             }))
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data =({'status':status.HTTP_500_INTERNAL_SERVER_ERROR,
                             "error": " somthing went wrong",
                             }))
        

class MarketerList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = marketer.objects.all()
    serializer_class = MarkterSerializers
    def list(self,request):
        queryset = self.get_queryset()
        serializer = MarkterSerializers(queryset, many=True)
        data = serializer.data
        length = len(data)
        return Response(status=status.HTTP_200_OK, data =({'status':status.HTTP_200_OK,
                             "data":data,
                             "total_item": length,
                             }))
        
class MarketerDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = marketer.objects.all()
    serializer_class = MarkterSerializers
    lookup_field = "id"
    def page(self,request):
        queryset = self.get_queryset()
        
        serializer = MarkterSerializers(queryset)
        return Response({'status':status.HTTP_200_OK,
                             "data":serializer.data,
                             
                             })
        # if marketer.balance < MINIMUM_BALANCE:
        #     response_text = 'Sending Amount'
        #     response_color = 'red'
        # else:
        #     response_text = 'Balance: {}'.format(marketer.balance)
        #     response_color = 'black'
        # response = Response(response_text)
        # response['X-Message'] = response_text
        # response['X-Color'] = response_color
        # return response

