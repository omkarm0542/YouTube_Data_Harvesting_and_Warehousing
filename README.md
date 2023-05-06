# YouTube_Data_Harvesting_and_Warehousing

This project is a Streamlit app that allows users to enter a YouTube channel ID, view channel details, and select channels to migrate to a data warehouse. The app retrieves data from the YouTube API, stores it in a MongoDB data lake, migrates it to a SQL data warehouse, queries the warehouse with SQL, and displays the data in the Streamlit app.

# Getting Started
*** Prerequisites***

To run this project, you will need:

a. Python 3.7 or higher

b. A Google Cloud Platform (GCP) project with YouTube API enabled

c. MongoDB installed and running locally

d. A SQL database such as MySQL or PostgreSQL installed and running locally


# Installing
1. Clone this repository:

> git clone https://github.com/your_username/youtube-data-visualization.git

2. Install the required Python packages:

> pip install -r requirements.txt

#Configuration

1. Set up a GCP project and enable the YouTube API. Follow the instructions to create a new project and enable the API.

2. Create a .env file in the root directory of the project and add the following variables:

```
GOOGLE_API_KEY=<your_gcp_api_key>

MONGO_URI=<your_mongo_uri>

DB_NAME=<your_mongo_db_name>

DB_COLLECTION=<your_mongo_collection_name>

SQLALCHEMY_DATABASE_URI=<your_sql_database_uri>
```

# Running the app
1. To start the app, run:

> streamlit run app.py

2. Open your browser and navigate to http://localhost:8501.

# Usage

1. Enter a YouTube channel ID in the input field and click the Get Channel Data button.

2. The app will retrieve the channel details and display them in a table.

3. Select the channels you want to migrate to the data warehouse by checking the corresponding boxes in the table.

4. Click the Migrate Data button to migrate the selected channels to the data warehouse.

5. The app will display a success message once the data has been migrated.

6. Enter a channel ID in the input field and click the Get Videos button to retrieve the videos for that channel.

7. The app will retrieve the videos and display them in a table.

8. Use the filter dropdowns to filter the data by video category and/or view count.

9. The app will display a bar chart of the top 10 videos based on view count for the selected filters.

# License

This project is licensed under the MIT License - see the LICENSE file for details.









