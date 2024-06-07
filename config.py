SECRET_KEY = '12345'
 
SNOWFLAKE_CONFIG = {
    'account': 'zsmhnub-ir98847',
    'user': 'Meghana',
    'password': 'Maggi@3107',
    'database': 'CMS',
    'schema': 'public'
}

import snowflake.connector
# Function to establish Snowflake connection
def get_snowflake_connection():
    try:
        connection = snowflake.connector.connect(**SNOWFLAKE_CONFIG)
        return connection
    except Exception as e:
        print("An error occurred while connecting to Snowflake:", e)
        return None

# Snowflake connector instance
SNOWFLAKE_CONNECTOR = get_snowflake_connection()

