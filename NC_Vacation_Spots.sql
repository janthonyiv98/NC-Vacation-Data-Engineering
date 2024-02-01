CREATE DATABASE NC_vacation_spots;

CREATE TABLE Coordinates (
    city_id VARCHAR(4) NOT NULL,
    City VARCHAR(30) NOT NULL,
    Latitude DECIMAL NOT NULL,
    Longitude DECIMAL NOT NULL
    PRIMARY KEY (city_id)
);

CREATE TABLE Climate (
    id INT NOT NULL,
    NC_ID VARCHAR(4) NOT NULL,
    city_name VARCHAR(40) NOT NULL,
    datetime DATE NOT NULL,
    tempmax DECIMAL NOT NULL,
    tempmin DECIMAL NOT NULL,
    temp DECIMAL NOT NULL,
    feelslikemax DECIMAL NOT NULL,
    feelslikemin DECIMAL NOT NULL,
    feelslike DECIMAL NOT NULL,
    dew DECIMAL NOT NULL,
    humidity DECIMAL NOT NULL,
    precip DECIMAL NOT NULL,
    precipprob INT NOT NULL,
    precipcover DECIMAL NOT NULL,
    preciptype VARCHAR(30),
    snow DECIMAL NOT NULL,
    snowdepth DECIMAL NOT NULL,
    windgust DECIMAL NOT NULL,
    windspeed DECIMAL NOT NULL,
    winddir DECIMAL NOT NULL,
    sealevelpressure DECIMAL NOT NULL,
    cloudcover DECIMAL NOT NULL,
    visibility DECIMAL NOT NULL,
    solarradiation DECIMAL NOT NULL,
    solarenergy DECIMAL NOT NULL,
    uvindex DECIMAL NOT NULL,
    severerisk INT NOT NULL,
    sunrise DATETIME NOT NULL,
    sunset DATETIME NOT NULL,
    moonphase DECIMAL NOT NULL,
    conditions VARCHAR(100),
    description	VARCHAR(100),
    icon VARCHAR (100),
    stations VARCHAR (105),
    PRIMARY KEY (id),
    FOREIGN KEY (NC_ID) REFERENCES Coordinates(city_id)
);