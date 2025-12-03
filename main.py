import pandas as pd
import seaborn as sns
import matplotlib
from sklearn.cluster import KMeans
from src.spotify_api import create_album_csv, get_token

token = get_token()

create_album_csv(token, "Film Noir", "Faouzia", filename = "film_noir_data.csv")