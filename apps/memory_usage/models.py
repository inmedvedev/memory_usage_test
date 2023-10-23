from mongoengine import Document, DateTimeField, FloatField
from datetime import datetime


class MemoryUsage(Document):
    created_at = DateTimeField(default=datetime.utcnow)
    percent = FloatField()

    @classmethod
    def create(cls, data: dict) -> "MemoryUsage":
        self = cls(
            percent=data.get("percent"),
        )
        self.save()
        return self

    def get_payload(self):
        payload = self.to_mongo()
        payload["_id"] = str(payload["_id"])
        return payload
