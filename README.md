# "North Carolina Elemental Excursions: Embrace the Weather in Every Step"
   ## Weather Data Logger 

Dataset: Visual Crossing
[https://www.visualcrossing.com/weather-api]

  This analysis provides valuable insights into the climatic conditions experienced throughout the year, offering a comprehensive perspective for planning a trip to North Carolina. Seasonal averages were meticulously calculated for key meteorological parameters, allowing travelers to understand the nuanced weather dynamics. During the spring season (March 20 to June 21), temperatures in North Carolina tend to rise, accompanied by moderate humidity levels and occasional precipitation, creating a vibrant and comfortable atmosphere. The summer months (June 21 to September 23) bring warmer temperatures, higher humidity, and potential variations in precipitation, creating an ideal environment for outdoor activities. Fall (September 22 to December 21) is characterized by decreasing temperatures, stable humidity, and potential changes in precipitation patterns, providing a picturesque backdrop of colorful foliage. As winter sets in (December 21 to March 19), North Carolina experiences cooler temperatures, lower humidity, and the possibility of snowfall, offering a unique winter experience. This tailored analysis empowers travelers, researchers, and weather enthusiasts alike to make informed decisions and appreciate the diverse weather conditions across North Carolina's cities.

## Database Design

For our Coordinates table, we first gathered the Latitude and Longitude of each city selected using data from Google Maps, and stored that data in a CSV. We then added a primary key distinguishing each city (nc01 - nc12).

For our Climate table, we retrieved the CSVs for each of the cities and stored them in our repo. From there we combined the CSVs into one large Pandas DataFrame. From there we added the foreign key to each record based on the city. We then added a unique identifier to each record to be the climate table's primary key.

We then chose to store our data using postgreSQL. We chose SQL over noSQL since all of our data here is tabular, and was downloaded as CSVs. That made the upload into postgreSQL simple. Our Coordinates table is linked to the Climate table using the NC_ID. That can be seen in the ERD found in the repo (Weather_ERD.png).

Primary Github repository : https://github.com/janthonyiv98/Project_3
Resource used: https://raredogmarketing.com/resources/combining-multiple-csv-files-into-one-file-using-python-step-by-step-guide

## Visualizations

Using MatPlotLib and Python functions we learned earlier in the bootcamp, we created simple visualizations to aid in the decision-making process for vacationers in North Carolina. The first of these visualizations was a line chart comparing the average daily temperatures across the entirety of 2023 for the cities in our list. Adding an extra layer of customization, we used Python to create a basic app where the user inputs three cities of their choice from the group of 12 to further tailor the line chart to their potential plans. This was accomplished using input functions and then combining the three responses into a single variable to create a new filtered DataFrame and graph focused on the selected cities. In the Jupyter Notebook found in our repository, you can find an example of a temperature comparison between Boone, Charlotte and Wilmington.

We also created bar graphs detailing the number of rainy and snowy days experienced by each of our cities in 2023, giving further context to the type of weather vacationers may come to expect at various North Carolina destinations. This was done by tapping into the "icon" column in our CSV file, which noted the prevailing weather condition for each given day (i.e. sunny, partly cloudy, rain, snow, etc.).

In addition, we generated heat maps displaying the seasonal average temperatures of these cities. We restructured the data utilizing Pandas to tailor DataFrames as needed and explored Seaborn, a new library, to build these vibrant graphs. ​Seaborn, renowned for its thorough documentation, offers a variety of engaging options for statistical data visualization. It provides a user-friendly installation process and furnishes robust tools for developing intricate statistical analyses.

For further information, please refer to:  https://seaborn.pydata.org/index.html
