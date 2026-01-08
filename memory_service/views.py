from django.shortcuts import render

# Create your views here.
import math
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import VectorEntry
from .embedding import generate_embedding


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def store_embedding(request):
    try:
        payload = request.data

        embedding = generate_embedding(payload)

        VectorEntry.objects.create(
            embedding=embedding,
            source_type=payload.get("source_type", "unknown"),
            source_id=payload.get("source_id")
        )

        return Response({"status": "stored"}, status=201)

    except Exception:
        # 🔴 MEMORY FAILURE MUST NOT BREAK SYSTEM
        return Response({"status": "ignored"}, status=202)


def cosine_similarity(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    mag_a = math.sqrt(sum(x * x for x in a))
    mag_b = math.sqrt(sum(y * y for y in b))
    return dot / (mag_a * mag_b + 1e-9)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def query_similar(request):
    try:
        context_vector = request.data.get("vector")
        results = []

        for entry in VectorEntry.objects.all():
            score = cosine_similarity(context_vector, entry.embedding)
            if score >= 0.75:
                results.append({
                    "source_type": entry.source_type,
                    "score": round(score, 3)
                })

        return Response({"matches": results}, status=200)

    except Exception:
        return Response({"matches": []}, status=200)
