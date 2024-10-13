import pymongo

def connect_to_mongodb(connection_string):
    """Connects to MongoDB and returns a MongoClient object.

    Args:
        connection_string (str): The MongoDB connection string.

    Returns:
        MongoClient: The MongoClient object.
    """

    client = pymongo.MongoClient(connection_string)
    return client

def get_collection(client, database_name, collection_name):
    """Gets a MongoDB collection.

    Args:
        client (MongoClient): The MongoDB client.
        database_name (str): The name of the database.
        collection_name (str): The name of the collection.

    Returns:
        Collection: The MongoDB collection.
    """

    db = client[database_name]
    collection = db[collection_name]
    return collection

def insert_document(collection, document):
    """Inserts a document into a MongoDB collection.

    Args:
        collection (Collection): The MongoDB collection.
        document (dict): The document to insert.

    Returns:
        InsertOneResult: The result of the insertion.
    """

    result = collection.insert_one(document)
    return result

def find_documents(collection, query={}, projection=None):
    """Finds documents in a MongoDB collection.

    Args:
        collection (Collection): The MongoDB collection.
        query (dict, optional): The query filter. Defaults to an empty dictionary.
        projection (dict, optional): The projection fields. Defaults to None.

    Returns:
        Cursor: A cursor object representing the found documents.
    """

    results = collection.find(query, projection)
    return results

def update_document(collection, query, update):
    """Updates a document in a MongoDB collection.

    Args:
        collection (Collection): The MongoDB collection.
        query (dict): The query filter.
        update (dict): The update operations.

    Returns:
        UpdateResult: The result of the update.
    """

    result = collection.update_one(query, update)
    return result

def delete_document(collection, query):
    """Deletes a document from a MongoDB collection.

    Args:
        collection (Collection): The MongoDB collection.
        query (dict): The query filter.

    Returns:
        DeleteResult: The result of the deletion.
    """

    result = collection.delete_one(query)
    return result