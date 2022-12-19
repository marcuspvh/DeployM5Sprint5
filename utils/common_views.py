# from rest_framework.views import APIView, Request, Response, status


# class PostCommonView:
#     def create(self, request: Request) -> Response:
        
#         serializer = self.view_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         serializer.save()

#         return Response(serializer.data, status.HTTP_201_CREATED)

# class GetCommonView:
#     def list(self, request: Request)-> Response:
       
#         query_set = self.view_query_set.all()

#         serializer = self.view_serializer(query_set, many=True)

#         return Response(serializer.data, status.HTTP_200_OK)


# class PostGetCommonView(PostCommonView, GetCommonView, APIView) :
#     def get(self, request: Request)-> Response:
#         return super().list(request)

#     def post(self, request: Request) -> Response:
#         return super().create(request)


# class OmlyGetCommonView(GetCommonView, APIView) :
#     def get(self, request: Request)-> Response:
#         return super().list(request)


# class OmlyPostCommonView(PostCommonView, APIView) :
#     def post(self, request: Request) -> Response:
#         return super().create(request)
