# Amazon_Vine_Analysis

# Purpose / Background

Since your work with Jennifer on the SellBy project was so successful, you’ve been tasked with another, larger project: analyzing Amazon reviews written by members of the paid Amazon Vine program. The Amazon Vine program is a service that allows manufacturers and publishers to receive reviews for their products. Companies like SellBy pay a small fee to Amazon and provide products to Amazon Vine members, who are then required to publish a review.

In this project, you’ll have access to approximately 50 datasets. Each one contains reviews of a specific product, from clothing apparel to wireless products. You’ll need to pick one of these datasets and use PySpark to perform the ETL process to extract the dataset, transform the data, connect to an AWS RDS instance, and load the transformed data into pgAdmin. Next, you’ll use PySpark, Pandas, or SQL to determine if there is any bias toward favorable reviews from Vine members in your dataset. Then, you’ll write a summary of the analysis for Jennifer to submit to the SellBy stakeholders.


# Results


**How many Vine reviews and non-Vine reviews were there?**

![Screen Shot 2022-02-20 at 1 34 12 PM](https://user-images.githubusercontent.com/92615504/154858283-de595d7f-4d18-42b3-83c3-ddff3c792a2a.png)

![Screen Shot 2022-02-20 at 1 34 46 PM](https://user-images.githubusercontent.com/92615504/154858304-8b4b0731-36a5-4c48-ac51-2405e29a8e43.png)


**How many Vine reviews were 5 stars? How many non-Vine reviews were 5 stars?**

![Screen Shot 2022-02-20 at 1 36 05 PM](https://user-images.githubusercontent.com/92615504/154858358-cff85d9a-26a5-4c39-ae91-d47552895b69.png)

![Screen Shot 2022-02-20 at 1 36 19 PM](https://user-images.githubusercontent.com/92615504/154858366-cc974ffd-9fdb-48dc-9d31-0da35e3a28c4.png)



**What percentage of Vine reviews were 5 stars? What percentage of non-Vine reviews were 5 stars?**

![Screen Shot 2022-02-20 at 1 36 52 PM](https://user-images.githubusercontent.com/92615504/154858403-8f31ae0a-4fa3-423c-86fe-226f45ca5aee.png)

![Screen Shot 2022-02-20 at 1 37 56 PM](https://user-images.githubusercontent.com/92615504/154858458-0b4c4da6-07de-49c9-8a9a-0f775b5b46a3.png)


# Summary

Based on the images above, it can be determined that a solid 38% of the reviews were in the vine program. On the otherhand, a solid 54.5% of the reviews were non-vine. This all indicates a negative bias. I think a good additinal test would be standard diviation just to see if there any outlier data, a long with mean, median, mode. 
