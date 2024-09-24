"""
search_songs.py

Description:
    Assists in fetching songs from the database
"""

from pymilvus import connections, utility, Collection

def fetch_songs(collection, danceability=0.5, valence=0.5, genre="acoustic", ret_num=1):
    """
    Fetches a list of songs from database. To fetch the name do: 
    result[idx].entity.get('track_name')

    Args:
        collection (Collection): A Milvus databse collection object
        danceability (float, optional): Value for danceability. Defaults to 0.5.
        valence (float, optional): Value for valence. Defaults to 0.5.
        genre (str, optional): Value for track_genre. Defaults to "acoustic".
        ret_num (int, optional): Number of songs to return. Defaults to 1.

    Returns:
        list: List of songs
    """
    result = collection.search(
        data=[[danceability, valence]],  # query vectors
        anns_field="danceability_valence",
        param={"params": {"nprobe": 10}},
        limit=ret_num,  # number of returned entities
        expr=f"track_genre=='{genre}'",
        output_fields=["track_name", "danceability_valence"],  # specifies fields to be returned
    )[0]
    return result

def main():
    """
    Main Function

    Raises:
        ConnectionError: When connection to Milvus Database fails
        NameError: When the name of database is incorrect
    """
    try:
        connections.connect("default", host="localhost", port="19530")
        print("Connected to Milvus.")
    except Exception as e:
        raise ConnectionError(f"Failed to connect to Milvus: {e}") from e

    collection_name = "songs_db"
    if not utility.has_collection(collection_name):
        raise NameError(f"Could not find collection with name [{collection_name}]")

    collection = Collection(collection_name)
    collection.load()
    songs = fetch_songs(collection, ret_num=5)
    for idx, song in enumerate(songs):
        print(f"{idx}.\t{song.entity.get('track_name')}")

if __name__ == "__main__":
    main()
