from flask import Blueprint, request, abort, jsonify
from apps.memory_usage.models import MemoryUsage


memory_usage_blueprint = Blueprint(
    "memory_usage", __name__, url_prefix="/api/memory_usage"
)


@memory_usage_blueprint.route("/", methods=["GET"])
def get_memory_usage():
    offset = int(request.args.get("offset", 0))
    limit = min(int(request.args.get("limit", 25)), 25)
    memory_usages = MemoryUsage.objects().skip(offset).limit(limit)
    return [memory_usage.get_payload() for memory_usage in memory_usages]


@memory_usage_blueprint.route("/create", methods=["POST"])
def create_memory_usage():
    memory_usage = MemoryUsage.create(request.json)
    payload = memory_usage.get_payload()
    return payload


@memory_usage_blueprint.route("/<memory_usage_id>/update", methods=["PUT"])
def update_memory_usage(memory_usage_id):
    percent = request.json.get("percent")
    if not percent:
        abort(400, "Please provide percent field")
    memory_usage = MemoryUsage.objects(id=memory_usage_id).first()
    if not memory_usage:
        abort(404, "MemoryUsage object is not found")
    memory_usage.modify(set__percent=percent)
    return memory_usage.get_payload()
