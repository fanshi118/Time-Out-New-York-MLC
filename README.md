## Final Project for Machine Learning for Cities Class

### Group Members
Shi Fan

Tianyi Gu

Xiaoge Wu

Yuxiang Zhang

### Project Description
We implemented a venue recommendation system for Foursquare users based on their historical check-in records. The data were collected indirectly from the Foursquare check-ins shared on Twitter. Our data contain all such records from Feb. 2014 to Feb. 2015 within New York City. We preprocessed the data using PySpark and extracted all the Foursquare check-in records from 113 GB geo-tagged tweets. Then, we scraped venue information for each unique venue that users checked in using the Foursquare's Public API. In addition, we scraped the network information for each user using the Twitter's Public API.

As for the analysis part, we plan to establish a similarity index for both users, by taking both spatio-temporal and contextual features (i.e. friends network) into account. Techniques involved include collaborative filtering and spectral clustering.

### Acknowledgement
The Twitter data were collected for research and academic purposes from the Twitter's Public API by the Visualization and Data Analysis lab at New York University (VIDA-NYU) — special thanks to Professor Huy T. Vo for making it available to us. 