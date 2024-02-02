Topic: Weather Data Logger / *"North Carolina Elemental Excursions: Embrace the Weather in Every Step

Dataset: Open-Meteo
https://open-meteo.com/en/docs/historical-weather-api/

Proposal: "North Carolina Elemental Excursions: Embrace the Weather in Every Step" is an ambitious and innovative data analysis project that seeks to revolutionize the way individuals plan and experience their journeys. At its core, the project aims to seamlessly integrate weather data into the travel planning process, offering users a comprehensive and personalized understanding of weather conditions throughout their excursions.

## Database Design

For our Coordinates table, we first gathered the Latitude and Longitude of each city selected using data from Google Maps, and stored that data in a CSV. We then added a primary key distinguishing each city (nc01 - nc12).

For our Climate table, we retrieved the CSVs of for each of the cities and stored them in our repo. From their we combined the CSVs into one large Pandas DataFrame. From there we added the foreign key to each record based on the city. We then added a unique identifier to each record to be the climate table's primary key.

We then chose to store our data using postgreSQL. We chose SQL over noSQL since all of our data here is tabular, and was downloaded as CSVs. That made the upload into postgreSQL simple. Our Coordinates table is linked to the Climate table using the NC_ID. That can be seen in the ERD found in the repo (Weather_ERD.png).

Primary Github repository : https://github.com/janthonyiv98/Project_3
