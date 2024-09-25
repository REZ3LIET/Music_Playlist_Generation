# Music_Playlist_Generation | [Medium](https://medium.com/@rezeliet/creating-vector-db-with-milvus-for-multiple-features-d4c29106f727)

MPG is a project to test the working of [Milvus DB](https://github.com/milvus-io/milvus). The goal of this project is to get suggestions for songs a Vector Database.

## Installation
This project is developed in a devcontainer with following configuration:
- Ubuntu: 22.04
- Python: 3.10.12
- Docker: 27.3.1

1. To install Milvus refer [Run Milvus Standalone](https://milvus.io/docs/install_standalone-docker.md)

2. Getting the repo:
```bash
git clone https://github.com/REZ3LIET/Music_Playlist_Generation.git
```
Note: Using a Virtual Environment is preferred if not using devcontainer.

3. To get important python packages:
```bash
cd Music_Playlist_Generation
pip install -r requirements.txt
```

## Usage
### Database:
To setup the database I am using [Spotify Tracks Genre](https://www.kaggle.com/datasets/thedevastator/spotify-tracks-genre-dataset) from Kaggle. To create a vector databse run the following:
```bash
cd Music_Playlist_Generation/music_playlist_generation/scripts/
python3 songs_db.py
```

Note: To know about the process of setting up Milvus Vector Databse refer: [mpg_db_creation notebook](./music_playlist_generation/notebooks/mpg_db_creation.ipynb)

### Song Search:
To search for songs run the following:
```bash
cd Music_Playlist_Generation/music_playlist_generation/scripts/
python3 search_songs.py
```

As this is an ongoing project generating playlist is still under development.
