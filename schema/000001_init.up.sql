CREATE TABLE IF NOT EXISTS missions (
    mission_id VARCHAR(255) NOT NULL,
    mission_name VARCHAR(255) NOT NULL,
    mission_description TEXT,
    mission_manufacturer VARCHAR(255),
    mission_wikipedia VARCHAR(255),
    mission_website VARCHAR(255),
    mission_twitter VARCHAR(255),

    PRIMARY KEY (mission_id)
);

CREATE TABLE IF NOT EXISTS rockets (
    rocket_id VARCHAR(255) NOT NULL,
    rocket_name VARCHAR(255) NOT NULL,
    rocket_description TEXT NOT NULL,
    rocket_active BOOLEAN NOT NULL,
    rocket_company VARCHAR(255) NOT NULL,
    rocket_boosters INT NOT NULL,
    rocket_cost_per_launch INT NOT NULL,
    rocket_country VARCHAR(255) NOT NULL,
    rocket_diameter INT NOT NULL,
    rocket_mass INT NOT NULL,
    rocket_type VARCHAR(255) NOT NULL,
    rocket_wikipedia VARCHAR(255) NOT NULL,
    rocket_height INT NOT NULL,
    rocket_engines INT NOT NULL,
    rocket_first_flight VARCHAR(255) NOT NULL,

    PRIMARY KEY (rocket_id)
);

CREATE TABLE IF NOT EXISTS launches (
    launch_id VARCHAR(255) NOT NULL,
    launch_date_local VARCHAR(255) NOT NULL,
    launch_details TEXT,
    launch_rocket_id VARCHAR(255) NOT NULL,
    launch_rocket_name VARCHAR(255) NOT NULL,
    launch_mission_id VARCHAR(255) NOT NULL,
    launch_mission_name VARCHAR(255) NOT NULL,
    launch_article_link VARCHAR(255),
    launch_video_link VARCHAR(255),
    launch_wikipedia VARCHAR(255),

    PRIMARY KEY (launch_id),
    FOREIGN KEY (launch_rocket_id) REFERENCES rockets (rocket_id),
    FOREIGN KEY (launch_mission_id) REFERENCES missions (mission_id)
);