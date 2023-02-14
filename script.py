import requests
import psycopg2
import os

# Connect to Postgres
conn = psycopg2.connect(dbname=os.environ.get("POSTGRES_DB"), user=os.environ.get("POSTGRES_USER"),
                        password=os.environ.get("POSTGRES_PASSWORD"))

cur = conn.cursor()

# Get data about missions, rockets and launches from GraphQL API
url = "https://spacex-production.up.railway.app/"

# Get data about rockets
query = """
query {
    rockets {
        name
        description
      active
      company
      boosters
      cost_per_launch
      country
      diameter {
        meters
      }
      mass {
        kg
      }
      type
      wikipedia
      id
      height {
        meters
      }
      engines {
        number
      }
      first_flight
    }
}
"""
response = requests.post(url, json={'query': query})
data = response.json()['data']['rockets']

# Insert data into Postgres
for item in data:
    cur.execute('''INSERT INTO rockets (rocket_name, rocket_description, rocket_active, rocket_company, rocket_boosters, rocket_cost_per_launch, rocket_country, rocket_diameter,
                rocket_mass, rocket_type, rocket_wikipedia, rocket_id, rocket_height, rocket_engines, rocket_first_flight) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                (item['name'], item['description'], item['active'], item['company'], item['boosters'], item['cost_per_launch'], item['country'], item['diameter']['meters'],
                item['mass']['kg'], item['type'], item['wikipedia'], item['id'], item['height']['meters'], item['engines']['number'], item['first_flight']))

# Get data about missions
query = """
query {
    missions {
        name
        description
        manufacturers
        wikipedia
        website
        twitter
        id
    }
}
"""
response = requests.post(url, json={'query': query})
data = response.json()['data']['missions']

# Insert data into Postgres
for item in data:
    cur.execute('''INSERT INTO missions (mission_name, mission_description, mission_manufacturers, mission_wikipedia, mission_website, mission_twitter, mission_id) VALUES (%s, %s, %s, %s, %s, %s, %s)''',
                (item['name'], item['description'], item['manufacturers'], item['wikipedia'], item['website'], item['twitter'], item['id']))

# Get data about missions from launches (because missions API is not working)
query = """
query {
  launches {
    mission_id
    mission_name
  }
}
"""
response = requests.post(url, json={'query': query})
data = response.json()['data']['launches']

for item in data:
    cur.execute('''INSERT INTO missions (mission_name, mission_id) VALUES (%s, %s)''',
                (item['mission_name'], item['mission_id']))

# Get data about launches
query = """
query {
  launches {
    id
    launch_date_local
    details
    rocket {
      rocket {
        id
        name
      }
    }
    mission_id
    mission_name
    links {
      article_link
      video_link
      wikipedia
    }
  }
}
"""
response = requests.post(url, json={'query': query})
data = response.json()['data']['launches']

# Insert data into Postgres
for item in data:
    cur.execute('''INSERT INTO launches (launch_id, launch_date_local, launch_details, launch_rocket_id, launch_rocket_name, launch_mission_id, launch_mission_name, launch_article_link,
                launch_video_link, launch_wikipedia) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                (item['id'], item['launch_date_local'], item['details'], item['rocket']['rocket']['id'], item['rocket']['rocket']['name'], item['mission_id'], item['mission_name'],
                item['links']['article_link'], item['links']['video_link'], item['links']['wikipedia']))

# Commit changes
conn.commit()

# Close connection
cur.close()
conn.close()