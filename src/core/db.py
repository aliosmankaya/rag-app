import os
from pymilvus import MilvusClient


class DB:
    path = f"{os.path.abspath(os.curdir)}/src/db"
    if not os.path.exists(path):
        os.makedirs(path)
    client = MilvusClient("src/db/milvus.db")

    @classmethod
    def create_collection(cls, name: str, dim: int):
        if cls.client.has_collection(name):
            cls.client.drop_collection(name)

        cls.client.create_collection(
            collection_name=name,
            dimension=dim,
            metric_type="IP",
            consistency_level="Strong",
        )

    @classmethod
    def insert_collection(cls, name: str, data: list):
        cls.client.upsert(collection_name=name, data=data)

    @classmethod
    def list_collection(cls):
        return cls.client.list_collections()

    @classmethod
    def search(cls, name: str, data: list, limit: int):
        return cls.client.search(
            collection_name=name,
            data=[data],
            limit=limit,
            search_params={"metric_type": "IP", "params": {}},
            output_fields=["text"],
        )

    @classmethod
    def update_collection(cls, name: str, new_name: str):
        cls.client.rename_collection(old_name=name, new_name=new_name)

    @classmethod
    def delete_collection(cls, name: str):
        cls.client.delete(collection_name=name)
