from rest_framework import views
from rest_framework.response import Response

 
class ComputeTotals(views.APIView):
  """
  Computes totals for all cell ranges.
  """
  permission_classes = []

  def get(self, request, *args, **kwargs):
    """
    Return a hardcoded response.
    """
    return Response({"success": True, "content": "Hello World!"})
