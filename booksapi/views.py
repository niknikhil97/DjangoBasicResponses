from django.shortcuts import render
from rest_framework.views import APIView
from booksapi.models import Book
from booksapi.serializers import BookSerializer
from rest_framework.response import Response
# Create your views here.

class BookView(APIView):

    def get(self,request,format=None):
        books=Book.objects.all()
        serializer=BookSerializer(books,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)



class BookDetailView(APIView):

    def get(self,request,id):
        a=Book.objects.get(pk=id)
        serializer=BookSerializer(a)
        return Response(serializer.data)

    def put(self,request,id):
        a=Book.objects.get(pk=id)
        serializer=BookSerializer(instance=a,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self,request,id):
        a=Book.objects.get(pk=id)
        serializer=BookSerializer(a)
        a.delete()
        return Response(serializer.data)

    def patch(self,request,id):
        a=Book.objects.get(pk=id)
        serializer=BookSerializer(instance=a,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
