from pymongo import MongoClient
from typing import Dict, List, Any, Optional


class MongoManager:
    def __init__(self, host: str = "localhost", port: int = 27017,
                 username: Optional[str] = None, password: Optional[str] = None,
                 database: str = "mydatabase"):
        """
        Initialize MongoDB connection
        """
        # Construct connection URI
        if username and password:
            self.uri = f"mongodb://{username}:{password}@{host}:{port}"
        else:
            self.uri = f"mongodb://{host}:{port}"

        # Create client and database connections
        self.client = MongoClient(self.uri)
        self.db = self.client[database]

    def insert_one(self, collection: str, data: Dict) -> str:
        """
        Insert a single document into a collection
        Returns the inserted document's ID
        """
        result = self.db[collection].insert_one(data)
        return str(result.inserted_id)

    def insert_many(self, collection: str, data: List[Dict]) -> List[str]:
        """
        Insert multiple documents into a collection
        Returns list of inserted document IDs
        """
        result = self.db[collection].insert_many(data)
        return [str(id) for id in result.inserted_ids]

    def find_one(self, collection: str, query: Dict) -> Optional[Dict]:
        """
        Find a single document matching the query
        """
        result = self.db[collection].find_one(query)
        return result

    def find_many(self, collection: str, query: Dict) -> List[Dict]:
        """
        Find all documents matching the query
        """
        cursor = self.db[collection].find(query)
        return list(cursor)

    def update_one(self, collection: str, query: Dict, new_values: Dict) -> int:
        """
        Update a single document matching the query
        Returns number of modified documents
        """
        result = self.db[collection].update_one(
            query, {'$set': new_values}
        )
        return result.modified_count

    def update_many(self, collection: str, query: Dict, new_values: Dict) -> int:
        """
        Update all documents matching the query
        Returns number of modified documents
        """
        result = self.db[collection].update_many(
            query, {'$set': new_values}
        )
        return result.modified_count

    def delete_one(self, collection: str, query: Dict) -> int:
        """
        Delete a single document matching the query
        Returns number of deleted documents
        """
        result = self.db[collection].delete_one(query)
        return result.deleted_count

    def delete_many(self, collection: str, query: Dict) -> int:
        """
        Delete all documents matching the query
        Returns number of deleted documents
        """
        result = self.db[collection].delete_many(query)
        return result.deleted_count

    def close(self):
        """
        Close the MongoDB connection
        """
        self.client.close()