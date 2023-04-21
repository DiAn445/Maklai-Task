import re
from nltk import Tree
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from BinarTreeApi.paraphrase import paraphrase
from .serializers import ParaphraseSerializer


class ParaphraseAPIView(APIView):
    def get(self, request):
        # Creating serializer and validator
        serializer = ParaphraseSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        tree = serializer.validated_data.get('tree', None)
        limit = serializer.validated_data['limit']

        # If 'tree' is not present, just returns standard interface DRF
        if tree is None:
            return Response(status=status.HTTP_200_OK)

        result = []

        # Get from str Tree instance
        tree = Tree.fromstring(tree)

        for i in range(limit):
            # cleaning string according to task's output by means of re
            result.append({"tree": re.sub(r'\s{2,}|\n', ' ', str(paraphrase(tree)))})

        return Response({"paraphrases": result})
