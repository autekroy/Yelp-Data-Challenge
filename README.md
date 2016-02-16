# Yelp-Data-Challenge

Self project for own interests. Top foods in restaurants.

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
    * For everey category folder, a .json file (named after category) includes every business id in this category will be included in `_Category_business_list` folder
    * take in 4 minutes
2. run `python combine_review.py Restaurants`: create files contain all review in one business c
  * By choose a category (Ex: Restaurants), we create a training dataset and testing dataset for such category.
  * Create `dataset` to store training and testing dataset
  * Format of training and testing dataset (split by tab): business_id, review, stars

### Data Visualization
 1. [D3.js](https://github.com/mbostock/d3/wiki/Gallery)
    * [Bubble Chart](http://bl.ocks.org/mbostock/4063269)

### Programming Language, Tool & Library
 1. Python 2.7.6
    * [gensim](https://radimrehurek.com/gensim/index.html): for topic modeling
    * [vaderSentiment](https://pypi.python.org/pypi/vaderSentiment): for sentimental analysis
    * [NLTK - Natural Language ToolKit](http://textminingonline.com/dive-into-nltk-part-i-getting-started-with-nltk)

### Wikipedia Inspiration & method
 1. [Expectation–maximization algorithm](http://en.wikipedia.org/wiki/Expectation%E2%80%93maximization_algorithm): find maximum likelihood or maximum a posteriori (MAP) estimates of parameters in statistical models
 2. [Latent semantic analysis](http://en.wikipedia.org/wiki/Latent_semantic_analysis)
 3. [Latent Dirichlet allocation](http://en.wikipedia.org/wiki/Latent_Dirichlet_allocation)
 4. [Text Mining](http://en.wikipedia.org/wiki/Text_mining)
 5. [LSI](http://en.wikipedia.org/wiki/Latent_semantic_indexing)
 6. [SVD](http://en.wikipedia.org/wiki/Singular_value_decomposition)

### Other Dataset
 1. [SNPA Amazon reviews](http://snap.stanford.edu/data/web-Amazon.html)

### Reference
 1. [Improving Restaurants by Extracting Subtopics from Yelp Reviews](http://www.yelp.com/html/pdf/YelpDatasetChallengeWinner_ImprovingRestaurants.pdf)