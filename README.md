# HHA504_assignment_nosql_dbs

## BigQuery
![db-creation](https://github.com/user-attachments/assets/9b85e167-34c6-4c21-8e43-cc0961937ca0)
![db-creation](https://github.com/user-attachments/assets/991ce5d0-2b99-41c3-aa59-30c35ec9858f)
![query&results](https://github.com/user-attachments/assets/dd350fef-bfe7-4382-8ed1-f68f623d4571)
![query-details](https://github.com/user-attachments/assets/fa44e7f9-131b-4a51-ac64-ca20362178cd)

### Reflection

- Using BigQuery for the assignment was straightforward. It was simple create the table through uploading the csv file containing the data. After creating the table, the features were easy to navigate for querying the data, viewing the query results, and finding the query details. To monitor the usage details of the query, all I had to do was expand the job history tab at the bottom of the page. However, I monitored the cost of running the query over several days, but the billing section of GCP showed no cost incurred. Thus, I assume the price was small enough to be negligible or cost little to nothing.

## MongoDB
![db-creation](https://github.com/user-attachments/assets/6ebc8480-0557-4967-85eb-8020fdf5f0b3)
![db-connection](https://github.com/user-attachments/assets/b7de8d80-ca8c-401b-bb88-e524e023bfe1)
![data-uploaded](https://github.com/user-attachments/assets/2052a7e4-2e8c-4113-9f0c-9ac849ebb261)
![query-results](https://github.com/user-attachments/assets/90301a29-a785-47b2-97b0-745c8fdcc783)

### Reflection

- Using MongoDB for the assignment was more complicated than BigQuery, but the features were still easy to navigate, especially when compared to Redis. The process of setting up and configuring the database took longer than BigQuery due to the additional element of writing code to convert the data to JSON format and using code to upload the data to the platform. After successfully running the code to convert the data and upload the data, I was able to query the data and obtain the results through the MongoDB browser instead of using the Compass application.

## Redis
![db-connection-details](https://github.com/user-attachments/assets/3a8b5218-4068-44ac-b6fa-a33fd6caa717)
![db-connection](https://github.com/user-attachments/assets/82b3e7d1-3de2-42e7-816e-3290ee8847fe)
![data-uploaded](https://github.com/user-attachments/assets/83cff392-63e8-40dd-a91c-21711ea0161d)
![query&results](https://github.com/user-attachments/assets/8255d7f8-b487-4ac2-9dc0-e82ce499092d)
![edited-data](https://github.com/user-attachments/assets/a3fe9590-af4a-4197-94a4-854f79997c22)

### Reflection
- My experience with Redis for the assignment was the most complicated. I found it to be complex to navigate for setting up and configuring the database. Similar to MongoDB, there was the element of writing code to convert the data to JSON format, set PatientID as the unique key, and upload the data to Redis. I was able to successfully run the code, but could not see the data on the Redis browser. The bulk of my time was spent on finding where the data was uploaded on Redis in order to reach the step of querying the data and updating the “Treatment Plan” value. Eventually, I realized that, unlike MongoDB, I needed to install the Redis Insight application to complete the remainder of the assignment. The fields to create the database on the Redis Insight application were slightly confusing because I did not know the username. I explored the configurations section on the Redis browser and found the default username under security. Then, I was able to connect to the database on Redis Insight, which was easier to navigate. From there, it was simple to query the data with the unique key and edit the values of the instance.
