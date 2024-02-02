# "North Carolina Elemental Excursions: Embrace the Weather in Every Step"
   ## Weather Data Logger 

Dataset: Visual Crossing
[https://www.visualcrossing.com/weather-api]

  This analysis provides valuable insights into the climatic conditions experienced throughout the year, offering a comprehensive perspective for planning a trip to North Carolina. Seasonal averages were meticulously calculated for key meteorological parameters, allowing travelers to understand the nuanced weather dynamics. During the spring season (March 20 to June 21), temperatures in North Carolina tend to rise, accompanied by moderate humidity levels and occasional precipitation, creating a vibrant and comfortable atmosphere. The summer months (June 21 to September 23) bring warmer temperatures, higher humidity, and potential variations in precipitation, creating an ideal environment for outdoor activities. Fall (September 22 to December 21) is characterized by decreasing temperatures, stable humidity, and potential changes in precipitation patterns, providing a picturesque backdrop of colorful foliage. As winter sets in (December 21 to March 19), North Carolina experiences cooler temperatures, lower humidity, and the possibility of snowfall, offering a unique winter experience. This tailored analysis empowers travelers, researchers, and weather enthusiasts alike to make informed decisions and appreciate the diverse weather conditions across North Carolina's cities.

## Database Design

For our Coordinates table, we first gathered the Latitude and Longitude of each city selected using data from Google Maps, and stored that data in a CSV. We then added a primary key distinguishing each city (nc01 - nc12).

For our Climate table, we retrieved the CSVs of for each of the cities and stored them in our repo. From their we combined the CSVs into one large Pandas DataFrame. From there we added the foreign key to each record based on the city. We then added a unique identifier to each record to be the climate table's primary key.

We then chose to store our data using postgreSQL. We chose SQL over noSQL since all of our data here is tabular, and was downloaded as CSVs. That made the upload into postgreSQL simple. Our Coordinates table is linked to the Climate table using the NC_ID. That can be seen in the ERD found in the repo (Weather_ERD.png).

Primary Github repository : https://github.com/janthonyiv98/Project_3
