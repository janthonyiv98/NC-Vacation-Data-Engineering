# North Carolina Elemental Excursions: Embrace the Weather in Every Step

This analysis provides valuable insights into the climatic conditions experienced throughout the year, offering a comprehensive perspective for planning a trip to North Carolina. Seasonal averages were meticulously calculated for key meteorological parameters, allowing travelers to understand the nuanced weather dynamics. During the spring season (March 20 to June 21), temperatures in North Carolina tend to rise, accompanied by moderate humidity levels and occasional precipitation, creating a vibrant and comfortable atmosphere. The summer months (June 21 to September 23) bring warmer temperatures, higher humidity, and potential variations in precipitation, creating an ideal environment for outdoor activities. Fall (September 22 to December 21) is characterized by decreasing temperatures, stable humidity, and potential changes in precipitation patterns, providing a picturesque backdrop of colorful foliage. As winter sets in (December 21 to March 19), North Carolina experiences cooler temperatures, lower humidity, and the possibility of snowfall, offering a unique winter experience. This tailored analysis empowers travelers, researchers, and weather enthusiasts alike to make informed decisions and appreciate the diverse weather conditions across North Carolina's cities.

## Data Sources
* [Visual Crossing](https://www.visualcrossing.com/weather-api)
  * Downloaded a year's worth of climate data from 12 NC cities as CSVs.
* [Google Maps](https://maps.google.com/)
  * Retrieved coordinate data for the 12 NC cities, and stored as a CSV.


## Database Design
For our Coordinates table, we first gathered the Latitude and Longitude of each city selected using data from Google Maps, and stored that data in a CSV. We then added a primary key distinguishing each city (nc01 - nc12). This file is located in the main repo under `NC_Coordinate_Data.csv`.

For our Climate table, we retrieved the CSVs for each of the cities and stored them in our repo under the folder `2023_Weather_Data`. From there we combined the CSVs into one large Pandas DataFrame. From there we added the foreign key to each record based on the city. We then added a unique identifier to each record to be the climate table's primary key. This ETL process can be found in the `combine_csv.py` code file in the main repo. The resulting file, also in the main repo is titled `combined_data.csv`.
 * Resource used: https://raredogmarketing.com/resources/combining-multiple-csv-files-into-one-file-using-python-step-by-step-guide

We then chose to store our data using postgreSQL. We chose SQL over noSQL since all of our data here is tabular, and was downloaded as CSVs. That made the upload into postgreSQL simple. The schema code can be found in the main repo under `NC_Vacation_Spots.sql`. Our Coordinates table is linked to the Climate table using the NC_ID. That can be seen in the ERD found in the repo `Weather_ERD.png`. We used [Quick Database Diagrams](https://www.quickdatabasediagrams.com/) to create our ERD.

### Ethical Considerations
We specifically chose datasets that were free to access and use. Our use of the [Google Maps](https://about.google/brand-resource-center/products-and-services/geo-guidelines/#:~:text=Google%20Earth%20or%20Earth%20Studio%20can%20be%20used%20for%20purposes,any%20commercial%20or%20promotional%20purposes.) and [Visual Crossing](https://www.visualcrossing.com/weather-services-terms) data falls under the Fair Use of both of their Terms of Use, as this was an academic project. This data involves no Personally Identifiable Information.

### Data Limitations
We were only able to get a year's worth of data for 12 cities from Visual Crossing, as part of their unpaid tier. With more historical data, we could offer better recommendations.

## Visualizations

### Libaries Used
* Pandas
* MatPlotLib
* geoplotlib
* Seaborn

### How to Use
Using MatPlotLib and Python functions we learned earlier in the bootcamp, we created simple visualizations to aid in the decision-making process for vacationers in North Carolina. The first of these visualizations was a line chart comparing the average daily temperatures across the entirety of 2023 for the cities in our list. Adding an extra layer of customization, we used Python to create a basic app where the user inputs three cities of their choice from the group of 12 to further tailor the line chart to their potential plans. This was accomplished using input functions and then combining the three responses into a single variable to create a new filtered DataFrame and graph focused on the selected cities. In the Jupyter Notebook found in our repo titled `Average Temperature Line Chart.ipynb`, you can find an example of a temperature comparison between Boone, Charlotte and Wilmington.

We also created bar graphs detailing the number of rainy and snowy days experienced by each of our cities in 2023, giving further context to the type of weather vacationers may come to expect at various North Carolina destinations. This was done by tapping into the "icon" column in our CSV file, which noted the prevailing weather condition for each given day (i.e. sunny, partly cloudy, rain, snow, etc.). This can be found in the `Rainy Days Bar Chart.ipynb` and `Snowy Days Bar Chart.ipynb`.

In addition, we generated heat maps displaying the seasonal average temperatures of these cities. We restructured the data utilizing Pandas to tailor DataFrames as needed and explored Seaborn, a new library, to build these vibrant graphs. This can be found in the `maps.ipynb` file. Also included is a map of the cities we chose created using Geoplotlib.
* ​Seaborn, renowned for its thorough documentation, offers a variety of engaging options for statistical data visualization. It provides a user-friendly installation process and furnishes robust tools for developing intricate statistical analyses. For further information, please refer to: (https://seaborn.pydata.org/index.html).
* While geoplotlib does not have a thorough documentation, it did give us a great way to plot all of our points on a map. (https://andrea-cuttone.github.io/geoplotlib/).

## Primary Github repository
* https://github.com/janthonyiv98/Project_3

## Presentation Slides
* Can be found in the main repo under `Project 3 - NC Elemental Excursions.pdf`.
 * Slides were powered by [Canva](https://www.canva.com/).

## Group Members
* Joseph Anthony
* Everette Gough
* Joanna Lewis
* Keisha Maldonado
* Austin McConnell
* Michele di Sanctis
