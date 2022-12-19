# from rest_framework.views import APIView, Request, Response, status
# from django.shortcuts import get_object_or_404



# class GetDetailView:
#     def retrieve(self, request: Request, *args, **kwargs) -> Response:
#         id_value = kwargs[self.url_param_name]

#         model_object = get_object_or_404(self.view_query_set, pk=id_value)

#         serializer = self.view_serializer(model_object)

#         return Response(serializer.data)



# class PatchDetailView:
#     def update(self, request: Request, *args, **kwargs) -> Response:
       
#         id_value = kwargs[self.url_param_name]

#         model_object = get_object_or_404(self.view_query_set, pk=id_value)

        
#         serializer = self.view_serializer(model_object, data=request.data, partial=True)

#         serializer.is_valid(raise_exception=True)
        
#         serializer.save()

#         return Response(serializer.data, status.HTTP_200_OK)

# class DeleteDetailView:
#     def destroy(self, request: Request, *args, **kwargs) -> Response:
       
#         id_value = kwargs[self.url_param_name]

#         model_object = get_object_or_404(self.view_query_set, pk=id_value)

#         model_object.delete()

#         return Response(status=status.HTTP_204_NO_CONTENT)

# class OnlyGetDetailView(GetDetailView, APIView):
#    def get(self, request: Request, *args, **kwargs) -> Response:
#     return super().retrieve(request, *args, **kwargs)


# class OnlyPatchDetailView(PatchDetailView, APIView):
#    def patch(self, request: Request, *args, **kwargs) -> Response:
#     return super().update(request, *args, **kwargs)

# class OnlyDeleteDetailView(DeleteDetailView, APIView):
#    def delete(self, request: Request, *args, **kwargs) -> Response:
#     return super().destroy(request, *args, **kwargs)


