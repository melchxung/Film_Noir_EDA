# Album Film Noir Exploratory Data Analysis 

- Goal: Preform data analysis on Film Noir by Faouzia
  - cluser the songs so each row is a song
  - easier to analyze musical/lyrical patterns across the album
  
- Background: Faouzia Ouihya is a Moroccan-Canadian singer who released her debut album [Film Noir](https://open.spotify.com/album/0FffqcK2whBazSFcAIxebQ) on 11/7/2025.

### Dataset
 - using Spotify API pull for each track if possible:
  - Musical Features
    - danceability
    - energy
    - valence
    - tempo
    - acousticness
    - instrumentalness
    - liveness
    - loudness
    - speechiness
  - Lyric Features
   - sentiment polarity
   - subjectivity
   - word count
   - vocabulary richness
   - % of positive/negative emotional words
   - topic clusters (using TF-IDF or embeddings)
   - predominant themes
  - Metadata
    - track length
    - genre tagging
    - collaboration or not
    - release order

### Univariable Analysis
- Distribution of tempo
- Distribution of valence
- Distribution of song sentiment socres
- Distribution of track length
- Distribution of lyrical themes (bar plots)

### Bivariate Analysis
examples will determin later
- Sentiment vs Valence
- Energy vs Acousticness
- Track length vs Sentiment
- Tempo vs Topic Cluster

### Multivariate Analysis
- Normalize features (StandardScaler)
- Select impt deatures (e.g. temp, energy, sentiment, valence, acousticness)
- Try multiple values of k (2-10)
- Use Elbow Method to find best k
- Use Silhouette Score to confirm cluseter quality
- Train KMeans(k) on your scaled features

### Interpreting Clusters
- Cluster 0

### Summary Statistics on Clusters
  
### Which Cluster of songs represent Faouzia's strongest commercial direction?

### Deliverables
- dataset
- final report/pdf
- dashboard?

- from: https://www.youtube.com/watch?v=iwUli5gIcU0&list=PLi5spBcf0UMXfbMt1X2bHQkk7mHXkTUhs&index=2
- to personalize it:
  - maybe spotify data from album: film noir by Faouzia to predict based off of most listened to song
  - do all in vs code aka use jupiternote book lib in vs code

- End Results
  - document everything in the README code w the data analysis

##Steps
- create vs code project in .venv
- imported libraries pands, seaborn, matplotlib, sklearn
