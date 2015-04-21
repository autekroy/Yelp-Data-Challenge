# Yelp-Data-Challenge

Top foods in restaurants.

### About
 1. [Yelp Data Challenge](http://www.yelp.com/dataset_challenge)
 2. [Yelp's Academic Dataset Examples](https://github.com/Yelp/dataset-examples)

### Running Steps

 1. run `python split_review_on_business_ID.py`: create 2 folders (takes in 7 minuts)
  * `read_and_write_file` function:
    * `review_based_on_business_ID` folder (1.55 G)
    * review data based on different business ID, and file name is business ID
    * taek in 3 miuntes
  * `divide_review_on_category` function:
    * `review_based_on_business_and_category` folder (5.06 G)
    * review data based on category from above folder
    * may have same file in different category folder so the size of folder is larger
    * For everey category folder, there's a .json file (named after category) including every business id in this category
    * take in 4 minutes