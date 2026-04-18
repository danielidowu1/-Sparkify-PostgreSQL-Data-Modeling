# sql_queries.py

# DROP TABLES
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# Create Tables

# Fact table
songplays_table = ("""CREATE IF NOT EXISTS songplays
                (
                    songplay_id SERIAL NOT NULL PRIMARY KEY,
                    start_time TIMESTAMP NOT NULL,
                    user_id INT NOT NULL,
                    level VARCHAR,
                    song_id VARCHAR NOT NULL,
                    artist_id VARCHAR NOT NULL, 
                    session_id INT NOT NULL, 
                    location VARCHAR, 
                    user_agent VARCHAR,
                    FOREIGN KEY (start_time) REFERENCES time (start_time),
                    FOREIGN KEY (user_id) REFERENCES users (user_id),
                    FOREIGN KEY (song_id) REFERENCES songs (song_id),
                    FOREIGN KEY (artist_id) REFERENCES artists (artist_id));
                    );
                """)

# Dimension tables
users_play_table = ("""CREATE IF NOT EXISTS Users
                (
                    user_id INT NOT NULL PRIMARY KEY,
                    first_name VARCHAR,
                    last_name VARCHAR,
                    gender VARCHAR(1),
                    level VARCHAR
                    );
                """)

songs_table = ("""CREATE IF NOT EXISTS songs
                (
                song_id VARCHAR NOT NULL PRIMARY KEY,
                title VARCHAR,
                artist_id VARCHAR NOT NULL,
                year INT NOT NULL,
                duration FLOAT NOT NULL
                );
            """)

artists_table = ("""CREATE TABLE IF NOT EXISTS artists
                (
                    artist_id VARCHAR NOT NULL PRIMARY KEY,
                    name VARCHAR,
                    location VARCHAR,
                    latitude INT,
                    longitude INT
                    );
                """)

time_table = ("""CREATE IF NOT EXISTS time
            (
                start_time TIMESTAMP NOT NULL PRIMARY KEY,
                hour INT,
                day INT,
                week INT,
                month INT,
                year INT,
                weekday INT
                );
            """)

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays ( start_time, user_id, level,
                song_id, artist_id, session_id, location, user_agent)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level
""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year,duration)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (song_id) DO NOTHING
""")

artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, latitude, longitude)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (artist_id) DO NOTHING
""")


time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (start_time) DO NOTHING
""")

# FIND SONGS
# Implement the song_select query in sql_queries.py to find the song ID and artist ID based on the title, artist name, and
# duration of a song
# get the song ID and artist ID by querying the songs and artists tables to find matches based on song title, artist name, 
# and song duration time.

song_select = ("""SELECT song_id, songs.artist_id
                FROM songs
                JOIN artists
                ON songs.artist_id = artists.artist_id
                WHERE songs.title = %s
                AND artists.name = %s
                AND songs.duration = %s;
""")

#List of Loops
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
create_table_queries = [songplays_table, user_table, songs_table, artists_table, time_table]