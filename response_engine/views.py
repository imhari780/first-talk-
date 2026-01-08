from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .schemas import ResponseEngineRequest
from .services import generate_response

@csrf_exempt
def response_engine(request):
    if request.method != "POST":
        return JsonResponse({"code": "METHOD_NOT_ALLOWED"}, status=405)

    try:
        payload = json.loads(request.body)
        data = ResponseEngineRequest(**payload)

        result = generate_response(
            room_type=data.room_type,
            recent_interactions=data.recent_interactions,
            semantic_context=data.semantic_context
        )

        return JsonResponse(result, status=200)

    except Exception:
        # Silent failure allowed (PDF rule)
        return JsonResponse({}, status=200)
