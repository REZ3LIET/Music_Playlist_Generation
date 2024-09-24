import pandas as pd
from pymilvus import connections, utility, FieldSchema, CollectionSchema, DataType, Collection

def define_collection(collection_name="songs_db", desc="Song Database"):
    if utility.has_collection(collection_name):
        new_collection = input(
            f"A collection with name [{collection_name}] already exists, do you wish to overwrite \
                it? [Y/N]: "
            )
        if new_collection.lower() == "n":
            raise NameError(f"Tried to create data with pre-existing name [{collection_name}]")

        print("Deleting old collection")
        utility.drop_collection(collection_name)

    # Define fields for our collection
    fields = [
        FieldSchema(name="song_id", dtype=DataType.INT64, is_primary=True, auto_id=False),
        FieldSchema(name="track_genre", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="danceability_valence", dtype=DataType.FLOAT_VECTOR, dim=2),
        FieldSchema(name="track_name", dtype=DataType.VARCHAR, max_length=1000)
    ]

    schema = CollectionSchema(fields, description=desc)
    collection = Collection(collection_name, schema)
    return collection

def data_to_collection(collection, dataframe):
    track_genre = dataframe["track_genre"].to_list()
    danceability_valence = list(zip(
        dataframe["danceability"].to_list(),
        dataframe["valence"].to_list()
    ))
    track_name = dataframe["track_name"].to_list()
    data = [
        {
            "song_id": i,
            "track_genre": track_genre[i],
            "danceability_valence": danceability_valence[i],
            "track_name": track_name[i],
        }
        for i in range(len(danceability_valence))
    ]

    index_params = {
        "metric_type":"L2",
        "index_type":"IVF_FLAT",
        "params":{"nlist":128}
    }
    collection.create_index("danceability_valence", index_params)
    insert_result = collection.insert(data)
    print("Your database is ready")
    print(insert_result)

def main():
    try:
        connections.connect("default", host="localhost", port="19530")
        print("Connected to Milvus.")
    except Exception as e:
        raise ConnectionError(f"Failed to connect to Milvus: {e}")

    collection = define_collection()
    path = "/workspaces/Music_Playlist_Generation/music_playlist_generation/data/data.csv"
    df = pd .read_csv(path)
    data_to_collection(collection, df)

if __name__ == "__main__":
    main()